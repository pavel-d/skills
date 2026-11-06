# CareKit

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/carekit) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/carekit.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Explain health-data use clearly and request access when the related care feature needs it.
- Keep system privacy controls authoritative rather than creating a competing permission model.

## Source section outline

- Data and privacy
- HealthKit integration
- Motion data
- Photos
- ResearchKit integration
- CareKit views
- Tasks
- Charts
- Contact views
- Notifications
- Symbols and branding
- Platform considerations
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-CareKit-intro@2x.png)

<details>
<summary>All 58 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-CareKit-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-CareKit-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-tasks-and-charts@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-tasks-and-charts~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-contacts@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-contacts~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-view-components@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-view-components~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-simple-task@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-simple-task~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-instructions-task@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-instructions-task~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-log-task@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-log-task~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-checklist-task@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-checklist-task~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-grid-task@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-grid-task~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-bar-chart@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-bar-chart~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-scatter-chart@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-scatter-chart~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-line-chart@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-line-chart~dark@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-simple-contact@2x.png)

![Apple image 26 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-simple-contact~dark@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-detailed-contact@2x.png)

![Apple image 28 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit-detailed-contact~dark@2x.png)

![Apple image 29 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/49/196C46B0-DF68-4947-B211-4FEECE415A6E/3408_wide_250x141_1x.jpg)

![Apple image 30 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/49/196C46B0-DF68-4947-B211-4FEECE415A6E/3408_wide_250x141_2x.jpg)

![Apple image 31 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/49/196C46B0-DF68-4947-B211-4FEECE415A6E/3408_wide_250x141_3x.jpg)

![Apple image 32 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/119/EAFF830B-8468-49BA-A5DC-D3A3E8B7F463/4960_wide_250x141_1x.jpg)

![Apple image 33 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/119/EAFF830B-8468-49BA-A5DC-D3A3E8B7F463/4960_wide_250x141_2x.jpg)

![Apple image 34 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/119/EAFF830B-8468-49BA-A5DC-D3A3E8B7F463/4960_wide_250x141_3x.jpg)

![Apple image 35 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/accessibility.svg)

![Apple image 36 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/carekit.svg)

![Apple image 37 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/color.svg)

![Apple image 38 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-notifications-thumbnail@2x.png)

![Apple image 39 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-notifications-thumbnail~dark@2x.png)

![Apple image 40 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail@2x.png)

![Apple image 41 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail~dark@2x.png)

![Apple image 42 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-color-thumbnail@2x.png)

![Apple image 43 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-color-thumbnail~dark@2x.png)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 45 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 46 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/healthkit.svg)

![Apple image 47 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 48 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 49 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/researchkit.svg)

![Apple image 50 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

![Apple image 51 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-carekit-thumbnail@2x.png)

![Apple image 52 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-carekit-thumbnail~dark@2x.png)

![Apple image 53 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-healthkit-thumbnail@2x.png)

![Apple image 54 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-healthkit-thumbnail~dark@2x.png)

![Apple image 55 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-researchkit-thumbnail@2x.png)

![Apple image 56 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-researchkit-thumbnail~dark@2x.png)

![Apple image 57 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 58 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

</details>
