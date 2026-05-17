# Data Retention

**Summary**: This page explains how Matomo manages data retention for raw and report data, including configuration for deletion and anonymization.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2024-05-15

---

## Data Types in Matomo
Within Matomo, there are two primary types of data (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md):

- **Raw Data**: Individual visit information typically accessed through the **Visits Log**. It includes sources, user data, and all on-site activity. This data is also used for creating **new segment reports**.
- **Report Data**: Aggregated data compiled from raw data to create reports for specific metrics (e.g., visits from a specific country on a specific date). This is the primary data used for reviewing website trends over time.

## Retention Policies by Platform
Matomo allows different retention policies based on the hosting version (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md):

- **Matomo Cloud**: Offers unlimited **report data** retention, but **raw data** retention is limited based on the user's plan.
- **Matomo On-Premise / Matomo for WordPress**: Users can choose to keep both types of data indefinitely.

## Configuring Raw Data Retention
Raw data is inherently more personal and is often deleted more frequently than report data (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### Regular Deletion of Old Raw Data
1. Navigate to **Settings** > **Privacy** > **Anonymize data**.
2. Locate the **Regularly delete old raw data** section.
3. Enable **Regularly delete old raw data from the database**.
4. Set the **Delete logs older than (days)** value (e.g., 365 days for one year).
5. Click **Save**.

### Anonymization of Previously Tracked Raw Data
This is a one-off process to anonymize historical data (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md):
1. Login as **Super User**.
2. Navigate to **Administration** > **Privacy** > **Anonymize data**.
3. In the **Anonymize previously tracked raw data** section:
    - Select specific **websites** or **all websites**.
    - Define a **start date and end date** for the process.
    - Choose which columns to anonymize: **IP**, **UserID**, **Location**, **visits**, and **action columns**.
4. Note: Some values may be set to default rather than strictly anonymized, and the process can take a long time.

## Configuring Report Data Retention
Aggregated report data can be kept indefinitely, but may be removed to save server space (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### Deletion of Old Aggregated Report Data
1. Navigate to **Settings** > **Privacy** > **Anonymize data**.
2. Locate the **Delete old aggregated report data** section.
3. Enable **Regularly delete old reports from the database**.
4. Set the **Delete logs older than (months)** value.
5. Optional: Enable **Keep basic metrics** to retain numeric metrics without associated personal data labels.
6. Select specific reports to **Keep all data for**.
7. Click **Save**.

## Related pages
- [[privacy-overview]]
- [[gdpr-compliance]]
- [[index|Matomo Analytics Index]]
