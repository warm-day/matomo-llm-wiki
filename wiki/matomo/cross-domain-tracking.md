# Cross-domain Tracking

**Summary**: Configuration for tracking visitors across multiple domain names using Alias URLs and Roll-up Reporting to ensure visit continuity.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-15

---

## Setting up Cross Domain Linking
Cross-domain tracking ensures that visitors are accurately tracked across different domains within the same visit (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

### 1. Configure Alias URLs
- Navigate to **Administration** > **Websites** > **Manage**.
- Edit the website and specify all domain names in the **Alias URLs** field. At least two domains are required.

### 2. Enable in Tracking Code
- In the administration area, go to **Websites** > **Tracking Code**.
- Click **Advanced: Show** and check **Enable Cross Domain linking**. This also automatically hides clicks to known alias URLs in the "Outlinks" report.
- Verify the generated code contains these lines:

```jsx
_paq.push(["setDomains", ["*.domain1.com", "*.domain2.com"]]);
_paq.push(["enableCrossDomainLinking"]);
```

### 3. Verification and pk_vid Parameter
When Cross Domain linking is active, clicking a link from `domain1.com` to `domain2.com` will append a `pk_vid` parameter to the URL.
- **pk_vid**: Contains a string of data including the **Visitor ID** to maintain session continuity (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Roll-up Reporting
Roll-up Reporting aggregates reports from multiple websites into a single view.

### Limits and Availability
- **On-Premise**: Unlimited Roll-ups and source websites.
- **Cloud**: Unlimited Roll-ups, up to 30 source websites per Roll-up.

### Creation Steps
1. Click **All Websites** (top right).
2. Click **Add a new website** and select **Roll-Up**.
3. Name the Roll-up and select **Source measurables** from the dropdown. You can also search for a term to add all websites containing that term.
4. Configure currency and time zone, then **Save**.

## Related pages
- [[multi-website-tracking|Multi-website Tracking]]
- [[index|Matomo Index]]
