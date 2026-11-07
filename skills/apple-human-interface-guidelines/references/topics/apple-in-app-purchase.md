# Apple In-App Purchase

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Integrate purchase choices into the product experience with clear names and complete billing information.
- Let people understand the value before committing and consult current purchase and subscription requirements.

## Source section outline

- Best practices
- Supporting Family Sharing
- Providing help
- Auto-renewable subscriptions
- Making signup effortless
- Supporting offer codes
- Helping people manage their subscriptions
- Platform considerations
- watchOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-IAP-intro@2x.png)

<details>
<summary>All 47 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-IAP-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-IAP-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/iap-intro@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/custom-purchase-help@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/custom-refund-request@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-refund-flow-1@2x.png)

![Apple image 7 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-refund-flow-1~dark@2x.png)

![Apple image 8 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-refund-flow-2@2x.png)

![Apple image 9 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-refund-flow-2~dark@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/iphone-onboarding@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/freemium-app@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/freemium-app~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/paywall-meter@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/paywall-meter~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/iphone-free-trial@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/iphone-upgrade@2x.png)

![Apple image 17 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/iphone-upgrade~dark@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-onboarding@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/iphone-custom-redeem@2x.png)

![Apple image 20 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/subscription-management@2x.png)

![Apple image 21 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/subscription-management~dark@2x.png)

![Apple image 22 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-provided-redemption-1@2x.png)

![Apple image 23 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-provided-redemption-1~dark@2x.png)

![Apple image 24 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-provided-redemption-3@2x.png)

![Apple image 25 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-provided-redemption-3~dark@2x.png)

![Apple image 26 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/clarify-description-before@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/clarify-description-after@2x.png)

![Apple image 28 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/lock-up-option-information@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/list-option-information@2x.png)

![Apple image 30 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/60AD843F-4A38-4D0D-A6EA-4B9C8F85495A/10720_wide_250x141_1x.jpg)

![Apple image 31 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/60AD843F-4A38-4D0D-A6EA-4B9C8F85495A/10720_wide_250x141_2x.jpg)

![Apple image 32 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/60AD843F-4A38-4D0D-A6EA-4B9C8F85495A/10720_wide_250x141_3x.jpg)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.advancedcommerceapi/advanced-commerce-PageImage-card@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.advancedcommerceapi/advanced-commerce-PageImage-card~dark@2x.png)

![Apple image 35 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-in-app-purchase.svg)

![Apple image 36 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay.svg)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 38 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/onboarding.svg)

![Apple image 39 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 40 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-onboarding-thumbnail@2x.png)

![Apple image 41 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-onboarding-thumbnail~dark@2x.png)

![Apple image 42 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-apple-pay-thumbnail@2x.png)

![Apple image 43 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-apple-pay-thumbnail~dark@2x.png)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-in-app-purchase-thumbnail@2x.png)

![Apple image 45 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-in-app-purchase-thumbnail~dark@2x.png)

![Apple image 46 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 47 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

</details>
