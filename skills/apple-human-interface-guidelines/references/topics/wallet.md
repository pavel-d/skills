# Wallet

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/wallet) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/wallet.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Offer an understandable way to add relevant passes and group related passes when appropriate.
- Use the prescribed Wallet controls and avoid presenting an add action for a pass already present.

## Source section outline

- Passes
- Pass anatomy
- Pass field types
- Designing passes
- Pass styles
- Boarding passes
- Coupons
- Event tickets
- Store cards
- Poster generic passes
- Generic passes
- Pass images
- Logo
- Primary logo
- Secondary logo
- Icon
- Strip image
- Thumbnail
- Background
- Footer
- Order tracking
- Displaying order and fulfillment details
- Identity verification
- Platform considerations
- watchOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Wallet-intro@2x.png)

<details>
<summary>All 103 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Wallet-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Wallet-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-hero@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-add-to-apple-wallet@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-pass-notification@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-pass-notification~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-pass-live-activity@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-pass-live-activity~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-wallet-app@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-wallet-app~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-pass-pass-designer-overview@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-pass-pass-designer-overview~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-text-sufficient-contrast@2x.png)

![Apple image 14 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-text-insufficient-contrast@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-background-sufficient-contrast@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-background-insufficient-contrast@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-types-airline-boarding@2x.png)

![Apple image 20 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-types-coupon@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-types-poster-event-ticket@2x.png)

![Apple image 22 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-types-event-ticket-background@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-types-event-ticket@2x.png)

![Apple image 24 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-types-store-card@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-types-generic-poster-pass@2x.png)

![Apple image 26 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-types-generic-pass@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-logo@2x.png)

![Apple image 28 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-logo~dark@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-logo-no-shadow@2x.png)

![Apple image 30 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-logo-with-shadow-incorrect@2x.png)

![Apple image 31 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-primary-logo-square@2x.png)

![Apple image 32 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-primary-logo-square~dark@2x.png)

![Apple image 33 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-primary-logo-wide@2x.png)

![Apple image 34 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-primary-logo-wide~dark@2x.png)

![Apple image 35 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-secondary-logo@2x.png)

![Apple image 36 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-secondary-logo~dark@2x.png)

![Apple image 37 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-icon-notification@2x.png)

![Apple image 38 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-icon-notification~dark@2x.png)

![Apple image 39 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-icon-wallet@2x.png)

![Apple image 40 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-icon-wallet~dark@2x.png)

![Apple image 41 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-strip-image@2x.png)

![Apple image 42 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-strip-image~dark@2x.png)

![Apple image 43 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-thumbnail@2x.png)

![Apple image 44 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-thumbnail~dark@2x.png)

![Apple image 45 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-background-unblurred@2x.png)

![Apple image 46 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-background-layout-qr-code@2x.png)

![Apple image 47 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-background-layout-qr-code-safe-areas@2x.png)

![Apple image 48 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-background-layout-barcode@2x.png)

![Apple image 49 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-passes-images-background-layout-barcode-safe-areas@2x.png)

![Apple image 50 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-status-order-placed@2x.png)

![Apple image 51 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-status-order-placed~dark@2x.png)

![Apple image 52 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-status-delivered@2x.png)

![Apple image 53 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-status-delivered~dark@2x.png)

![Apple image 54 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-dashboard@2x.png)

![Apple image 55 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-dashboard~dark@2x.png)

![Apple image 56 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-status-on-the-way-fields@2x.png)

![Apple image 57 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-status-on-the-way-fields~dark@2x.png)

![Apple image 58 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-product-images@2x.png)

![Apple image 59 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-product-images~dark@2x.png)

![Apple image 60 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-contacts@2x.png)

![Apple image 61 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-contacts~dark@2x.png)

![Apple image 62 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-status-pickup-details@2x.png)

![Apple image 63 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-ot-status-pickup-details~dark@2x.png)

![Apple image 64 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-button-verify-age@2x.png)

![Apple image 65 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-button-verify-age~dark@2x.png)

![Apple image 66 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-button-verify-identity@2x.png)

![Apple image 67 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-button-verify-identity~dark@2x.png)

![Apple image 68 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-button-continue-with@2x.png)

![Apple image 69 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-button-continue-with~dark@2x.png)

![Apple image 70 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-button-verify-with@2x.png)

![Apple image 71 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet-button-verify-with~dark@2x.png)

![Apple image 72 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-card-and-details@2x.png)

![Apple image 73 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-pass-design-intro@2x.png)

![Apple image 74 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-diagram@2x.png)

![Apple image 75 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-diagram~dark@2x.png)

![Apple image 76 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-boarding-pass@2x.png)

![Apple image 77 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-boarding-pass~dark@2x.png)

![Apple image 78 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-coupon@2x.png)

![Apple image 79 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-coupon~dark@2x.png)

![Apple image 80 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-store-card@2x.png)

![Apple image 81 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-store-card~dark@2x.png)

![Apple image 82 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-event-ticket@2x.png)

![Apple image 83 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-event-ticket~dark@2x.png)

![Apple image 84 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-generic-pass@2x.png)

![Apple image 85 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/watch-layout-generic-pass~dark@2x.png)

![Apple image 86 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/5FACC310-770C-4BD9-8696-9E837324C325/10719_wide_250x141_1x.jpg)

![Apple image 87 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/5FACC310-770C-4BD9-8696-9E837324C325/10719_wide_250x141_2x.jpg)

![Apple image 88 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/5FACC310-770C-4BD9-8696-9E837324C325/10719_wide_250x141_3x.jpg)

![Apple image 89 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.financekit/FinanceKit-PageImage-card@2x.png)

![Apple image 90 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.financekit/FinanceKit-PageImage-card~dark@2x.png)

![Apple image 91 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay.svg)

![Apple image 92 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 93 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/id-verifier.svg)

![Apple image 94 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 95 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-apple-pay-thumbnail@2x.png)

![Apple image 96 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-apple-pay-thumbnail~dark@2x.png)

![Apple image 97 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-id-verifier-apps-thumbnail@2x.png)

![Apple image 98 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-id-verifier-apps-thumbnail~dark@2x.png)

![Apple image 99 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-wallet-thumbnail@2x.png)

![Apple image 100 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-wallet-thumbnail~dark@2x.png)

![Apple image 101 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 102 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

![Apple image 103 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/wallet.svg)

</details>
