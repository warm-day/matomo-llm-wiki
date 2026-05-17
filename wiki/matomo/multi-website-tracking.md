# Multi-website Tracking

**Summary**: Instructions for adding new websites and tracking multiple subdomains or subdirectories within Matomo.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-15

---

## Adding a New Website
To add a website, you must be logged into Matomo as a **Super User** (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

1. Navigate to **Administration** > **Websites/Measurable** > **Manage**.
2. Click **Add a new website**.
3. Fill out the website form with relevant options.

Note: For **Cross-domain tracking**, websites should be added as **Alias URLs** rather than separate entries (see [[cross-domain-tracking]]).

## Standard Tracking (Single Domain)
The standard use case tracks a single domain name (with no subdomains) or a specific subdomain in a single Matomo website (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

```jsx
_paq.push(['setSiteId', 1]);
_paq.push(['setTrackerUrl', u+'matomo.php']);
_paq.push(['trackPageView']);
```

## Tracking One Domain and its Subdomains
To record users across a main domain and all its subdomains, cookies must be shared using `setCookieDomain`. This call must be included in the tracking code on every related page (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

```jsx
_paq.push(['setSiteId', 1]);
_paq.push(['setTrackerUrl', u+'matomo.php']);

// Share the tracking cookie across example.com and all of its subdomains
_paq.push(['setCookieDomain', '*.example.com']);

// Tell Matomo the website domain so that clicks on these domains are not tracked as 'Outlinks'
_paq.push(['setDomains', '*.example.com']);

_paq.push(['trackPageView']);
```

## Tracking Subdirectories as Separate Websites
You can track specific subdirectories (e.g., `/user/MyUsername`) as independent Matomo websites. This requires customizing `setSiteId`, `setCookiePath`, and `setDomains` (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### Configuration Requirements:
- **Homepage (Site ID X)**: Use default tracking code. In **Administration** > **Websites**, the URL for Site ID X should be set to `example.com/`.
- **Subdirectory (Site ID Y)**: In **Administration** > **Websites**, the URL for Site ID Y should be set to the specific path (e.g., `example.com/user/MyUsername`).

### Tracking Code for a Subdirectory Page:
```jsx
// Use the specific Site ID (Y) for this subdirectory
_paq.push(['setSiteId', Y]);

// Create the tracking cookie specifically in the subdirectory
_paq.push(['setCookiePath', '/user/MyUsername']);

// Clicks to other subdirectories (e.g., /user/AnotherUsername) will be tracked as 'Outlinks'
_paq.push(['setDomains', 'example.com/user/MyUsername']);

_paq.push(['setTrackerUrl', u+'matomo.php']);
_paq.push(['trackPageView']);
```

### Technical Rationale for setCookiePath
When tracking many subdirectories in separate websites, using **setCookiePath** prevents **cookie bloating**. This ensures:
- **Accuracy**: Prevents the browser from deleting cookies due to volume limits.
- **Performance**: Reduces the amount of cookie data sent with each request.

## Related pages
- [[user-roles|User Roles]]
- [[cross-domain-tracking|Cross-domain Tracking]]
- [[index|Matomo Index]]
