# User Roles

**Summary**: Definitions for View, Write, Admin, and Super User roles in Matomo, governing access to reports and configuration settings.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-15

---

## Role Definitions
Matomo uses a hierarchical permission system to control access to website data and administration tools (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

- **View**: Allows a user to see reports for a specific website.
- **Write**: Includes all **View** permissions, plus the ability to create, update, and delete website-specific features such as **Goals**, **Forms**, **Funnels**, **A/B tests**, **Heatmaps**, and **Session Recordings**.
- **Admin**: Includes all **Write** permissions, plus the ability to configure the website itself and manage user access for that specific website.
- **Super User**: The highest level of access. Can perform any action on any website, enable/disable plugins, and modify global system settings.

## Related pages
- [[multi-website-tracking|Multi-website Tracking]]
- [[index|Matomo Index]]
