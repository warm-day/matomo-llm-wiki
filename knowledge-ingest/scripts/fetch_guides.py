import os
import sqlite3
import time

# Since browser-harness is installed as an editable module, we can import its helpers directly.
from browser_harness.helpers import new_tab, wait_for_load, js
from browser_harness.admin import ensure_daemon

# Constants
DB_PATH = "knowledge-ingest/scraper_manifest.db"
RAW_DIR = "raw/guides"

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS manifest (
            url TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            type TEXT NOT NULL,
            category TEXT
        )
    ''')
    
    # Insert ROOT if it doesn't exist
    cursor.execute('''
        INSERT OR IGNORE INTO manifest (url, status, type, category)
        VALUES (?, ?, ?, ?)
    ''', ("https://matomo.org/guides/", "PENDING", "ROOT", None))
    
    conn.commit()
    return conn

def add_url(conn, url, status, type_val, category=None):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO manifest (url, status, type, category)
        VALUES (?, ?, ?, ?)
    ''', (url, status, type_val, category))
    conn.commit()
    return cursor.rowcount > 0

def update_status(conn, url, status):
    cursor = conn.cursor()
    cursor.execute('UPDATE manifest SET status = ? WHERE url = ?', (status, url))
    conn.commit()

def get_next_pending(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT url, type, category FROM manifest 
        WHERE status = "PENDING" 
        ORDER BY 
            CASE type 
                WHEN 'ARTICLE' THEN 1 
                WHEN 'CATEGORY' THEN 2 
                WHEN 'ROOT' THEN 3 
            END
        LIMIT 1
    ''')
    return cursor.fetchone()

def get_links_containing(pattern):
    """Executes JS in the browser to return all links containing a specific string pattern."""
    script = f"""
        Array.from(document.querySelectorAll('a'))
             .map(a => a.href)
             .filter(href => href.includes('{pattern}'))
    """
    return js(script)

def get_article_content():
    """Extracts the main content of the article to avoid headers/footers/menus."""
    script = """
        let container = document.querySelector('article') 
                     || document.querySelector('main') 
                     || document.querySelector('.content') 
                     || document.body;
        return container.innerText || container.textContent;
    """
    return js(script)

def main():
    conn = init_db()
    
    # Make sure the daemon is running before we start calling new_tab()
    ensure_daemon()
    
    TARGET_ARTICLES = 5
    articles_downloaded = 0
    urls_processed = 0

    print(f"Starting fetch job. Target articles to download: {TARGET_ARTICLES}")

    while articles_downloaded < TARGET_ARTICLES:
        pending = get_next_pending(conn)
        
        if not pending:
            print("No PENDING URLs found in the manifest.")
            break

        url, type_val, category = pending
        print(f"[{articles_downloaded}/{TARGET_ARTICLES} Articles] Processing: {url} ({type_val})")
        
        try:
            # 1. Navigate to the page
            new_tab(url)
            wait_for_load()
            time.sleep(2) # Buffer for dynamic rendering
            
            # 2. Extract based on page type
            if type_val == "ROOT":
                # Find categories: links inside /guide/ but not /faq/
                all_guides_links = get_links_containing("matomo.org/guide/")
                
                new_categories = 0
                for link in all_guides_links:
                    link = link.split('#')[0] # Remove anchors
                    if "/faq/" not in link and link != url:
                        if add_url(conn, link, "PENDING", "CATEGORY"):
                            new_categories += 1
                
                print(f"  -> Discovered {new_categories} new categories.")
                update_status(conn, url, "DOWNLOADED")
                
            elif type_val == "CATEGORY":
                # Find specific guides: links inside /faq/
                all_faq_links = get_links_containing("matomo.org/faq/")
                
                category_slug = url.strip("/").split("/")[-1]
                new_faqs = 0
                for link in all_faq_links:
                    link = link.split('#')[0]
                    if add_url(conn, link, "PENDING", "ARTICLE", category_slug):
                        new_faqs += 1
                        
                print(f"  -> Discovered {new_faqs} new FAQs/Guides.")
                update_status(conn, url, "DOWNLOADED")
                
            elif type_val == "ARTICLE":
                content = get_article_content()
                
                # Format paths
                cat_folder = category if category else "uncategorized"
                article_id = url.strip("/").split("/")[-1]
                save_dir = os.path.join(RAW_DIR, cat_folder)
                os.makedirs(save_dir, exist_ok=True)
                
                save_path = os.path.join(save_dir, f"{article_id}.md")
                
                # Save markdown file
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(f"<!-- Source: {url} -->\\n\\n")
                    f.write(content)
                    
                print(f"  -> Saved to {save_path}")
                update_status(conn, url, "DOWNLOADED")
                articles_downloaded += 1

        except Exception as e:
            print(f"  -> ERROR processing {url}: {str(e)}")
            # We skip marking as downloaded so it will retry next time
            
        urls_processed += 1

    print(f"Job complete. Downloaded {articles_downloaded} articles across {urls_processed} URL visits.")
    conn.close()

if __name__ == "__main__":
    main()
