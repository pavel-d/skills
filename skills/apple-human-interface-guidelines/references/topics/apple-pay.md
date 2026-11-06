# Apple Pay

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/apple-pay) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/apple-pay.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Use approved payment controls and present Apple Pay appropriately when supported and available.
- Keep the action tied to payment or supported setup and verify branding and payment-sheet requirements.

## Source section outline

- Offering Apple Pay
- Streamlining checkout
- Customizing the payment sheet
- Displaying a website icon
- Handling problems
- Data validation errors
- Payment processing problems
- Supporting subscriptions
- Supporting donations
- Using Apple Pay buttons
- Button types
- Apple Pay button
- Set Up Apple Pay button
- Button styles
- Black
- White with outline
- White
- Button size and position
- Apple Pay mark
- Referring to Apple Pay
- Platform considerations
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Apple-Pay-intro@2x.png)

<details>
<summary>All 112 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Apple-Pay-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Apple-Pay-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-sheet@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-sheet~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/custom-button-yes@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/custom-button-yes~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 8 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/custom-button-no@2x.png)

![Apple image 9 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/custom-button-no~dark@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/payment-sheet-before-account@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/payment-sheet-before-account~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/payment-sheet-ios@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/payment-sheet-ios~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/payment-sheet-web@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/payment-sheet-web~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/web-icon-payment@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/web-icon-payment~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pay-sheet-error-ios@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/pay-sheet-error-ios~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pay-sheet-error-web@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/pay-sheet-error-web~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/detail-view-error-web@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/detail-view-error-web~dark@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/fixed-subscription-ios@2x.png)

![Apple image 26 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/fixed-subscription-ios~dark@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/variable-subscription-ios@2x.png)

![Apple image 28 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/variable-subscription-ios~dark@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/fixed-subscription-web@2x.png)

![Apple image 30 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/fixed-subscription-web~dark@2x.png)

![Apple image 31 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/no-payment-required-ios@2x.png)

![Apple image 32 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/no-payment-required-ios~dark@2x.png)

![Apple image 33 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/no-payment-required-web@2x.png)

![Apple image 34 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/no-payment-required-web~dark@2x.png)

![Apple image 35 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-card-on-button@2x.png)

![Apple image 36 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-card-on-button~dark@2x.png)

![Apple image 37 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-buy-with@2x.png)

![Apple image 38 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-buy-with~dark@2x.png)

![Apple image 39 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-pay-with@2x.png)

![Apple image 40 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-pay-with~dark@2x.png)

![Apple image 41 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-check-out-with@2x.png)

![Apple image 42 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-check-out-with~dark@2x.png)

![Apple image 43 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-continue-with@2x.png)

![Apple image 44 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-continue-with~dark@2x.png)

![Apple image 45 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-book-with@2x.png)

![Apple image 46 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-book-with~dark@2x.png)

![Apple image 47 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-donate-with@2x.png)

![Apple image 48 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-donate-with~dark@2x.png)

![Apple image 49 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-subscribe-with@2x.png)

![Apple image 50 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-subscribe-with~dark@2x.png)

![Apple image 51 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-reload-with@2x.png)

![Apple image 52 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-reload-with~dark@2x.png)

![Apple image 53 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-add-money-with@2x.png)

![Apple image 54 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-add-money-with~dark@2x.png)

![Apple image 55 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-top-up-with@2x.png)

![Apple image 56 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-top-up-with~dark@2x.png)

![Apple image 57 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-order-with@2x.png)

![Apple image 58 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-order-with~dark@2x.png)

![Apple image 59 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-rent-with@2x.png)

![Apple image 60 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-rent-with~dark@2x.png)

![Apple image 61 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-support-with@2x.png)

![Apple image 62 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-support-with~dark@2x.png)

![Apple image 63 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-contribute-with@2x.png)

![Apple image 64 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-contribute-with~dark@2x.png)

![Apple image 65 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-tip-with@2x.png)

![Apple image 66 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-tip-with~dark@2x.png)

![Apple image 67 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-button@2x.png)

![Apple image 68 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-button~dark@2x.png)

![Apple image 69 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-set-up@2x.png)

![Apple image 70 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-set-up~dark@2x.png)

![Apple image 71 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-black-yes@2x.png)

![Apple image 72 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-black-no@2x.png)

![Apple image 73 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-outline-yes@2x.png)

![Apple image 74 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-outline-no@2x.png)

![Apple image 75 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-white-yes@2x.png)

![Apple image 76 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-white-no@2x.png)

![Apple image 77 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-same-size-correct@2x.png)

![Apple image 78 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-same-size-correct~dark@2x.png)

![Apple image 79 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-smaller-incorrect@2x.png)

![Apple image 80 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-smaller-incorrect~dark@2x.png)

![Apple image 81 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-right-side-correct@2x.png)

![Apple image 82 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-right-side-correct~dark@2x.png)

![Apple image 83 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-left-side-incorrect@2x.png)

![Apple image 84 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-left-side-incorrect~dark@2x.png)

![Apple image 85 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-top-correct@2x.png)

![Apple image 86 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-top-correct~dark@2x.png)

![Apple image 87 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-below-incorrect@2x.png)

![Apple image 88 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/ap-below-incorrect~dark@2x.png)

![Apple image 89 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/minimum-corner-radii@2x.png)

![Apple image 90 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/minimum-corner-radii~dark@2x.png)

![Apple image 91 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/default-corner-radii@2x.png)

![Apple image 92 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/default-corner-radii~dark@2x.png)

![Apple image 93 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/maximum-corner-radii@2x.png)

![Apple image 94 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/maximum-corner-radii~dark@2x.png)

![Apple image 95 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/minimum-apple-pay@2x.png)

![Apple image 96 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/minimum-apple-pay~dark@2x.png)

![Apple image 97 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/minimum-apple-pay-donate@2x.png)

![Apple image 98 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/minimum-apple-pay-donate~dark@2x.png)

![Apple image 99 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay-mark-with-payment-options@2x.png)

![Apple image 100 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/FC715972-F367-4C86-A291-5C0358E5E230/9873_wide_250x141_1x.jpg)

![Apple image 101 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/FC715972-F367-4C86-A291-5C0358E5E230/9873_wide_250x141_2x.jpg)

![Apple image 102 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/FC715972-F367-4C86-A291-5C0358E5E230/9873_wide_250x141_3x.jpg)

![Apple image 103 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-in-app-purchase.svg)

![Apple image 104 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pay.svg)

![Apple image 105 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 106 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 107 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-apple-pay-thumbnail@2x.png)

![Apple image 108 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-apple-pay-thumbnail~dark@2x.png)

![Apple image 109 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-in-app-purchase-thumbnail@2x.png)

![Apple image 110 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-in-app-purchase-thumbnail~dark@2x.png)

![Apple image 111 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 112 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

</details>
