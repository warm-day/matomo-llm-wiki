# Forms Tracking

**Summary**: Advanced tracking for online forms, providing insights into conversion rates, drop-offs, and field-level user behavior.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Implementation
This is a **paid feature** that automatically discovers forms on your website.

### Manual Configuration
If automatic discovery is insufficient, forms can be configured via **Administration > Forms > Manage Forms**:
- **Matching Conditions**: Define criteria based on **form names** or **form IDs**.
- **Page Restrictions**: Limit tracking to specific URLs or paths.
- **Conversion Criteria**: Define when a form is considered "converted" (e.g., successful submission).

## Specialized Reports
Form Analytics provides seven distinct reports:
- **Drop-off Report**: Identifies the last field a visitor interacted with before abandoning the form.
- **Entry Fields**: Shows which fields users interact with first.
- **Time and Hesitation**: Measures how much time users spend on each field and where they hesitate most.
- **Field Size**: Analyzes the amount of typing required for each field.
- **Usage Frequency**: Identifies the most and least used fields.
- **Most Corrected**: Highlights fields where visitors frequently encounter errors or change their input.
- **Blank Fields**: Lists fields that are often left empty and may be candidates for removal.

## Related pages
- [[index|Matomo Analytics Index]]
- [[session-recordings|Session Recordings]]
- [[goals-conversions|Goals & Conversions]]
