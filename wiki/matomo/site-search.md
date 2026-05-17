# Site Search

**Summary**: Tracking and reporting for internal website search queries, including keywords, categories, and result counts.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Configuration
### Automatic Tracking
Matomo can automatically parse URL parameters for search keywords.
1. Navigate to **Administration > Websites > Manage** (or **Measurables > Manage**).
2. Edit the website and enable **Site Search tracking**.

### Manual Tracking
Use the `trackSiteSearch` function to record keywords manually.

```jsx
_paq.push(['trackSiteSearch',
    "Banana",        // Required: Search keyword
    "Organic Food",  // Optional: Search category (set to false if unused)
    0                // Optional: Number of results (0 indicates 'No Results')
]);
```

**Implementation Note**: On search result pages, call `trackSiteSearch` **instead** of `trackPageView`. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## Reporting
- **Visitors > Overview**: Displays total Site Searches alongside other primary metrics.
- **Behaviour > Site Search**: Detailed reports including **Top Internal Searches**.
- **Pages Following a Site Search**: Shows which pages are most frequently visited after a search.

## Related pages
- [[index|Matomo Analytics Index]]
- [[data-collection-basics|Data Collection Basics]]
- [[custom-dimensions|Custom Dimensions]]
