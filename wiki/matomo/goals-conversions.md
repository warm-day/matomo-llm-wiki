# Goals and Conversions

**Summary**: Instructions for creating and managing goals in Matomo, and tracking conversions using manual JavaScript calls.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-22

---

## Goal Configuration
Goals are managed in the **Goals** section of the Matomo interface. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
1. Navigate to **Goals > Manage Goals**.
2. Click **Add A New Goal**.
3. Configure details in the **Update Goal** view.
4. **Options**: You can track multiple goals per visit or set up conversion funnels.

## Manual Goal Tracking
You can trigger a goal conversion manually using the `trackGoal` function.
```javascript
// Logs a conversion for goal ID 1
_paq.push(['trackGoal', 1]);

// Logs a conversion for goal ID 1 with custom revenue (e.g., dynamic value from cart)
_paq.push(['trackGoal', 1, <?php echo $cart->getCartValue(); ?>]);
```

## Goal Reporting
The **Goals** report provides several views:
- **Time-series graph**: Displays conversion count and eCR (ecommerce conversion rate).
- **Summary cards**: Total conversions, eCR, and revenue for the period.
- **Goal breakdown**: Data broken down by individual goals.
- **Dimension breakdowns**:
  - **Referrers**: Channel, search engine, keyword, website, campaign.
  - **Engagement**: Location (country, city, etc.), device type, model, and brand.

## Related pages
- [[event-tracking|Event Tracking]]
- [[ecommerce-tracking|E-commerce Tracking]]
- [[index|Matomo Analytics Index]]
