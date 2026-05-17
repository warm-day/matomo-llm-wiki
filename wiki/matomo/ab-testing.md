# A/B Testing

**Summary**: Matomo's A/B testing framework allows for comparing different variations of pages, URLs, or code snippets to optimize conversion rates and user experience.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-23

---

## Prerequisites
- **Premium Feature**: Included in the **Cloud-hosted Business plan** or available as a purchase on the **Matomo Marketplace** for On-Premise installations (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Management
- **Access**: Experiments are managed via the **Experiments** menu item under the user icon (top right).
- **Permissions**: Requires at least **'Write'** or **'Admin'** access for the specific website (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Setup Workflow
1. **Creation**: Click **"Create new experiment"**. Basic information is required to start.
2. **Redirect Experiments**: If comparing different URLs, specify a **Redirect Page URL** for each variation.
    - **Requirement**: The Matomo Tracking code MUST be included on all pages, including the redirect target URLs (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
3. **Activation**: Click **"Embed code"** and add the snippet to the site. The experiment starts when the first user enters it.
4. **Completion**: Mark as finished via the report page or management section.
    - **Mandate**: Once finished, remove all experiment-related code from the website or app (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Implementation
The **A/B Testing plugin** adds the JavaScript framework directly to `matomo.js`.

### Writable Matomo.js Verification
To ensure A/B testing works by default, verify that `matomo.js` is writable:
1. Log in as a **Super User**.
2. Navigate to **Administration > System Check**.
3. Look for the **"Writable Matomo.js"** report. If a warning is displayed, follow the linked documentation to resolve it (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### Preventing Content Flickering
To prevent "flashing" of original content, `matomo.js` must be loaded **synchronously** in the `<head>`:
1. **Move** the tracking code into the HTML `<head>`.
2. **Remove** the asynchronous loading lines:
```javascript
var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
g.type='text/javascript';
g.async=true;
g.src=u+'matomo.js';
s.parentNode.insertBefore(g,s);
```
3. **Add** the synchronous script tag after the closing `</script>` of the initialization block:
```html
<script type="text/javascript" src="//$yourPiwikDomain/matomo.js"></script>
```

### Code Anatomy
Experiments should be initialized before the page view is tracked, in the `<head>`, and after the DOM is ready. **Do not use a Tag Manager for A/B testing code** (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

```javascript
var _paq = window._paq = window._paq || [];
_paq.push(['AbTesting::create', {
    name: 'ExperimentName',
    percentage: 100,
    startDateTime: '2017/08/25 00:00:00 UTC',
    endDateTime: '2020/05/21 23:59:59 UTC',
    trigger: function () {
        if (isLoggedIn && userAge < 50) {
            return true;
        }
        return false;
    },
    matomoTracker: Matomo.getAsyncTracker(matomoUrl, matomoSiteId),
    variations: [
        {
            name: 'blue',
            percentage: 40,
            activate: function(event) {
                document.getElementById('btn').style.color = '#0000ff';
            }
        },
        {
            name: 'red',
            activate: function(event) {
                document.getElementById('btn').style.color = '#ff0000';
            }
        }
    ]
}]);
```

### Configuration Parameters
- **percentage**: Overall visitor participation (default 100%).
- **trigger**: Function to restrict participation based on custom logic (e.g., country, user age).
- **variation.percentage**: Traffic allocation per variation. If unspecified, remaining traffic is shared equally (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **activate method**: Use `this.name` to access the variation name. The `event` object provides:
    - `event.experiment`: Access experiment instance.
    - `event.redirect(url)`: Redirect the user.
    - `event.onReady(callback)`: Execute code when DOM is ready.

## Testing & Maintenance
- **Force Variation**: Append `?pk_ab_test=$variationName` to the URL to test a specific variation.
- **Global Disable**: To stop all tests without removing code:
```javascript
_paq.push(['AbTesting::disable']);
```

## Single-Page Applications (SPA)
For SPAs, you must manually notify Matomo of URL/title changes and re-initialize the experiment:
```javascript
window.addEventListener('pathchange', function() {
    var _paq = window._paq = window._paq || [];
    _paq.push(['setCustomUrl', window.location.pathname]);
    _paq.push(['setDocumentTitle', document.title]);
    _paq.push(['AbTesting::create', {
        name: 'theExperimentName',
        includedTargets: [{"attribute":"url","type":"starts_with","value":"http:\/\/www.example.org","inverted":"0"}],
        excludedTargets: [],
        variations: [
            {
                name: 'original',
                activate: function (event) {}
            },
            {
                name: 'blue',
                activate: function(event) {
                    document.getElementById('btn').style.color = '#0000ff';
                }
            }
        ]
    }]);
    _paq.push(['trackPageView']);
});
```

## Related pages
- [[data-collection-basics|Data Collection Basics]]
- [[index|Matomo Index]]
