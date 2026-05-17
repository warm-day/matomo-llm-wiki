# Cookieless Tracking

**Summary**: Procedures for configuring Matomo to track visitors without using cookies, enabling data collection without a consent banner under specific conditions.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2026-05-13

---

## Disabling Cookies
Matomo can be configured to disable cookies globally, per website, or via the Tag Manager (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### 1. Global Configuration (All Websites)
To prevent cookies from being used across all websites in a Matomo instance:
- **Requirement**: Must be logged in as a **Super User**.
- **Action**: Navigate to **Administration > Privacy > Anonymize data**.
- **Setting**: Enable the checkbox **"Force tracking without cookies"**.
- **Impact**: 
    - Automatically updates the JavaScript tracker to ensure all trackers do not use cookies.
    - Matomo server-side will ignore any received tracking cookies.
    - Cookies will remain disabled even if consent methods (e.g., `_paq.push(['rememberConsentGiven']);`) are called.

### 2. Per Website Configuration
To disable cookies for a specific website using the JavaScript tracking code:
- **Requirement**: Locate the Matomo tracking code in your site's editor.
- **Action**: Add `_paq.push(['disableCookies']);` before the `trackPageView` call.
- **Code Example**:
    ```javascript
    [...]
    // Call disableCookies before calling trackPageView
    _paq.push(['disableCookies']);
    _paq.push(['trackPageView']);
    [...]
    ```

### 3. Matomo Tag Manager (MTM) Configuration
If using MTM without a separate cookie consent solution:
- **Variable Setting**: In your **Matomo Configuration** variable, ensure the **Disable Cookies** checkbox is enabled.
- **Tag Setting**: When creating a Matomo Tag, assign it to use this configuration variable.

---

## Using Matomo Without a Consent Banner
You can safely use Matomo without a consent mechanism (cookie banner) if the collected data is minimized and not shared (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### Technical Checklist
1. **Disable Cookies**: (See steps above).
2. **Anonymize IP Address**: Ensure IP anonymization is active.
3. **Anonymize Referrer**: Prevent tracking of full referrer URLs.
4. **Exclude Personal Data**:
    - Scrub personal data from **URLs** and **Page Titles**.
    - Avoid personal data in **Custom Variables**, **Dimensions**, and **Events**.
5. **Mask Personal Data**: Apply masking in **Heatmaps** and **Session Recordings**.
6. **Anonymize Ecommerce Order IDs**:
    - Go to **Privacy > Anonymize data**.
    - Enable **Anonymize Order ID**.
    - Click **Save**.
7. **Disable User ID**: Do not use the User ID feature.
8. **Support Do Not Track (DNT)**:
    - Go to **Administration > Privacy > Users opt-out**.
    - Scroll to **Support Do Not Track preference**.
    - Click **Enable Do Not Track support (Recommended)**.
    - Click **Save**.

### Procedural Checklist
- **Single Site Tracking**: Only track users on a single site; do not track across different domains.
- Opt-Out Mechanism: Include the Matomo Opt-out form in your Privacy Policy.
- Privacy Policy & Terms: Update your policy to mention Matomo and how data is handled. You can also [add Privacy Policy and Terms & Conditions links directly in Matomo](https://matomo.org/faq/how-do-i-display-links-to-my-privacy-policy-and-or-terms-conditions-to-people-who-view-matomo-reports/).
- Analytics Only: Only use the collected data for analytics purposes.

---

## Consent-based Transition
This advanced setup allows Matomo to start in cookieless mode and transition to cookie-based tracking once a user provides consent (Example using **Cookiebot**) (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### Implementation Script
Add this code to the header of each page, beneath the Cookiebot code:

```javascript
<script>
var waitForTrackerCount = 0;

function matomoWaitForTracker() {
  if (typeof _paq === 'undefined' || typeof Cookiebot === 'undefined') {
    if (waitForTrackerCount < 40) {
      setTimeout(matomoWaitForTracker, 250);
      waitForTrackerCount++;
      return;
    }
  } else {
    window.addEventListener('CookiebotOnAccept', function (e) {
      consentSet();
    });
    window.addEventListener('CookiebotOnDecline', function (e) {
      consentSet();
    })
  }
}

function consentSet() {
  if (Cookiebot.consent.statistics) {
    _paq.push(['setCookieConsentGiven']);
    _paq.push(['setConsentGiven']);
  } else {
    _paq.push(['forgetCookieConsentGiven']);
    _paq.push(['forgetConsentGiven']);
  }
}

document.addEventListener('DOMContentLoaded', matomoWaitForTracker());
</script>
```
**Note**: Matomo will only transition to cookie-based tracking if the user provides **‘Statistics’** consent via Cookiebot.

## Related pages
- [[privacy-overview]]
- [[consent-management]]
- [[gdpr-compliance]]
- [[index|Matomo Analytics Index]]
