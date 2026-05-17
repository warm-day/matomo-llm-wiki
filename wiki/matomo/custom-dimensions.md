# Custom Dimensions

**Summary**: Custom dimensions allow for the collection of extra event parameters alongside standard Matomo tracking data, categorized into Visitor and Action types.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Dimension Types
There are two primary types of custom dimensions in Matomo:
- **Visitor type**: Typically retains a consistent value per session. These appear in **Visitor** reports (or the **User IDs** page if User ID is configured). (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Action type**: Dynamically changes based on user interaction, often multiple times per session. These appear in the **Behaviour** report. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

**Limits**: Sites can have **5-15 custom dimensions** per type. They can only be **deactivated**, not deleted. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## Implementation
Tracking requires the [CustomDimensions plugin](https://plugins.matomo.org/CustomDimensions) from the Matomo Marketplace.

### Configuration Options
1. **Regex Rules**: Set up triggers via **Administration > Custom dimensions** for specific Page URLs or Page Titles to automatically assign values.
2. **Manual JS Tracking**: Activate the dimension in the admin panel and push values from the website.

### JavaScript Tracking
It is imperative to push the pageview **after** custom definitions are set:

```jsx
_paq.push(['setCustomDimension', customDimensionId = 1, customDimensionValue = 'Member']);
_paq.push(['trackPageView']);
```

**Persistence**: Once set, the value persists for all subsequent tracking requests. To clear a value after a request:

```jsx
_paq.push(['deleteCustomDimension', customDimensionId]);
```

### Action-Specific Dimensions
To set a dimension for a single specific action (avoiding the need for manual deletion):

```jsx
_paq.push(['trackEvent', category, action, name, value, {dimension1: 'DimensionValue'}]);
_paq.push(['trackSiteSearch', keyword, category, resultsCount, {dimension1: 'DimensionValue'}]);
_paq.push(['trackLink', url, linkType, {dimension1: 'DimensionValue'}]);
_paq.push(['trackGoal', idGoal, customRevenue, {dimension1: 'DimensionValue'}]);
```

**Multiple Dimensions**: Multiple values can be set in a single call:

```jsx
_paq.push(['trackPageView', pageTitle, {dimension1: 'DimensionValue', dimension4: 'Test', dimension7: 'Value'}]);
```

## Related pages
- [[index|Matomo Analytics Index]]
- [[user-id|User ID]]
- [[event-tracking|Event Tracking]]
