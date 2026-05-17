# Campaign Tracking

**Summary**: Tracking marketing campaigns using URL parameters, supporting both standard and extended campaign metrics.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-03-05

---

## Campaign Parameters
### Default Parameters
Matomo tracks these by default:
- **mtm_campaign**: Name of the campaign.
- **mtm_keyword**: Specific keyword for the campaign.

### Extended Parameters
Requires the **Marketing Campaigns Reporting plugin**:
- **mtm_source**: Source where the user originated.
- **mtm_medium**: Marketing medium (e.g., email, cpc).
- **mtm_content**: Specific link or content type clicked.
- **mtm_cid**: Unique identifier for a specific ad.
- **mtm_group**: Audience type of the campaign.
- **mtm_placement**: Ad placement (e.g., newsfeed, home-banner).

## Third-Party Compatibility
The plugin also automatically detects standard **UTM parameters**:
- `utm_campaign`, `utm_source`, `utm_medium`, `utm_term`, `utm_content`, `utm_id`.

## Tools
- **URL Builder**: Matomo provides an official [URL builder tool](https://matomo.org/docs/tracking-campaigns-url-builder/) for generating tracked links.

## Related pages
- [[index|Matomo Analytics Index]]
- [[attribution-models|Attribution Models]]
