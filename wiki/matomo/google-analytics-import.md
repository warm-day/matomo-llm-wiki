# Google Analytics Import

**Summary**: Methods for importing historical and real-time data from Google Analytics (GA) into Matomo.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-15

---

## Fundamentals
When starting a GA import, Matomo automatically creates a **new website** for the imported data.
- **Restriction**: The import **cannot** go into an existing Matomo website, and data cannot be merged later (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Import Methods

### 1. Quick Connect
The fastest way to connect and import properties.
- Navigate to **Administration** > **System** > **Google Analytics Import**.
- Choose **Quick connect** and click **Connect with Google Analytics**.
- **Note**: You may receive a "Google hasn't verified this app" warning. You can safely continue by clicking **Advanced** and then **Go to matomo.cloud (unsafe)**.
- Select the GA properties to import. Matomo creates a new website for each selected property automatically.
- **Viewing Data**: Refresh the page and select the newly created Matomo website from the dropdown on the top left to see your data.

### 2. Advanced Google OAuth Client
Ideal for multiple websites or high-traffic sites.
- Provides faster migration and higher API limits.
- Requires manual configuration of a Google OAuth client.

### 3. Self-Hosted Plugin Method
For users running a self-hosted Matomo instance.
- **Requirement**: Use the latest version of Matomo and the **GoogleAnalyticsImporter** plugin.
- **Process**:
    1. Install the [Google Analytics Importer](https://plugins.matomo.org/GoogleAnalyticsImporter) plugin.
    2. Authorize Matomo to access GA data.
    3. Schedule the import job to run.
    4. Embed the Matomo tracking code for the newly created website into your site.
    5. **Verify Tracking**: Confirm that visits are being recorded in real-time within Matomo.
    6. **Cleanup**: Once historical data is migrated, set the **End Date** of the import job to the current date and remove the old Google Analytics code snippets from your website (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Related pages
- [[multi-website-tracking|Multi-website Tracking]]
- [[index|Matomo Index]]
