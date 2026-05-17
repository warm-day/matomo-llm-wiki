import os
import sys
import subprocess
import shutil
import platform
import textwrap
import argparse
from datetime import datetime

def run_command(cmd, silent=True):
    try:
        # Using capture_output=True to keep the CLI clean unless there's an error
        result = subprocess.run(cmd, shell=True, check=True, capture_output=silent, text=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_pandoc():
    system = platform.system()
    print(f"Attempting to install Pandoc for {system}...")
    
    if system == "Darwin": # macOS
        if run_command("command -v brew"):
            return run_command("brew install pandoc", silent=False)
    elif system == "Linux":
        if run_command("command -v apt-get"):
            print("Note: This may require sudo password.")
            return run_command("sudo apt-get update && sudo apt-get install -y pandoc", silent=False)
        elif run_command("command -v yum"):
            return run_command("sudo yum install -y pandoc", silent=False)
    elif system == "Windows":
        if run_command("command -v winget"):
            return run_command("winget install pandoc", silent=False)
        elif run_command("command -v choco"):
            return run_command("choco install pandoc", silent=False)
    
    return False

def check_dependencies():
    print("\n--- [1/3] Checking System Dependencies ---")
    
    # 1. Python 3
    print(f"✅ Python {platform.python_version()} ... OK")

    # 2. Pandoc (Mandatory for non-MD sources)
    if run_command("pandoc --version"):
        print("✅ Pandoc is installed ... OK")
    else:
        print("❌ Pandoc NOT found.")
        success = install_pandoc()
        if success:
            print("✅ Pandoc installed successfully.")
        else:
            print("\nFATAL: Pandoc is required to convert technical documents (PDF, Docx, etc.) to Markdown.")
            print("Please install it manually:")
            print(" - macOS: brew install pandoc")
            print(" - Linux: sudo apt-get install pandoc")
            print(" - Windows: winget install pandoc")
            sys.exit(1)

    # 3. mdsplit (Mandatory for partitioning)
    if run_command("mdsplit -h"):
        print("✅ mdsplit is installed ... OK")
    else:
        print("📦 mdsplit NOT found. Installing via pip...")
        if run_command(f"{sys.executable} -m pip install mdsplit"):
            print("✅ mdsplit installed successfully.")
        else:
            print("\nFATAL: Failed to install mdsplit via pip.")
            sys.exit(1)

    # 4. mdformat (Mandatory for normalization)
    if run_command("mdformat --version"):
        print("✅ mdformat is installed ... OK")
    else:
        print("📦 mdformat NOT found. Installing via pip...")
        if run_command(f"{sys.executable} -m pip install mdformat mdformat-gfm"):
            print("✅ mdformat installed successfully.")
        else:
            print("\nFATAL: Failed to install mdformat via pip.")
            sys.exit(1)

def init_structure(target_dir):
    print("\n--- [2/3] Initializing Folder Structure ---")
    folders = [
        "raw", 
        "wiki", 
        "staging", 
        "audit", 
        "knowledge-ingest/scripts", 
        "knowledge-ingest/references",
        "knowledge-ingest/assets",
        ".github",
        ".agents/skills"
    ]
    for f in folders:
        path = os.path.join(target_dir, f)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"  [+] Created: {f}/")
            if not f.startswith("."):
                with open(os.path.join(path, ".gitkeep"), "w") as keep:
                    pass
        else:
            print(f"  [.] Checked: {f}/ (exists)")

