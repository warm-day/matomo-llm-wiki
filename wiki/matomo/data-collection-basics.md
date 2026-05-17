# Data Collection Basics

**Summary**: Definitions of fundamental tracking metrics and a list of data points captured by the standard Matomo tracking code.

**Sources**: [[../../raw/Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md]]

**Last updated**: 2025-05-22

---

## Basic Definitions
- **Visit**: A 30-minute time-out based period of user activity. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Unique Visitors**: The total count of unique IDs. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **New Visitor**: A unique visitor coming to the website for the first time. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Returning Visitor**: A visitor identified by ID who visits subsequently. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Hit**: A recorded request in Matomo. It can be a page view, event tracking, download, outlink, onsite search, or content tracking request. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Entry Page**: Also known as the Landing Page; the first pageview in a visit. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Entrances**: The count of visits that started on a particular page. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Exit Page**: The last page accessed during a visit. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)
- **Exit Rate**: The ratio of exits on a page to the visits on that page. (source: Matomo Analytics DB 74e2f6cb8f0549379ec3cbe6c6a1a066.md)

## Basic Tracking Data
When the basic tracking code is installed, the following data is captured with each pageview event:
- **User IP** and **User Agent** (used to detect browser, OS, device type, brand, and model).
- **Date & time** of the request.
- **Page Title** and **Page URL**.
- **Referrer URL**.
- **Screen resolution**.
- **File downloads** and **Outbound link clicks**.
- **Page speed**.
- **User Location**: Country, region, city, longitude, and latitude.
- **Main Language**.
- **1st Party Cookie Info**: Random unique visitor ID, time of the first visit, time of the previous visit, and number of visits.

## Related pages
- [[tag-manager|Matomo Tag Manager]]
- [[event-tracking|Event Tracking]]
- [[index|Matomo Analytics Index]]
