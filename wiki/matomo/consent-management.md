# Consent Management

**Summary**: Matomo provides two levels of consent to balance user privacy with data accuracy: Cookie Consent and Tracking Consent.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2026-05-13

---

## Types of Consent
Matomo offers two distinct forms of consent to manage how visitor data is collected (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md):

1. **Cookie Consent**: Prevents tracking cookies from being set until consent is gained. Data is still collected but with reduced accuracy for certain reports ([source FAQ 156](https://matomo.org/faq/general/faq_156/)).
2. **Tracking Consent**: No data is tracked at all until the user explicitly consents. This provides the highest privacy but results in missing data.

### 1. Cookie Consent
This mode is used when personal data is not being tracked. Matomo will track visitors without using cookies if consent is not provided (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md). Cookies will only be used if consent for **Statistics** cookies was given in a consent manager like Cookiebot.

- **Requirement**: Use `_paq.push(['requireCookieConsent']);`.
- **Impact of Disabled Cookies**:
    - **Visitor Recognition**: Matomo uses IP addresses and footprints to identify unique visitors, which is less accurate than cookie-based IDs.
    - **Attribution**: Goals and Ecommerce conversions are attributed only to the channel used in the visit that converts.
    - **Missing Reports**: Multi-Attribution and Cohort reports will not show data.
    - **Inaccurate Reports**: The following reports count all visits without cookies as if they were new visitors:
        - Days since last visit
        - Visits by visit count
        - Visits to Conversion
        - Days to Conversion

#### Setup Guide (Cookie Consent)
1. Go to *Administration > Measurables > Tracking Code* and ensure the correct website is selected.
2. **Copy the tracking code from your Matomo dashboard** and paste it into a text editor.
3. Add the line `_paq.push(['requireCookieConsent']);` just before the first line starting with `_paq.push`.
4. Add this updated code to all pages on your website directly before the `</head>` tag, replacing any existing Matomo tracking code (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

```javascript
<!-- Matomo -->
<script>
  var _paq = window._paq = window._paq || [];
  _paq.push(['requireCookieConsent']); // Added before other _paq.push calls
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//matomo/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '1']);
  })();
</script>
<script src="//matomo/matomo.js"></script>
<!-- End Matomo Code -->
```

#### Matomo Tag Manager (MTM) Setup
- **Custom HTML Tag**: Create a tag containing `_paq.push(['requireCookieConsent']);`.
- **Trigger**: Create a trigger on **DOM Ready**.
- **Execution Order**: The DOM Ready trigger **must be executed first before the Pageview trigger**.
- **Tag Assignment**: In your Custom HTML tag, set "Execute this tag when any of these triggers are triggered" to "DOM Ready".

### 2. Tracking Consent
This mode must be used if personal data (e.g., user identifiers, eCommerce orders) is being tracked. If consent for **Statistics** cookies is not given, Matomo will not perform any tracking at all (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

- **Requirement**: Use `_paq.push(['requireConsent']);`.

#### Setup Guide (Tracking Consent)
1. Go to *Administration > Measurables > Tracking Code* and ensure the correct website is selected.
2. **Copy the tracking code from your Matomo dashboard** and paste it into a text editor.
3. Add the line `_paq.push(['requireConsent']);` just before the first line starting with `_paq.push`.
4. Add this updated code to all pages on your website directly before the `</head>` tag, replacing any existing Matomo tracking code (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

```javascript
<!-- Matomo -->
<script>
  var _paq = window._paq = window._paq || [];
  _paq.push(['requireConsent']); // Added before other _paq.push calls
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//matomo/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '1']);
  })();
</script>
<script src="//matomo/matomo.js"></script>
<!-- End Matomo Code -->
```

## Functional and Security Cookies
Even if tracking is disabled, some cookies may still be placed for functional or security reasons (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md):

- **piwik_ignore**: Created when a user excludes themselves from being tracked via the cookie method or iframe opt-out. It is set on the domain of your Matomo server.
- **MATOMO_SESSID**: A temporary short-lived cookie providing a [cryptographic nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce) to prevent CSRF security issues while users opt-out of tracking.
- **mtm_consent** and **mtm_consent_removed**: Created when asking for tracking consent.
- **_pk_testcookie**: Used only to check if the visitor's browser supports cookies; it contains no identifier and is deleted shortly after creation.

## Related pages
- [[privacy-overview]]
- [[cookieless-tracking]]
- [[gdpr-compliance]]
- [[tag-manager]]
- [[index|Matomo Analytics Index]]
