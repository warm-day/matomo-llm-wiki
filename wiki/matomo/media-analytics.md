# Media Analytics

**Summary**: Automatic tracking of video and audio interactions, providing detailed metrics on how media is consumed.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Requirements
Media tracking is automatically integrated into the standard Matomo JavaScript tracker (`matomo.js`).

**Critical Requirement**: The `matomo.js` file in your Matomo directory **must be writable** by the webserver/PHP for automatic tracking to function. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

### Verification
1. Login to Matomo as a Super User.
2. Navigate to **Administration > System Check**.
3. Verify that the "Writable Matomo.js" check passes. If it fails, follow the [troubleshooting guide](https://developer.matomo.org/guides/media-analytics/setup#when-the-matomojs-in-your-piwik-directory-file-is-not-writable).

## Reporting
Reports are located under the **Media** section in the main navigation.
- **Overview**: High-level media metrics and evolution over time.
- **Real-time**: Live monitoring of current media interactions.
- **Video & Audio Reports**: Detailed metrics on consumption patterns.
- **Audience Log & Map**: Insights into audience location and behavior before/after media consumption.

## Related pages
- [[index|Matomo Analytics Index]]
- [[data-collection-basics|Data Collection Basics]]
- [[event-tracking|Event Tracking]]
