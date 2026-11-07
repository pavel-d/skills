# Virtual keyboards

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Choose an input layout appropriate to the value being entered.
- Verify keyboard presentation and editing behavior without assuming a specific hardware or software keyboard is present.

## Source section outline

- Best practices
- Custom input views
- Custom keyboards
- Platform considerations
- iOS, iPadOS
- tvOS
- visionOS
- watchOS
- Resources
- Related
- Developer documentation
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/components-virtual-keyboard-intro@2x.png)

<details>
<summary>All 55 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-virtual-keyboard-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-virtual-keyboard-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-ascii-capable@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-ascii-capable~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-ascii-capable-number-pad@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-ascii-capable-number-pad~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-decimal-pad@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-decimal-pad~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-default@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-default~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-email-address@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-email-address~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-name-phone-pad@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-name-phone-pad~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-number-pad@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-number-pad~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-numbers-and-punctuation@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-numbers-and-punctuation~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-phone-pad@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-phone-pad~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-twitter@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-twitter~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-url@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-url~dark@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-web-search@2x.png)

![Apple image 26 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/virtual-keyboard-web-search~dark@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ui-fully-visible@2x.png)

![Apple image 28 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/ui-fully-visible~dark@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 30 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/text-field-hidden@2x.png)

![Apple image 31 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/text-field-hidden~dark@2x.png)

![Apple image 32 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 33 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-hidden@2x.png)

![Apple image 34 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-hidden~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-digit-entry-views-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-digit-entry-views-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-selection-and-input-thumbnail@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-selection-and-input-thumbnail~dark@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-virtual-keyboards-thumbnail@2x.png)

![Apple image 40 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-virtual-keyboards-thumbnail~dark@2x.png)

![Apple image 41 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components@2x.png)

![Apple image 42 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components~dark@2x.png)

![Apple image 43 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/data-entry.svg)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-layout-thumbnail@2x.png)

![Apple image 45 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-layout-thumbnail~dark@2x.png)

![Apple image 46 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 47 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-keyboards-thumbnail@2x.png)

![Apple image 48 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-keyboards-thumbnail~dark@2x.png)

![Apple image 49 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/keyboards.svg)

![Apple image 50 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/layout.svg)

![Apple image 51 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 52 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-entering-data-thumbnail@2x.png)

![Apple image 53 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-entering-data-thumbnail~dark@2x.png)

![Apple image 54 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/selection-and-input.svg)

![Apple image 55 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-virtual-keyboard.png)

</details>
