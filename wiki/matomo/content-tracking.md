# Content Tracking

**Summary**: Tracking impressions and interactions with specific content elements such as banners, ads, or call-to-action blocks.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Implementation
Matomo tracks when specific HTML elements are viewed or clicked.

### HTML Markup
Add the `data-track-content` attribute to the HTML element you wish to track. Additional attributes for advanced markup can be found in the [official documentation](https://matomo.org/faq/how-to/how-do-i-markup-content-for-content-tracking/).

```html
<div data-track-content>
    <!-- Content to track (e.g., a banner) -->
</div>
```

### Visibility Tracking
To track impressions only when the content is actually visible on the screen, use the following JavaScript calls:

```jsx
_paq.push(['trackPageView']);
_paq.push(['trackVisibleContentImpressions']);
```

> **Note**: Documentation regarding specific content click tracking is currently limited and may be subject to future updates. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## Related pages
- [[index|Matomo Analytics Index]]
- [[event-tracking|Event Tracking]]
