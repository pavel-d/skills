# Typography

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/typography) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/typography.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Use readable text styles and a clear hierarchy across supported display and viewing contexts.
- Verify weight, contrast, text scaling, and localization together instead of specifying font size alone.

## Source section outline

- Ensuring legibility
- Conveying hierarchy
- Using system fonts
- Using custom fonts
- Supporting Dynamic Type
- Platform considerations
- iOS, iPadOS
- macOS
- tvOS
- visionOS
- watchOS
- Specifications
- iOS, iPadOS Dynamic Type sizes
- xSmall
- Small
- Medium
- Large (default)
- xLarge
- xxLarge
- xxxLarge
- iOS, iPadOS larger accessibility type sizes
- AX1
- AX2
- AX3
- AX4
- AX5
- macOS built-in text styles
- tvOS built-in text styles
- watchOS Dynamic Type sizes
- Small (default 38mm)
- Large (default 40mm/41mm/42mm)
- xLarge (default 44mm/45mm/49mm)
- watchOS larger accessibility type sizes
- Tracking values
- iOS, iPadOS, visionOS tracking values
- SF Pro
- SF Pro Rounded
- New York
- macOS tracking values
- tvOS tracking values
- watchOS tracking values
- SF Compact
- SF Compact Rounded
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-typography-intro@2x.png)

<details>
<summary>All 42 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-typography-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-typography-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-typography-incorrect@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-typography-correct@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-sanfrancisco@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-sanfrancisco~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-new-york@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-new-york~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/font-weight-sf-pro@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/font-weight-sf-pro~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-text-hierarchy-levels@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-text-hierarchy-levels~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-default-type@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-default-type~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-dynamic-type@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography-dynamic-type~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-typography-2d-text-correct@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-typography-3d-text-incorrect@2x.png)

![Apple image 20 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 21 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/E4CD1309-352A-444E-96A5-FB5D6BA69725/9167_wide_250x141_1x.jpg)

![Apple image 22 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/E4CD1309-352A-444E-96A5-FB5D6BA69725/9167_wide_250x141_2x.jpg)

![Apple image 23 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/E4CD1309-352A-444E-96A5-FB5D6BA69725/9167_wide_250x141_3x.jpg)

![Apple image 24 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/49/EA12E035-968D-4B74-AC8D-26CFD8F365A7/3823_wide_250x141_1x.jpg)

![Apple image 25 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/49/EA12E035-968D-4B74-AC8D-26CFD8F365A7/3823_wide_250x141_2x.jpg)

![Apple image 26 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/49/EA12E035-968D-4B74-AC8D-26CFD8F365A7/3823_wide_250x141_3x.jpg)

![Apple image 27 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/124/F688D32F-15D2-4082-9505-DB2FA7FE0B0B/6736_wide_250x141_1x.jpg)

![Apple image 28 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/124/F688D32F-15D2-4082-9505-DB2FA7FE0B0B/6736_wide_250x141_2x.jpg)

![Apple image 29 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/124/F688D32F-15D2-4082-9505-DB2FA7FE0B0B/6736_wide_250x141_3x.jpg)

![Apple image 30 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/accessibility.svg)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail@2x.png)

![Apple image 32 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail~dark@2x.png)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-typography-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-typography-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations~dark@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 40 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 41 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

![Apple image 42 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography.svg)

</details>
