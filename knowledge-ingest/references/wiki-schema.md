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
