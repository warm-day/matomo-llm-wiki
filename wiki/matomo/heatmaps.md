# Heatmaps and Session Recordings

**Summary**: Matomo captures user interactions such as clicks, mouse movements, and scrolls, allowing for visual analysis of visitor behavior via heatmaps and video-like session replays.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-23

---

## Creation and Management
To begin recording, a Heatmap must first be created in the Matomo interface.

- **Access**: Navigate to the **"Heatmaps"** menu in either reporting or administration and select **"Manage"**.
- **Setup**: Click **"Create new heatmap"** (bottom left). To modify existing ones, use the edit icon next to the heatmap name (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **Targeting**: Choose the target page using attributes:
    - **URL**
    - **URL path**
    - **URL parameter**
- **Matching Rules**: Comparisons include **"equals"**, **"starts with"**, **"contains"**, or **"matches the regular expression"**.

## Interaction Tracking
Matomo records the following user actions:
- **Clicks**: Tracking where users click on the page.
- **Mouse Movements**: Captures the path of the cursor.
- **Scrolls**: Shows how far down a page visitors typically venture.
- **Form Interactions**: Tracks how users engage with input fields.
- **Page Changes**: Captures dynamic content shifts.

## Heatmap Report Types
Once data is collected, several visualization types are available:
- **Click map**: Aggregated view of click density.
- **Mouse move**: Visualization of cursor paths and hovering behavior.
- **Scroll map**: Vertical distribution of user attention.
- **Above the fold**: Analysis of what content is visible without scrolling (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Related pages
- [[session-recordings|Session Recordings]]
- [[forms-tracking|Forms Tracking]]
- [[index|Matomo Index]]
