# Self-healing LLM Wiki

Inspired by [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), this repository implements a self-healing pipeline that converts raw documents into a structured, LLM-navigable knowledge graph. It uses a worker-auditor agent architecture to ensure zero technical details are lost during ingestion.

**Note:** Matomo web analytics guides and documentation were used in this project for demonstration of the workflow and the resulting wiki.

## Installation & Usage

### 1. To view the Demo
If you want to view the implementation example:
```bash
git clone https://github.com/warm-day/matomo-llm-wiki.git
```
You can explore the `wiki/` directory directly or use an AI assistant to query the knowledge base.

### 2. To start a New Project
If you want to create a new LLM Wiki for your own purposes, just use the provided bootstrap script:
```bash
python3 bootstrap_wiki.py
```
**What it does:** This script checks your system dependencies (like Pandoc, mdformat, mdsplit), initializes the mandatory folder structure (`raw/`, `wiki/`, `staging/`, `audit/`), deploys the `knowledge-ingest` agent skill, and scaffolds out the initial boilerplate files including index logs, templates, and Python utility scripts.

After that you can drop your own files into `raw/` and start the ingestion process by pointing LLM into the root of your project and ask to **ingest** a specific file.

## Browser Harness (Optional Automation)

Included in the repository is the **[browser-harness](browser-harness/)**, an optional but powerful tool that connects an LLM directly to a real browser. It provides a thin, editable Chrome DevTools Protocol (CDP) harness that allows the agent to navigate the web, extract data, or automate routine tasks with complete freedom.

When paired with GitHub Actions, the `browser-harness` can create a fully autonomous pipeline. For instance, the repository includes a `.github/workflows/fetch-guides.yml` action that uses the harness to automatically scrape new Matomo guides from matomo.org, so you won't need to manually find and drop those files into the project.

1. **Automated Scraping**: The GitHub Action runs daily (or manually), launching a headless browser in the Ubuntu runner.
2. **Fetching Content**: A Python script (`knowledge-ingest/scripts/fetch_guides.py`) drives the `browser-harness` to scrape the latest web content.
3. **Committing Raw Data**: It saves these new guides directly into the `raw/guides/` folder and commits them to the repository, ready to be ingested by the main LLM Wiki pipeline.

## Architecture Overview

<details>
<summary><b>Click to expand Detailed Architecture</b></summary>

### Directory Structure
- **`raw/`**: The immutable source of truth. Original PDFs, Docx, or massive Markdown files (and automated scrapes in `raw/guides/`) are placed here.
- **`staging/`**: A temporary workspace where the pipeline breaks massive source files into atomic, digestible chunks.
- **`wiki/`**: The active knowledge graph. Contains the final, synthesized Markdown pages.
  - **`wiki/index.md`**: The Global Cross-Project Index (the entry point for the LLM).
  - **`wiki/<domain>/index.md`**: The Per-Project Hub (e.g., `matomo/index.md`), linking to all atomic pages within that domain.
- **`audit/`**: A paper trail of machine-generated reports verifying that 100% of technical details were successfully migrated from `staging/` to `wiki/`.
- **`knowledge-ingest/`**: Contains the core logic, scripts, and worker instructions that power the pipeline.
- **`browser-harness/`**: Core package for headless browser automation and web extraction.
- **`.github/`**: Houses GitHub Actions for automating tasks like daily fetches using the browser harness.

### Core Philosophy
- **Atomicity**: Large documents are broken down into granular, focused pages (e.g., `user-roles.md`, `ab-testing.md`) to prevent LLM context-window degradation ("lost in the middle").
- **Semantic Parity**: The pipeline guarantees that zero technical facts, code blocks, or configuration flags are lost during the transition from raw text to the structured wiki.
- **Iterative Orchestration**: A Main Agent (Orchestrator) manages the pipeline, delegating heavy text-processing to specialized Sub-Agents (Synthesis and Audit Workers).

### Knowledge Ingestion Pipeline: Step-by-Step Flow

The pipeline is triggered by activating the `knowledge-ingest` skill. It executes in three distinct phases:

#### Phase 1: Pre-Processing (Deterministic)
The goal of this phase is to prepare the raw document for LLM ingestion using fast, deterministic Python scripts.

1. **Conversion**: If the source is not Markdown, `pandoc` normalizes it.
2. **Sanity Check**: `sanity_check.py` scans the file for encoding errors, garbage characters, or unreadable formatting.
3. **Partitioning**: `partition.py` breaks the massive source file into smaller `chunk_*.md` files (typically under 20KB each) and places them in the `staging/` directory. It uses header-based splitting (`mdsplit`) or falls back to Landmark-Aware splitting to ensure chunks are logically sound.

#### Phase 2: Synthesis Loop (Iterative Orchestration)
This is the core AI-driven engine. For every chunk in the `staging/` folder, the Orchestrator executes a strict **Plan -> Act -> Validate** loop.

1. **Synthesis (Act)**:
   - The Orchestrator invokes a **Synthesis Worker** sub-agent.
   - The Worker is instructed to read the specific `staging/chunk_XX.md`.
   - If the topic is new, the Worker creates a new atomic wiki page. If the topic exists, it reads the existing page and splices the new information in non-destructively.
   - The Worker applies the mandatory `wiki-schema.md` (adding summaries, bold scannability, and source citations).
2. **Recursive Indexing**:
   - The Orchestrator or Worker immediately updates the local category index (e.g., `matomo/index.md`) to ensure the new page is discoverable.
3. **Micro-Audit (Validate)**:
   - The Orchestrator invokes an independent **Auditor Worker** sub-agent.
   - The Auditor's sole job is to compare the original `staging/chunk_XX.md` against the newly updated `wiki/` pages.
   - It checks for **100% Semantic Parity**: verifying every single CLI command, IP address, code snippet, and configuration flag was migrated accurately.
   - If a fact is missing, the Auditor fixes the wiki page immediately. It outputs a report to `audit/audit_chunk_XX.md`.
4. **Graduation**:
   - Once the Auditor returns `PASSED`, the Orchestrator deletes the staging chunk and moves to the next one.

#### Phase 3: Finalization & Self-Healing
Once all chunks are processed, the pipeline performs structural validation across the entire knowledge base.

1. **Link Linting**:
   - The pipeline executes `lint_wiki.py`, which scans all `.md` files in the `wiki/` directory.
   - It enforces referential integrity: flagging any "dead links" or "orphaned pages" (pages with no inbound links).
2. **Global Context Check**:
   - A final agent pass reviews the newly updated category as a whole to ensure there are no redundant pages or logical contradictions created during the chunk-by-chunk ingestion.
3. **Cleanup**:
   - The temporary `audit/audit_chunk_*.md` files are automatically deleted, keeping the repository clean.
4. **Audit Trail Logging**:
   - A final entry is written to `wiki/log.md`, establishing an immutable record of when the source was ingested and who orchestrated it.

#### Updating Existing Knowledge
Because of the Orchestrator-Worker design, the pipeline natively handles updates. If a small patch document is dropped into `raw/`, the pipeline will partition it, read the *existing* wiki pages, and surgically update them with the new facts, followed by the rigorous Micro-Audit to ensure nothing was accidentally deleted.

</details>
