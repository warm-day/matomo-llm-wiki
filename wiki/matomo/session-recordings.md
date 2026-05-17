# Session Recordings

**Summary**: Recording and replaying user sessions to visualize interactions, scroll behavior, and clicks on the website.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Configuration
Session recordings are managed via **Administration > Session Recordings > Manage Session Recordings**.

### Targeting and Filters
When creating a new recording, you can define specific criteria:
- **Target Pages**: Filter by **URL**, **URL path**, or **URL parameter** using comparisons like "equals", "starts with", "contains", or "matches the regular expression".
- **Active Users**: Optionally record only users who actively scroll or click.
- **Min. Session Time**: Only record sessions that last at least a specified duration.
- **Capture Keystrokes**: Option to disable recording of text entered into form fields for privacy.
- **Limits**: Define the total **Number of sessions** to record and the **Sample Rate**.

## Reporting
Reports are accessible via the **Session Recordings** menu in the main navigation.
- **Replay**: Hover over a session row to access the replay action.
- **Visitor Information**: View session initialization time, duration, viewport resolution, location, and device information.
- **Visitor Profile**: Integration with the [Visitor Profile](https://matomo.org/docs/user-profile/) to see a user's broader history.

## Related pages
- [[index|Matomo Analytics Index]]
- [[user-id|User ID]]
- [[forms-tracking|Forms Tracking]]
