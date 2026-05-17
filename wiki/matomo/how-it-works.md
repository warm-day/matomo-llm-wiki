# How Matomo Works

**Summary**: This page explains the fundamental mechanisms of the Matomo Cloud service, covering installation, data collection, and processing.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## How Matomo Service Works (Cloud)
The Matomo Cloud version operates through a three-stage lifecycle: installation, data collection, and processing (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### 1. Installation
To begin tracking, the basic JavaScript tracking code must be installed on the website. This code initializes the tracking process and defines where data should be sent.

**Standard Tracking Code**:
```html
<!-- Matomo -->
<script type="text/javascript">
var _paq = window._paq = window._paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
var u="//{$MATOMO_URL}/";
_paq.push(['setTrackerUrl', u+'matomo.php']);
_paq.push(['setSiteId', {$IDSITE}]);
var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
g.type='text/javascript'; g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
})();
</script>
<!-- End Matomo Code -->
```
(source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

**Tracking Placeholders**:
- **{$MATOMO_URL}**: Replaced by your specific Matomo URL.
- **{$IDSITE}**: Replaced by the unique ID (idsite) of the website being tracked in Matomo.
(source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

### 2. Data Collection
Whenever a user interacts with the website (such as a page load), the tracking code initializes. A request containing data about the visitor's interaction is sent to Matomo's cloud server. By placing additional tracking codes for event tracking, user interactions other than pageviews can also be tracked (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### 3. Data Processing and Reporting
- **Database Queries**: Data is stored in a database where queries are run to populate the Matomo UI.
- **Visualization**: When a user accesses reports or refreshes pages in the Matomo UI, the system requests data from the database, runs the necessary queries, and returns visualised data to the interface.
(source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## How Matomo Service Works (Self-hosted)
The self-hosted version of Matomo allows users to run the service on their own infrastructure (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### 1. Installation
Self-hosted installation requires manual setup on the user's server:
- **Matomo Package**: A package for self-installation must be obtained from [Matomo.org](http://matomo.org/) and deployed to the website's server (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **Database**: Creation of a **MySQL** or similar database is required to host the analytics data (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **Tracking Code**: Installation of the **basic tracking code** on every page of the website (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### 2. Configuration
- **config.ini**: Configuration of the **config.ini** file on the website's server is required to point data to the database for hosting (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### 3. Data Collection
Whenever a user interacts with the website (pageload occurs), data is sent to a **self-hosted database** running Matomo’s configuration (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### 4. Data Processing and Reporting
- **Database Queries**: Queries are run in the database to populate the Matomo UI with visualised data (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **UI Interaction**: Interactions with the Matomo UI (viewing reports, refreshing pages, adjusting charts) trigger requests for data from the database (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **Visualization**: Visualised data is returned from the database and reflected in the Matomo UI (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Related pages
- [[index|Matomo Analytics Index]]
