# Dark Mode

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/dark-mode.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Respect system appearance and evaluate images, text, and surfaces in both light and dark contexts.
- Use adaptive semantic values so custom backgrounds do not undermine contrast or hierarchy.

## Source section outline

- Best practices
- Dark Mode colors
- Icons and images
- Text
- Platform considerations
- iOS, iPadOS
- macOS
- Resources
- Related
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-dark-mode-intro@2x.png)

<details>
<summary>All 43 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-dark-mode-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-dark-mode-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-stocks-app-dark-only-mode@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-system-colors-light@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-system-colors-dark@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-icon-in-light-mode@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-icon-in-dark-mode@2x.png)

![Apple image 8 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-illustration-in-light-mode@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-illustration-in-dark-mode-incorrect@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-illustration-in-dark-mode-correct@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-label-in-light-mode@2x.png)

![Apple image 12 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode-label-in-dark-mode@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/base-with-four-semantic-colors@2x.png)

![Apple image 14 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/elevated-with-four-semantic-colors@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/light-with-four-semantic-colors@2x.png)

![Apple image 16 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/48/174747D6-8723-4194-A932-7765179F1108/2949_wide_250x141_1x.jpg)

![Apple image 17 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/48/174747D6-8723-4194-A932-7765179F1108/2949_wide_250x141_2x.jpg)

![Apple image 18 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/48/174747D6-8723-4194-A932-7765179F1108/2949_wide_250x141_3x.jpg)

![Apple image 19 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/5CD0E251-424E-490F-89CF-1E64848209A6/9910_wide_250x141_1x.jpg)

![Apple image 20 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/5CD0E251-424E-490F-89CF-1E64848209A6/9910_wide_250x141_2x.jpg)

![Apple image 21 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/5CD0E251-424E-490F-89CF-1E64848209A6/9910_wide_250x141_3x.jpg)

![Apple image 22 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/accessibility.svg)

![Apple image 23 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/color.svg)

![Apple image 24 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode.svg)

![Apple image 25 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail@2x.png)

![Apple image 26 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail~dark@2x.png)

![Apple image 27 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-color-thumbnail@2x.png)

![Apple image 28 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-color-thumbnail~dark@2x.png)

![Apple image 29 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-dark-mode-thumbnail@2x.png)

![Apple image 30 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-dark-mode-thumbnail~dark@2x.png)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-materials-thumbnail@2x.png)

![Apple image 32 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-materials-thumbnail~dark@2x.png)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-typography-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-typography-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations~dark@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 40 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/materials.svg)

![Apple image 41 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 42 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

![Apple image 43 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography.svg)

</details>
