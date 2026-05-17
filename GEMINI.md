# Target Domain LLM Wiki Project Instructions

This project documents the Matomo web analytics documentation using the Karpathy LLM Wiki pattern.

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
