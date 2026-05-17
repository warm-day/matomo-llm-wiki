# E-commerce Tracking

**Summary**: A comprehensive guide to enabling and implementing E-commerce tracking in Matomo, including platform-specific modules and manual JavaScript triggers.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-22

---

## Setup Overview
E-commerce tracking requires a two-phase setup: enabling the feature in the Matomo interface and then implementing tracking on the e-commerce platform. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

### Enabling E-commerce in Matomo
- **For New Sites**: During site creation, scroll to **Ecommerce settings**, enable it, and set the currency.
- **For Existing Sites**:
  1. Go to **Settings > Measurables/Websites**.
  2. Edit the target website.
  3. Select **Ecommerce enabled** in the dropdown and choose the **Currency**.

## Magento 2 (M2) Implementation
Matomo offers a dedicated module for Magento 2. Configuration is managed in the M2 backend under **Jajuma > Matomo analytics > Configuration**.

### Configuration Tabs
- **General**: Configure the endpoint (URL + SiteID) and tracker access token for server-side tracking.
- **Dashboard**: Set the date range and access token to view Matomo data within M2.
  - *Dashboard Access*: Accessible via **Dashboard > Matomo > Matomo Dashboard**. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Privacy**: Configure respect for "Do Not Track" requests.
- **JS Tracking**: Configure pageviews, cross-subdomain tracking, heartbeat, and proxy settings.
  - *Note*: Tracker name changes in production require running `bin/magento s:d:` and clearing the cache.
- **E-commerce**: Enable JS or PHP (server-side) trackers. Choose between pushing all orders or only completed ones, and set push delays.
- **Matomo Tag Manager**: Enable and enter the container ID. Import the provided JSON file into the Matomo MTM container via the **Versions > Import** button.

## JavaScript-Based Triggers
If not using a module, manual JS triggers can be used to send data.

### Category View (PLP)
```javascript
_paq.push(['setEcommerceView',
  false,    // Product name (N/A for category)
  false,    // Product SKU (N/A for category)
  "Books"   // Category or array of up to 5 categories
]);
_paq.push(['trackPageView']);
```

### Product View (PDP)
```javascript
_paq.push(['setEcommerceView',
  "0123456789",               // (Required) productSKU
  "Ecommerce Analytics Book",  // (Optional) productName
  "Books",                    // (Optional) categoryName
  9.99                        // (Optional) price
]);
_paq.push(['trackPageView']);
```

### Cart Updates
To track additions or removals, send the details of **every item remaining in the cart**.
```javascript
_paq.push(['addEcommerceItem',
  "0123456789",               // (Required) productSKU
  "Ecommerce Analytics Book",  // (Optional) productName
  ["Books", "Best sellers"],   // (Optional) productCategory
  9.99,                       // (Recommended) price
  1                           // (Optional) quantity
]);
_paq.push(['trackEcommerceCartUpdate', 15.5]); // Total cart value
```

### Order Tracking
Typically triggered on the order confirmation page.
1. **Add Items**: Use `addEcommerceItem` for each product in the order.
2. **Track Order**: Send the order summary.
```javascript
_paq.push(['trackEcommerceOrder',
  "000123", // (Required) orderId
  10.99,    // (Required) grandTotal (including tax/shipping)
  9.99,     // (Optional) subTotal (excluding shipping)
  1.5,      // (Optional) tax
  1,        // (Optional) shipping
  false     // (Optional) discount (numeric value or false)
]);
```

## E-commerce Metrics
- **Ecommerce Orders**: Total order count.
- **Products Purchased**: Number of items sold.
- **Total Revenue**: Sum of order values.
- **Subtotals**: The order subtotal, excluding shipping and tax.
- **Tax** and **Shipping** costs.
- **Discounts**: Value of discounts applied.
- **Average Order Value (AOV)**.
- **Ecommerce Orders Conversion Rate**.
- **Abandoned Carts**: Total count and potential revenue of visits where products were added but not purchased.
- **Revenue per visit**.

## Related pages
- [[data-collection-basics|Data Collection Basics]]
- [[goals-conversions|Goals and Conversions]]
- [[index|Matomo Analytics Index]]
