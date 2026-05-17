# SEO Web Vitals

**Summary**: A monitoring feature for On-Premise Matomo installations that tracks core performance metrics used by search engines to rank pages.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-23

---

## Prerequisites
- **On-Premise Only**: This feature is currently NOT available for Matomo Cloud (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **Subscription**: Requires the **SEO Web Vitals plugin** from the Matomo Marketplace.
- **Public Visibility**: Pages must be fully public, internet-connected, and crawlable.
- **SSL**: A valid SSL certificate must be enabled.
- **Traffic**: Pages must receive regular visitors; data is aggregated over a **28-day period** (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Core Metrics and Thresholds
Reports are found under **Acquisition > SEO Web Vitals**.

### Page Speed Score
- **Description**: An aggregate score indicating performance.
- **Thresholds**: 
    - **Good**: > 90
    - **Medium**: 50 to 90
    - **Slow**: < 50

### First Contentful Paint (FCP)
- **Description**: Time until the browser renders the first piece of content.
- **Good Threshold**: Up to **1.8 seconds**.

### Final Input Delay (FID)
- **Description**: Time between the first visitor interaction (e.g., clicking a link) and the browser's response. Note: This does not include scrolling.
- **Good Threshold**: Up to **100ms**.

### Last Contentful Paint (LCP)
- **Description**: Time at which the largest text or image element is rendered on the screen.
- **Good Threshold**: Up to **2.5 seconds**.

### Cumulative Layout Shift (CLS)
- **Description**: Measures visual stability by tracking how much elements move during loading.
- **Good Threshold**: Score of **0.1 or less** (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Related pages
- [[installation|Installation]]
- [[index|Matomo Index]]
