# Tap to Pay on iPhone

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Complete merchant setup and required administrative acceptance before a customer payment interaction.
- Provide practical instruction for supported payment types and device readiness.

## Source section outline

- Enabling Tap to Pay on iPhone
- Educating merchants
- Checking out
- Displaying results
- Additional interactions
- Platform considerations
- Resources
- Related
- Developer documentation
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-TapToPay-intro@2x.png)

<details>
<summary>All 48 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-TapToPay-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-TapToPay-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-introduction-screen@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-introduction-screen~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-confirmation-screen@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-confirmation-screen~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-merchant-settings-tutorials@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-merchant-settings-tutorials~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-merchant-education-contactless-cards@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-merchant-education-contactless-cards~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-processing-screen-determinate-progress@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-processing-screen-determinate-progress~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-processing-screen-indeterminate-progress@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-processing-screen-indeterminate-progress~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-on-iphone-symbol-correct@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-on-iphone-symbol-correct~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-on-iphone-logo-incorrect@2x.png)

![Apple image 19 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-on-iphone-logo-incorrect~dark@2x.png)

![Apple image 20 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-authorizing-payment@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-authorizing-payment~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-confirmed-payment@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-confirmed-payment~dark@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-unconfirmed-payment@2x.png)

![Apple image 26 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-unconfirmed-payment~dark@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-unsuccessful-transaction@2x.png)

![Apple image 28 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-unsuccessful-transaction~dark@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/loyalty-card@2x.png)

![Apple image 30 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/loyalty-card~dark@2x.png)

![Apple image 31 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-on-iphone-loyalty@2x.png)

![Apple image 32 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-on-iphone-loyalty~dark@2x.png)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.ProximityReader/adding-support-for-tap-to-pay-PageImage-card@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.ProximityReader/adding-support-for-tap-to-pay-PageImage-card~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-alerts-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-alerts-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-progress-indicators-thumbnail@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-progress-indicators-thumbnail~dark@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 40 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 41 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 42 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 43 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

![Apple image 44 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tap-to-pay-on-iphone.svg)

![Apple image 45 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-tap-to-pay-on-iphone-thumbnail@2x.png)

![Apple image 46 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-tap-to-pay-on-iphone-thumbnail~dark@2x.png)

![Apple image 47 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 48 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

</details>
