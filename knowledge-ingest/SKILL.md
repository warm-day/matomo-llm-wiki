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
