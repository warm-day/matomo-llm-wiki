# Ecommerce Reports

**Summary**: Overview of the specialized ecommerce reporting capabilities in Matomo, including the Ecommerce Overview dashboard, granular logs, and multidimensional sales breakdowns.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-22

---

## Ecommerce Overview Page
The main dashboard for ecommerce performance, featuring visualization tools for key metrics.

### Chart 1: Evolution Graph
- **Time Series**: Displays data in increments of **Day**, **Week**, **Month**, or **Year**. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Metric Selection**: Users can toggle the following metrics on the chart:
  - **Ecommerce Orders**
  - **Conversion Rate**
  - **Total Revenue**
  - **Purchased Products**
  - **Average Order Value**
- **Interactivity**: Data can be **exported** or **annotated**.

### Chart 2: Sparkline Summary Cards
Provides a quick glance at key performance indicators. Clicking a card updates the Evolution Graph above. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Ecommerce Orders**
- **Total Revenue**
- **Average Order Value**
- **Ecommerce Orders conversion rate**
- **Purchased Products**
- **Visits with Abandoned Cart**
- **Revenue left in cart**

---

## Specialized Ecommerce Reports

### Cart Abandonments
Overview of visits where items were added to the cart but no purchase was completed. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

### Orders Overview
A detailed breakdown of sales performance, including:
- **Revenue**
- **Subtotals**
- **Tax**
- **Shipping**
- **Discounts**

### E-commerce Log
Provides **granular session-level data**, allowing for inspection of individual customer journeys and transactions. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

### Sales Tables
Performance metrics (sales and conversion rates) can be aggregated by:
- **Product Name**
- **Product SKU**
- **Product Category**

---

## Multidimensional Breakdowns
Ecommerce performance can be analyzed across various dimensions:
- **Referrers**: Sales by channels, search engines, and keywords. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Sales Engagement**: Analysis of days and visits required for conversion.
- **User Location**: Breakdown by country, continent, and region.
- **Devices**: Analysis by device type, model, and brand.
- **Custom Dimensions**: Performance across user-defined tracking dimensions.

## Related pages
- [[ecommerce-tracking|Ecommerce Tracking]]
- [[goals-conversions|Goals and Conversions]]
- [[index|Matomo Analytics Index]]
