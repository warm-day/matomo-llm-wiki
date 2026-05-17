# User ID

**Summary**: The [User ID](https://matomo.org/docs/user-id/) feature connects data from multiple devices and browsers to a single unique identifier for logged-in users.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Implementation Steps
1. **Assign Identifier**: Assign a unique, persistent, non-empty string (e.g., email or username) to each logged-in user.
2. **Persistence**: Set the User ID for **every pageload and pageview** to ensure continuous tracking.
3. **Tracking Call**: Use the `setUserId` method before any tracking functions (`trackPageView`, `trackEvent`, etc.).

### JavaScript Implementation
```jsx
_paq.push(['setUserId', 'USER_ID_HERE']);
_paq.push(['trackPageView']);
```

### Logout Handling
When a user logs out, notify Matomo and optionally force a new visit:

```jsx
// User has just logged out
_paq.push(['resetUserId']);

// Force a new visit for subsequent pageviews
_paq.push(['appendToTrackingUrl', 'new_visit=1']);
_paq.push(['trackPageView']);

// Reset tracking URL (important for SPAs)
_paq.push(['appendToTrackingUrl', '']);
```

## Tag Manager Configuration
1. Create a variable (e.g., `UserID`) that captures the unique identifier.
2. Update the **Matomo Configuration** variable.
3. In the **User ID** field, input `{{UserID}}`.
4. Preview and publish the container.

## Reporting
- **User IDs Report**: Located in **Visitors > User IDs**.
- **Engagement Metrics**: Hover over the table and click the **table icon** to select **Display a table with Visitor engagement metrics**.
- **Visitor Profile**: Hover over a User ID row and click the green icons to access granular data for that specific user.

## Related pages
- [[index|Matomo Analytics Index]]
- [[custom-dimensions|Custom Dimensions]]
- [[tag-manager|Tag Manager]]
