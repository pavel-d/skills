# Privacy

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/privacy.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Ask for the data needed for the current feature and explain the purpose where the request is made.
- Prefer system privacy protections and on-device processing when appropriate; make data use understandable.

## Source section outline

- Best practices
- Requesting permission
- Pre-alert screens, windows, or views
- Tracking requests
- Location button
- Protecting data
- Platform considerations
- macOS
- visionOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-privacy-intro@2x.png)

<details>
<summary>All 63 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-privacy-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-privacy-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-app-store-nutrition-labels@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-app-store-nutrition-labels~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-post-location-alert@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-post-location-alert~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-post-photo-alert@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-post-photo-alert~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-friends-contacts-alert@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-friends-contacts-alert~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-correct@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-correct~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-incorrect-cancel-button@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-incorrect-cancel-button~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-incorrect-close-button@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-incorrect-close-button~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-prohibited-incentive@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-prohibited-incentive~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-prohibited-imitation@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-prohibited-imitation~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-prohibited-alert@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-prohibited-alert~dark@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-prohibited-alert-annotation@2x.png)

![Apple image 26 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-custom-messaging-prohibited-alert-annotation~dark@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/location-button@2x.png)

![Apple image 28 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/location-button~dark@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-map-location-alert@2x.png)

![Apple image 30 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy-social-media-map-location-alert~dark@2x.png)

![Apple image 31 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/0A08BD06-2B59-45BA-AA75-C9206946195D/9945_wide_250x141_1x.jpg)

![Apple image 32 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/0A08BD06-2B59-45BA-AA75-C9206946195D/9945_wide_250x141_2x.jpg)

![Apple image 33 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/0A08BD06-2B59-45BA-AA75-C9206946195D/9945_wide_250x141_3x.jpg)

![Apple image 34 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/473C8E4A-1764-482D-BE24-B3A7BBDBD526/9996_wide_250x141_1x.jpg)

![Apple image 35 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/473C8E4A-1764-482D-BE24-B3A7BBDBD526/9996_wide_250x141_2x.jpg)

![Apple image 36 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/473C8E4A-1764-482D-BE24-B3A7BBDBD526/9996_wide_250x141_3x.jpg)

![Apple image 37 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/91B79F23-C28F-4E46-A066-887CB2AD6EE2/10943_wide_250x141_1x.jpg)

![Apple image 38 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/91B79F23-C28F-4E46-A066-887CB2AD6EE2/10943_wide_250x141_2x.jpg)

![Apple image 39 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/91B79F23-C28F-4E46-A066-887CB2AD6EE2/10943_wide_250x141_3x.jpg)

![Apple image 40 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.apptrackingtransparency/AppTrackingTransparency-PageImage-card@2x.png)

![Apple image 41 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.apptrackingtransparency/AppTrackingTransparency-PageImage-card~dark@2x.png)

![Apple image 42 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/data-entry.svg)

![Apple image 43 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/eyes.svg)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-privacy-thumbnail@2x.png)

![Apple image 45 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-privacy-thumbnail~dark@2x.png)

![Apple image 46 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations@2x.png)

![Apple image 47 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations~dark@2x.png)

![Apple image 48 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 49 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-eyes-thumbnail@2x.png)

![Apple image 50 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-eyes-thumbnail~dark@2x.png)

![Apple image 51 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/managing-accounts.svg)

![Apple image 52 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/onboarding.svg)

![Apple image 53 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 54 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-entering-data-thumbnail@2x.png)

![Apple image 55 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-entering-data-thumbnail~dark@2x.png)

![Apple image 56 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-managing-accounts-thumbnail@2x.png)

![Apple image 57 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-managing-accounts-thumbnail~dark@2x.png)

![Apple image 58 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-onboarding-thumbnail@2x.png)

![Apple image 59 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-onboarding-thumbnail~dark@2x.png)

![Apple image 60 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy.svg)

![Apple image 61 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sign-in-with-apple.svg)

![Apple image 62 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-sign-in-with-apple-thumbnail@2x.png)

![Apple image 63 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-sign-in-with-apple-thumbnail~dark@2x.png)

</details>
