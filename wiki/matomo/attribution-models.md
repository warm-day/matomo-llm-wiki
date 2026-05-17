# Attribution Models

**Summary**: Matomo's attribution models define how credit for conversions is distributed across various marketing interactions.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Default Model
The default attribution model in Matomo is **Last non-Direct**. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## Multi-Channel Attribution Extension
The **Multi-channel attribution** extension (purchased separately) provides six additional models:

- **Last Interaction**: The most common model; tracks how people reached the site in the session where they converted.
- **Last Non-direct**: Similar to Last Interaction but ignores direct visits (which often come from bookmarks), focusing on the last meaningful marketing source.
- **First Interaction**: Credits the very first interaction that led the user to the website, even if subsequent visits occurred.
- **Linear**: Splits conversion credit evenly across all interactions in the conversion path.
- **Position Based**: Allocates **40%** of the credit to both the first and last interactions, and splits the remaining **20%** among all interactions in between.
- **Time Decay**: Credit is distributed based on how recently the interaction occurred before the sale, with the most recent interactions receiving the most credit.

## Related pages
- [[index|Matomo Analytics Index]]
- [[campaign-tracking|Campaign Tracking]]
- [[goals-conversions|Goals & Conversions]]
