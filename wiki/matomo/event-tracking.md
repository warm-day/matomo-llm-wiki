# Event Tracking

**Summary**: Documentation on tracking user interactions in Matomo via manual JavaScript snippets or the Matomo Tag Manager.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-22

---

## Manual JavaScript Tracking
Events can be tracked by manually calling the `trackEvent()` function. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

### Event Components
- **Category (Required)**: Describes the type of event (e.g., "Link Clicks", "Videos").
- **Action (Required)**: The specific action taken (e.g., "Play", "Pause").
- **Name (Optional)**: Title of the element (e.g., video name).
- **Value (Optional)**: A numeric value (e.g., product cost).

### Implementation Example
```html
<a href="#" onclick="_paq.push(['trackEvent', 'Menu', 'Freedom']);">Freedom page</a>
```

## Tracking via Matomo Tag Manager (MTM)
Example: Tracking email link clicks.
1. **Create Tag**: In MTM, select **Matomo Analytics** tag type.
2. **Configure Event**:
   - **Tracking Type**: Event
   - **Event Category**: Contact
   - **Event Action**: Email Link Click
   - **Event Name**: `{{ClickDestinationUrl}}`
3. **Create Trigger**: Use **All links click**.
   - Set **Click Destination URL** starts with `mailto:`.
4. **Publish**: Save the tag and publish the container release.

## Reporting
Event reports are located under the **Behavior** section in the Matomo interface. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## Related pages
- [[data-collection-basics|Data Collection Basics]]
- [[tag-manager|Matomo Tag Manager]]
- [[goals-conversions|Goals and Conversions]]
- [[index|Matomo Analytics Index]]
