# Search fields

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/search-fields.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Explain searchable content or scope and offer timely results or suggestions.
- Keep results easy to interpret and avoid making people infer the field's purpose from placement alone.

## Source section outline

- Best practices
- Scope bars and tokens
- Platform considerations
- iOS
- Search as a tab
- Search in a toolbar
- Search as an inline field
- iPadOS, macOS
- tvOS
- watchOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/components-search-field-intro@2x.png)

<details>
<summary>All 44 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-search-field-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-search-field-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-scope-control-tokens@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-scope-control-tokens~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-search-as-tab-standard@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-search-as-tab-standard~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-search-as-tab-prominent@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-search-as-tab-prominent~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-ios-toolbar-with-items@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-ios-toolbar-with-items~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-ios-navigation-bar-item@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-ios-navigation-bar-item~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-toolbar-search-ipad@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-toolbar-search-ipad~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-toolbar-search-mac@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-toolbar-search-mac~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-ipad-search-in-sidebar@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-ipad-search-in-sidebar~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-ipad-search-in-tab-bar@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-ipad-search-in-tab-bar~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/search-fields-tvos-search@2x.png)

![Apple image 22 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/1AAA030E-2ECA-47D8-AE09-6D7B72A840F6/10044_wide_250x141_1x.jpg)

![Apple image 23 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/1AAA030E-2ECA-47D8-AE09-6D7B72A840F6/10044_wide_250x141_2x.jpg)

![Apple image 24 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/1AAA030E-2ECA-47D8-AE09-6D7B72A840F6/10044_wide_250x141_3x.jpg)

![Apple image 25 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/5614F523-C21B-4ADC-AF14-0417BC34EA15/10836_wide_250x141_1x.jpg)

![Apple image 26 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/5614F523-C21B-4ADC-AF14-0417BC34EA15/10836_wide_250x141_2x.jpg)

![Apple image 27 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/5614F523-C21B-4ADC-AF14-0417BC34EA15/10836_wide_250x141_3x.jpg)

![Apple image 28 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/119/BE8FF113-0FE1-40FC-86BF-FE95BE2FF7A5/5027_wide_250x141_1x.jpg)

![Apple image 29 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/119/BE8FF113-0FE1-40FC-86BF-FE95BE2FF7A5/5027_wide_250x141_2x.jpg)

![Apple image 30 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/119/BE8FF113-0FE1-40FC-86BF-FE95BE2FF7A5/5027_wide_250x141_3x.jpg)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-navigation-and-search-thumbnail@2x.png)

![Apple image 32 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-navigation-and-search-thumbnail~dark@2x.png)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-search-fields-thumbnail@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-search-fields-thumbnail~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-token-fields-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-token-fields-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components~dark@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 40 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/navigation-and-search.svg)

![Apple image 41 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 42 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-searching-thumbnail@2x.png)

![Apple image 43 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-searching-thumbnail~dark@2x.png)

![Apple image 44 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/searching.svg)

</details>