def register_skill(target_dir):
    print("\n--- [2.5/3] Registering Agent Skill (Universal) ---")
    skill_link = os.path.join(target_dir, ".agents", "skills", "knowledge-ingest")
    
    # Clean up existing link if it exists
    if os.path.exists(skill_link) or os.path.islink(skill_link):
        if os.path.islink(skill_link):
            os.unlink(skill_link)
        else:
            shutil.rmtree(skill_link)

    try:
        # Create relative symlink for cross-PC portability: .agents/skills/ki -> ../../knowledge-ingest
        if platform.system() == "Windows":
             os.symlink(os.path.abspath(os.path.join(target_dir, "knowledge-ingest")), skill_link, target_is_directory=True)
        else:
             os.symlink("../../knowledge-ingest", skill_link)
        print("  [+] Registered: knowledge-ingest (Universal Agent Skill)")
    except Exception as e:
        print(f"  [!] Skill Link Failed: {e}")
        print("      To fix manually, run: gemini skills link ./knowledge-ingest")

def write_boilerplate(target_dir, domain):
    print(f"\n--- [3/3] Deploying Boilerplate for '{domain}' ---")
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # 1. Mandatory Instructions (GEMINI.md)
    mandate_content = textwrap.dedent(f"""\
        # {domain} LLM Wiki Project Instructions

        This project documents the {domain} system using the Karpathy LLM Wiki pattern.

        ## Foundational Mandates

        - **Knowledge Ingestion**: ALL source ingestion must be performed using the `knowledge-ingest` skill. Activation: `activate_skill(name="knowledge-ingest")`.
        - **Semantic Parity**: 100% of technical details (code blocks, config flags, specs) must be accurately migrated from raw sources. This is enforced by the **Worker-Audit** workflow orchestrated by the Main Agent as defined in the skill.
        - **Context Management**: For large files, use the **Segmented Ingestion** workflow to avoid context loss. The Main Agent acts as the Orchestrator, while sub-agents act as specialized Workers.

        ## Folder structure

        ```
        raw/          -- source documents (immutable)
        staging/      -- temporary verbatim chunks (maintained by skill)
        wiki/         -- markdown pages maintained by Gemini CLI
        wiki/index.md -- table of contents
        wiki/log.md   -- append-only record of all operations
        audit/        -- machine-generated parity reports
        ```

        ## Wiki Standards

        ### 1. Page Format
        Every wiki page MUST follow the template in `knowledge-ingest/references/wiki-schema.md`:
        - Title and 1-2 sentence Summary.
        - Sources list (pointing to `raw/`).
        - "Last updated" timestamp.
        - Structured content with bold scannability.
        - "Related pages" section with `[[wiki-links]]`.

        ### 2. Citation & Naming
        - **Citations**: Every factual claim must reference its source file in the format `(source: filename.md)`.
        - **Naming**: File names must be lowercase with hyphens (e.g., `ecommerce-tracking.md`).
        - **Plain Language**: Write in clear, plain language while preserving 100% of technical accuracy.

        ### 3. Question Answering
        When answering questions:
        1. Read `wiki/index.md` first to locate relevant pages.
        2. Read those pages and synthesize a grounded answer.
        3. Cite specific wiki pages in the response.
        4. If an answer is valuable, offer to save it as a new wiki page.

        ### 4. Recursive Indexing
        - Every new concept page must be linked from its category `index.md`.
        - Category indexes must be linked from the root `wiki/index.md`.
        - Index updates are mandatory and must happen during the synthesis loop.

        ## Audit & Linting
        The `knowledge-ingest` skill uses a **Worker-Audit** process for semantic parity checks. For structural and cross-page audits:
        - Check for contradictions between pages.
        - Find orphan pages (no inbound links).
        - Identify missing concept pages for mentioned terms.
        - Flag outdated claims based on newer sources.
    """)

    skill_content = textwrap.dedent(f"""\
        ---
        name: knowledge-ingest
        description: A robust ETL pipeline for ingesting large technical sources into an LLM Wiki. Use when adding new sources to raw/ to ensure 100% data parity through deterministic partitioning, micro-audits, and progressive synthesis.
        ---

        # Knowledge Ingest Skill

        This skill provides a deterministic workflow for migrating large technical documents into a structured, cross-linked LLM Wiki. It focuses on **Data Parity** (ensuring no technical details are lost) and **Context Efficiency**.

        ## Mandatory Folders
        - `raw/`: Immutable source files.
        - `staging/`: Temporary verbatim chunks for iterative synthesis.
        - `wiki/`: The target knowledge base.
        - `audit/`: Folder for machine-generated audit reports.

        ## Phase 1: Pre-Processing (Deterministic)
        1. **Convert**: Run `pandoc` to normalize any source (PDF, DOCX) to Markdown.
        2. **Sanity Check**: Run `knowledge-ingest/scripts/sanity_check.py` to ensure the MD conversion is readable.
        3. **Ghost Headers (Optional)**: If the document lacks structure, perform a Discovery Pass to insert `## [Ingest Chunk]` headers.
        4. **Partition**: Run `knowledge-ingest/scripts/partition.py`. This uses `mdsplit` to break the source into chunks in `staging/`.

        ## Phase 2: Synthesis Loop (Iterative Orchestration)
        *The Main Agent acts as the Orchestrator. Recursively process all `.md` files in `staging/`:*

        > **ORCHESTRATOR WARNING**: Do NOT pass the contents of this `SKILL.md` file to sub-agents. It contains orchestration logic that will confuse them. Always point sub-agents to the specific worker guidelines in `references/`.

        1. **Invoke Synthesis Sub-Agent**: Use `invoke_agent` with the `generalist` sub-agent.
            - **Prompt**: "Act as a **Synthesis Worker**. Follow the instructions in `references/worker-synthesis.md` to process `staging/<chunk>.md`. Apply schemas from `references/wiki-schema.md`."
        2. **Recursive Indexing**: (Main Agent) Immediately update local and global index files.
        3. **Invoke Audit Sub-Agent**: Use `invoke_agent` with a *fresh* `generalist` sub-agent call.
            - **Prompt**: "Act as an **Auditor Worker**. Follow the instructions in `references/worker-audit.md` to verify `staging/<chunk>.md` against the updated wiki. Generate the report in `audit/audit_<chunk>.md`."
        4. **Graduate**: (Main Agent) Once the Audit Sub-Agent returns "PASSED", delete the chunk and move to the next file.

        ## Phase 3: Finalization
        1. **Link Linting**: Run `knowledge-ingest/scripts/lint_wiki.py` to ensure no orphaned pages or dead links.
        2. **Global Context Check**: Invoke a sub-agent to review the entire new category for logical consistency and redundancy.
        3. **Cleanup**: Delete all `audit/audit_chunk_*.md` files.
        4. **Log**: Record the completion in `wiki/log.md`.

        ## Quality Mandates
        - **Semantic Parity**: 100% of technical details (code blocks, config flags, specs) MUST be accurately migrated.
        - **Bold Scannability**: Use bold headers and short paragraphs as defined in `references/wiki-schema.md`.
        - **Verified Reachability**: Every page MUST be reachable from `wiki/index.md`. Orphaned pages or dead links are failures.
        - **Global Consistency**: No contradictory instructions or duplicate pages across the same source domain.
    """)

    worker_synthesis_content = textwrap.dedent("""\
        # Worker Instruction: Wiki Synthesis

        You are a **Synthesis Worker**. Your sole purpose is to transform raw technical content from a `staging/` chunk into a structured wiki page.

        ## Boundary Rules
        - **DO NOT** attempt to invoke other agents (`invoke_agent` tool).
        - **DO NOT** attempt to manage the overall ingestion pipeline.
        - **DO NOT** read or reference `SKILL.md`.

        ## Task Workflow
        1. **Read Target**: Read the specific `.md` file in `staging/` provided in your prompt.
        2. **Refresh Context**: Read the relevant `wiki/` pages mentioned to ensure continuity.
        3. **Synthesis**: Apply the formatting and technical mandates from `references/wiki-schema.md`.
        4. **Output**: Write or update the wiki files as instructed.

        ## Quality Standards
        - Ensure 100% semantic parity for all technical tokens (code, versions, specs).
        - Use **Bold Scannability** for headers and key terms.
        - Provide a brief summary of what was changed and any minor exclusions.
    """)

    worker_audit_content = textwrap.dedent("""\
        # Worker Instruction: Micro-Audit

        You are an **Auditor Worker**. Your sole purpose is to verify that technical content from a source chunk has been perfectly migrated to the wiki.

        ## Boundary Rules
        - **DO NOT** attempt to invoke other agents (`invoke_agent` tool).
        - **DO NOT** attempt to manage the overall ingestion pipeline.
        - **DO NOT** read or reference `SKILL.md`.

        ## Task Workflow
        1. **Compare**: Compare the provided `staging/<chunk>.md` against the updated `wiki/` pages.
        2. **Verify Parity**: Ensure every code block, version number, configuration flag, and technical specification has been accurately migrated.
        3. **Fix (If Needed)**: If any technical detail is missing or incorrect, fix the wiki file immediately.
        4. **Report**: Generate a brief report in `audit/audit_<chunk>.md` summarizing the verification.

        ## Output
        - Respond with **PASSED** only when 100% semantic parity is achieved.
    """)

    schema_content = textwrap.dedent("""\
        # Wiki Schema & Formatting Guide

        Use these templates and rules for all wiki pages created or updated via the `knowledge-ingest` skill.

        ## Page Template

        ```markdown
        # Page Title

        **Summary**: One to two sentences describing this page.

        **Sources**: [[raw/source-filename.md]]

        **Last updated**: YYYY-MM-DD

        ---

        ## Technical Details / Main Heading
        - **Key Token**: Verbatim description or code snippet.
        - **Requirement**: Use bolding for scannability.

        ## Related pages
        - [[related-concept]]
        - [[index|Category Index]]
        ```

        ## Mandatory Rules

        ### 1. Semantic Parity (Non-Negotiable)
        - Every code block (```...```) from the source must be represented.
        - Every function name, variable, or CLI command in backticks (`code`) must be migrated.
        - Every numerical specification (e.g., "PHP 7.2.5", "15 seconds") must be retained.
        - Note: The Audit Sub-Agent allows for intelligent reformatting, but the technical fact itself MUST exist in the wiki.

        ### 2. Bold Scannability
        - Use **Bold** for the start of list items or key technical terms.
        - Avoid large "wall of text" paragraphs.
        - Use sub-headers liberally to group related technical tokens.

        ### 3. Citations
        - Every factual claim should follow the format: (source: filename.md).
        - Cite the original `raw/` file, not the `staging/` chunk.

        ### 4. Interlinking
        - Every new page must link back to its category `index.md`.
        - Category indexes must link back to the root `wiki/index.md`.
        - Use contextual links `[[like-this]]` within paragraphs to build a non-linear web.

        ### 5. Categorization
        - Keep file names lowercase with hyphens: `cross-domain-tracking.md`.
        - Group related pages into folders: `wiki/installation/`, `wiki/data-collection/`, etc.
    """)

    files = {
        "GEMINI.md": mandate_content,
        "CLAUDE.md": mandate_content,
        ".github/copilot-instructions.md": mandate_content + "\n\n## Agent Skills\nSpecialized workflows are available in `.agents/skills/knowledge-ingest/SKILL.md`.",
        ".gitignore": textwrap.dedent("""\
            # LLM Wiki Ignores
            staging/*
            !staging/.gitkeep
            audit/*.md
            .DS_Store
            __pycache__/
            *.pyc
        """),
        "wiki/index.md": textwrap.dedent(f"""\
            # {domain} LLM Wiki Index

            Welcome to the technical knowledge base for {domain}.

            ## Categories
            - Core Concepts (Placeholder)
            - API Reference (Placeholder)
            - Deployment & Ops (Placeholder)

            ---
            *Last updated: [[wiki/log.md|Recent Activity]]*
        """),
        "wiki/log.md": textwrap.dedent(f"""\
            # Wiki Log

            | Date | Source | Operation | Auditor |
            | :--- | :--- | :--- | :--- |
            | {current_date} | System | Initialized Wiki | bootstrap.py |
        """),
        "knowledge-ingest/SKILL.md": skill_content,
        "knowledge-ingest/references/worker-synthesis.md": worker_synthesis_content,
        "knowledge-ingest/references/worker-audit.md": worker_audit_content,
        "knowledge-ingest/references/wiki-schema.md": schema_content,
        "knowledge-ingest/scripts/partition.py": textwrap.dedent("""\
            import os
            import sys
            import subprocess
            import argparse
            import re

            def run_command(cmd, verbose=True):
                try:
                    result = subprocess.run(cmd, shell=True, check=False, capture_output=True, text=True)
                    if result.returncode == 0:
                        return result.stdout
                    if verbose:
                        print(f"Command failed: {cmd}")
                        print(f"Error: {result.stderr}")
                    return None
                except Exception as e:
                    if verbose:
                        print(f"Exception running command {cmd}: {e}")
                    return None

            def partition_source(source_file, output_dir, max_level=2):
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                # 1. Normalize to Markdown using Pandoc if necessary
                base, ext = os.path.splitext(source_file)
                md_source = source_file
                if ext.lower() != '.md':
                    md_source = f"{base}.md"
                    print(f"Converting {source_file} to {md_source} via Pandoc...")
                    run_command(f"pandoc '{source_file}' -o '{md_source}'")

                # 2. Normalize via mdformat
                print(f"Standardizing {md_source} via mdformat...")
                run_command(f"mdformat --number '{md_source}'")

                # 3. Try mdsplit (Header-based partitioning)
                print(f"Attempting to partition {md_source} via mdsplit...")
                # Fix: mdsplit uses -h or no args for help
                if run_command("mdsplit -h", verbose=False) is not None:
                    # Use --force and correct argument names
                    cmd = f"mdsplit '{md_source}' --output '{output_dir}' --max-level {max_level} --force"
                    if run_command(cmd) is not None:
                        chunks = [f for f in os.listdir(output_dir) if f.endswith('.md')]
                        if len(chunks) > 1:
                             print(f"Success: Source partitioned into {len(chunks)} chunks via mdsplit.")
                             return

                print("mdsplit failed or was ineffective. Using Landmark-Aware partitioning...")
                landmark_split(md_source, output_dir)

            def landmark_split(source_file, output_dir):
                \"\"\"
                Surgical Fix: Recognized numbered bold headers common in Notion/Pandoc outputs.
                \"\"\"
                with open(source_file, 'r') as f:
                    content = f.read()

                # Split by horizontal rules, triple newlines, or numbered bold headers
                pattern = r'(\\n---\\n|\\n\\*\\*\\*\\n|\\n\\n\\n|\\n[0-9]+\\. \\*\\*.*)'
                parts = re.split(pattern, content)
                
                # Merge delimiters back with their following content
                merged_parts = []
                current_part = ""
                
                for part in parts:
                    if re.match(pattern, part):
                        if current_part.strip():
                            merged_parts.append(current_part)
                        current_part = part
                    else:
                        current_part += part
                        
                if current_part.strip():
                    merged_parts.append(current_part)

                # Write parts to staging
                written_count = 0
                for i, p in enumerate(merged_parts):
                    if len(p.strip()) < 100: # Skip tiny fragments
                        continue
                    chunk_path = os.path.join(output_dir, f"chunk_{written_count+1:02d}.md")
                    with open(chunk_path, 'w') as f:
                        f.write(p.strip())
                    written_count += 1
                
                if written_count > 0:
                    print(f"Success: Source partitioned into {written_count} chunks in '{output_dir}'.")
                else:
                    print("Error: Landmark split failed to produce chunks.")

            if __name__ == "__main__":
                parser = argparse.ArgumentParser(description="Partition a technical source for ingestion.")
                parser.add_argument("source", help="Path to the raw source file")
                parser.add_argument("--output", default="staging", help="Output directory for chunks")
                parser.add_argument("--level", type=int, default=2, help="Max header level for mdsplit")
                
                args = parser.parse_args()
                partition_source(args.source, args.output, args.level)
        """),
        "knowledge-ingest/scripts/sanity_check.py": textwrap.dedent("""\
            import os
            import sys
            import argparse

            def sanity_check(file_path):
                \"\"\"
                Checks if a markdown file is readable and likely not scrambled.
                \"\"\"
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    
                if not lines:
                    print(f"Sanity Check FAILED: {file_path} is empty.")
                    return False
                    
                # Check for garbage characters (binary-ish)
                total_chars = 0
                garbage_chars = 0
                for line in lines:
                    total_chars += len(line)
                    for char in line:
                        if not char.isprintable() and char not in ['\\n', '\\t', '\\r']:
                            garbage_chars += 1
                            
                garbage_ratio = garbage_chars / total_chars if total_chars > 0 else 0
                if garbage_ratio > 0.05:
                    print(f"Sanity Check FAILED: High garbage character density ({garbage_ratio:.2%}).")
                    return False
                    
                # Check for extremely long lines without whitespace (typical of PDF encoding errors)
                for i, line in enumerate(lines):
                    if len(line) > 500 and ' ' not in line:
                        print(f"Sanity Check FAILED: Extremely long line without whitespace at line {i+1}.")
                        return False
                        
                print(f"Sanity Check PASSED for {file_path}.")
                return True

            if __name__ == "__main__":
                parser = argparse.ArgumentParser(description="Sanity check for converted sources.")
                parser.add_argument("file", help="Path to the file to check")
                args = parser.parse_args()
                
                if sanity_check(args.file):
                    sys.exit(0)
                else:
                    sys.exit(1)
        """),
        "knowledge-ingest/scripts/lint_wiki.py": textwrap.dedent("""\
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
                links = re.findall(r'\\[\\[([^\\]|]+)(?:\\|[^\\]]+)?\\]\\]', content)
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
                    print("\\n--- DEAD LINKS FOUND ---")
                    for error in errors:
                        print(error)
                        
                if orphans:
                    print("\\n--- ORPHANED FILES FOUND (No inbound links) ---")
                    for orphan in orphans:
                        print(orphan)
                        
                if not errors and not orphans:
                    print("\\nWiki LINT PASSED: All links valid and no orphans found.")
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
        """)
    }

    for path, content in files.items():
        full_path = os.path.join(target_dir, path)
        if not os.path.exists(full_path):
            with open(full_path, "w") as f:
                f.write(content)
            print(f"  [+] Deployed: {path}")
        else:
            print(f"  [.] Skipped: {path} (exists)")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM Wiki Production Bootstrap Tool")
    parser.add_argument("--domain", default="Target Domain", help="The system/domain being documented")
    parser.add_argument("--out", default=".", help="Target directory for deployment")
    args = parser.parse_args()

    print("\n" + "="*50)
    print("   LLM Wiki Production Bootstrap Tool")
    print("="*50)
    
    check_dependencies()
    init_structure(args.out)
    register_skill(args.out)
    write_boilerplate(args.out, args.domain)
    
    print("\n✅ Deployment Complete!")
    print(f"   Project Domain : {args.domain}")
    print(f"   Target Folder  : {os.path.abspath(args.out)}")
    print("-" * 50)
    print("   Next steps:")
    print(f"   1. Update GEMINI.md with your {args.domain} specifics.")
    print("   2. Drop your first technical source into raw/")
    print("   3. Activate the skill: activate_skill(name='knowledge-ingest')")
    print("="*50 + "\n")