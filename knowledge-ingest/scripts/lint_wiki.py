import os
import re
import sys

def get_all_md_files(directory):
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, file), directory)
                md_files.append(rel_path)
    return md_files

def extract_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Matches [[link]] or [[link|text]]
    # Also handles relative paths inside the brackets
    links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    return links

def lint_wiki(wiki_dir):
    all_files = get_all_md_files(wiki_dir)
    file_to_links = {}
    all_targets = set()
    
    # Normalize paths to be relative to wiki_dir
    normalized_files = set(all_files)
    
    print(f"Scanning {len(all_files)} files in {wiki_dir}...")
    
    errors = []
    orphans = set(normalized_files)
    orphans.discard("index.md") # The root index doesn't need to be linked to
    
    for rel_path in all_files:
        full_path = os.path.join(wiki_dir, rel_path)
        links = extract_links(full_path)
        file_to_links[rel_path] = links
        
        dir_context = os.path.dirname(rel_path)
        
        for link in links:
            # Handle directory traversal and index implicit linking
            target = link.strip()
            
            # 1. Try direct path
            target_path = target if target.endswith(".md") else f"{target}.md"
            
            # Resolve relative paths (e.g. ../matomo-overview)
            resolved_path = os.path.normpath(os.path.join(dir_context, target_path))
            
            # ALLOWANCE: Links to the raw/ folder are valid but live outside wiki/
            if resolved_path.startswith("../raw/"):
                continue

            if resolved_path in normalized_files:
                all_targets.add(resolved_path)
                orphans.discard(resolved_path)
            else:
                # 2. Try implicit index (folder/ -> folder/index.md)
                index_path = os.path.normpath(os.path.join(dir_context, target, "index.md"))
                if index_path in normalized_files:
                    all_targets.add(index_path)
                    orphans.discard(index_path)
                else:
                    errors.append(f"DEAD LINK: '{link}' in {rel_path} (Resolved to: {resolved_path})")

    # Output results
    if errors:
        print("\n--- DEAD LINKS FOUND ---")
        for error in errors:
            print(error)
            
    if orphans:
        print("\n--- ORPHANED FILES FOUND (No inbound links) ---")
        for orphan in orphans:
            print(orphan)
            
    if not errors and not orphans:
        print("\nWiki LINT PASSED: All links valid and no orphans found.")
        return True
    else:
        return False

if __name__ == "__main__":
    wiki_directory = "wiki"
    if not os.path.exists(wiki_directory):
        print(f"Error: {wiki_directory} directory not found.")
        sys.exit(1)
        
    if lint_wiki(wiki_directory):
        sys.exit(0)
    else:
        sys.exit(1)
