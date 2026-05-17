# Content Customization

**Summary**: Methods for customizing tracked page titles and URLs, and enhancing visit duration accuracy via the HeartBeatTimer.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Custom Page Titles
By default, Matomo uses the HTML `<title>`. This can be overridden using `setDocumentTitle`.

```jsx
_paq.push(['setDocumentTitle', document.title]);
_paq.push(['trackPageView']);
```

### Sub-domain Prefixing
To distinguish between sub-domains in a single website entity:
```jsx
_paq.push(['setDocumentTitle', document.domain + "/" + document.title]);
_paq.push(['trackPageView']);
```

## Custom URLs
To track a page under a different URL than the one in the browser address bar, use `setCustomUrl`.

```jsx
_paq.push(['setCustomUrl', 'https://yourdomain.com/your-new-page-url']);
_paq.push(['trackPageView']);
```

## HeartBeatTimer
To accurately measure time spent on a page (even if the user doesn't navigate to another page), enable the HeartBeatTimer.

```jsx
_paq.push(['enableHeartBeatTimer']);
```

**Triggers**: The heart beat request executes when:
- Switching browser tabs (after current tab was active for at least **15 seconds**).
- Navigating to another page within the same tab.
- Closing the tab.

## Related pages
- [[index|Matomo Analytics Index]]
- [[data-collection-basics|Data Collection Basics]]
