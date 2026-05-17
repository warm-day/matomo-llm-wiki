# Matomo Tag Manager (MTM)

**Summary**: A guide to Matomo Tag Manager (MTM) covering installation, configuration, and comparison with Google Tag Manager (GTM).

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-22

---

## MTM vs GTM Comparison
- **Environments**: MTM uses **Dev**, **Staging**, and **Live** environments instead of GTM's "Live" and "Latest". (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Workspaces**: MTM does not feature workspaces.
- **Hosting**: MTM is hosted on your website, reducing the risk of scripts being blocked compared to external solutions.
- **Privacy**: No privacy disadvantage compared to direct tracking if only used for Matomo Analytics tags; other marketing tags may require user consent.

## Installation and Setup
- **Automatic Configuration**: MTM pre-configures a container for new sites automatically.
- **Activation**: Navigate to **Tag Manager** in the top menu or **Administration > Plugins** in the UI.
- **Embed Code**: Found in the **Install code** menu. Options include **dev**, **stage**, and **live**, which provide slightly different snippets.
- **Placement**: Copy and paste the snippet as high as possible on the website.
- **GTM Interoperability**: To prevent MTM from using GTM's `dataLayer` values, check the box in the **Edit container** screen (**Tag Manager > Manage Containers > Edit Container**).

## Usage Components
- **Tags**: Consist of Tag Type (e.g., Matomo Analytics, Facebook pixel), Triggers (when to execute), and Advanced Settings (execution frequency, date ranges).
- **dataLayer**: MTM supports GTM's `dataLayer`. To use a custom one, add the following before the container tag:
  ```html
  <script>
  var _mtm = _mtm || [];
  _mtm.push({'weather': 'sunny'});
  </script>
  ```
- **Multiple Environments**:
  1. Create each site (Dev, Staging, Production) as a separate **Measurable** in Matomo.
  2. Create a **Lookup Table** variable mapping hostnames/URLs to their respective Site IDs.
  3. Update the **Matomo Configuration** variable to use this Lookup Table (e.g., `{{SiteID}}`).
  4. Deploy the specific environment tracking code to its corresponding website.

## Debug Mode and Publishing
- **Preview/Debug**: Click **Preview / Debug** in the MTM interface and enter the URL.
- **Manual Debug**: If the console doesn't appear, append `?mtmPreviewMode=YourContainerID&mtmSetDebugFlag=1` to the URL. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Versions**: Snapshots of container configurations that allow for easy recovery and feedback.
- **Publishing**: Click **Publish** in the left menu, provide a version name, and click **Create New Version And Publish Release**.

## Migration from GTM
1. Create a container and environments in MTM.
2. Manually recreate GTM **Variables**, **Triggers**, and **Tags** in MTM.
3. Replace the GTM snippet with the MTM install code in the website header.
4. Preview, debug, and publish the new version.

## Related pages
- [[data-collection-basics|Data Collection Basics]]
- [[event-tracking|Event Tracking]]
- [[index|Matomo Analytics Index]]
