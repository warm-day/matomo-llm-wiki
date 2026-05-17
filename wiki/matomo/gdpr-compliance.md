# GDPR Compliance

**Summary**: Details on how Matomo enables data subjects to exercise their rights under GDPR, including data access, erasure, and objection tools.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2026-05-13

---

## Right to be Informed
- **Privacy Notice**: Users must be informed at the point of data collection with a clear privacy notice.
- **Minimum Requirements**: Notice must include reasons for processing, data retention duration, parties data is shared with, and a link to a completed [privacy policy page](https://matomo.org/privacy-policy/) (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Right of Access & Data Portability
- **Identity Verification**: Before providing access, the data subject's identity must be verified (e.g., matching email addresses).
- **Anonymization Note**: If personal data is anonymized, searching for a specific data subject is no longer possible as it is no longer personal data (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **GDPR Tools**: Accessible via **Administration → Privacy → GDPR tools**.
- **Exporting Data**: Use the **'EXPORT SELECTED VISITS'** button to download a file containing the data subject's visits (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Right to Erasure & Rectification
- **Procedure**: Navigate to **Administration (wheel icon) → Privacy → GDPR tools**.
- **Deletion**: After searching for and selecting a data subject, click **'DELETE SELECTED VISITS'** (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **Rectification**: For rectification requests, Matomo recommends using the right to erasure procedure instead (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Right to Object (Opt-out)
- **Opt-out iFrame**: Matomo provides an iFrame for users to object to tracking, typically placed on the privacy policy page.
- **Implementation**:
    - Navigate to **Administration → Privacy → Users Opt-out**.
    - Tweak the HTML code customization parameters (see below).
    - Copy/Paste the code into your website (e.g., the privacy policy page).
    - **Verification**: Test the implementation to ensure it is working correctly (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **Customization Parameters**:
    - **backgroundColor**: Hexadecimal color string (e.g., 'ffffff', 'ddd').
    - **fontColor**: Hexadecimal color string (e.g., 'ffffff', 'ddd').
    - **fontSize**: Valid CSS font size (e.g., '1.2em', '15pt', '15px', '50%').
    - **fontFamily**: String containing only letters, spaces, or hyphens (e.g., 'Lucida', 'Courier new').
    - **language**: Two-letter language code (e.g., 'en', 'de').
- **Third-Party Solutions**: 3rd party opt-out solutions can also be used (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Right to Withdraw Consent
- **Withdrawal Mechanism**: Users must be able to perform a specific action to remove consent, such as clicking a button labeled "I do not want to be tracked anymore."
- **Matomo Consent Feature**: 
    - Configuration is available in **Administration → Privacy → Asking for consent**.
    - For implementation details, refer to the [Matomo Tracking Consent Guide](https://developer.matomo.org/guides/tracking-consent) (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).
- **Third-Party Solutions**: 3rd party consent management solutions are supported (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md).

## Related pages
- [[privacy-overview]]
- [[index|Matomo Analytics Index]]
