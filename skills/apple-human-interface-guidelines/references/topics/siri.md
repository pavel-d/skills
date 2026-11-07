# Siri

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/siri) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/siri.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Expose useful common tasks using the vocabulary people associate with the app.
- Offer relevant results and actions rather than using assistant interactions for promotion.

## Source section outline

- Getting your app to work with Siri
- Sharing contextual information
- Best practices
- Customizing your app’s experience with Siri
- Editorial guidelines
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Siri-intro@2x.png)

<details>
<summary>All 34 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Siri-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Siri-intro~dark@2x.png)

![Apple image 3 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/0C71E74E-4A72-4B59-A24D-778CA7A70B82/10891_wide_250x141_1x.jpg)

![Apple image 4 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/0C71E74E-4A72-4B59-A24D-778CA7A70B82/10891_wide_250x141_2x.jpg)

![Apple image 5 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/0C71E74E-4A72-4B59-A24D-778CA7A70B82/10891_wide_250x141_3x.jpg)

![Apple image 6 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/A23B9856-2ECA-4591-84FA-0E595455AB25/10893_wide_250x141_1x.jpg)

![Apple image 7 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/A23B9856-2ECA-4591-84FA-0E595455AB25/10893_wide_250x141_2x.jpg)

![Apple image 8 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/A23B9856-2ECA-4591-84FA-0E595455AB25/10893_wide_250x141_3x.jpg)

![Apple image 9 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/CAF3A339-4121-4E23-93E9-2CD25F0E3A69/10763_wide_250x141_1x.jpg)

![Apple image 10 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/CAF3A339-4121-4E23-93E9-2CD25F0E3A69/10763_wide_250x141_2x.jpg)

![Apple image 11 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/CAF3A339-4121-4E23-93E9-2CD25F0E3A69/10763_wide_250x141_3x.jpg)

![Apple image 12 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/Making-on-screen-content-available-to-Siri-and-Apple-Intelligence-PageImage-card@2x.png)

![Apple image 13 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/Making-on-screen-content-available-to-Siri-and-Apple-Intelligence-PageImage-card~dark@2x.png)

![Apple image 14 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/app-intents-PageImage-card@2x.png)

![Apple image 15 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/app-intents-PageImage-card~dark@2x.png)

![Apple image 16 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-thumbnail@2x.png)

![Apple image 17 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-thumbnail~dark@2x.png)

![Apple image 18 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-snippets-thumbnail@2x.png)

![Apple image 19 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-snippets-thumbnail~dark@2x.png)

![Apple image 20 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/displaying-static-and-interactive-snippets-PageImage-card@2x.png)

![Apple image 21 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/displaying-static-and-interactive-snippets-PageImage-card~dark@2x.png)

![Apple image 22 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-inclusion-thumbnail@2x.png)

![Apple image 23 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-inclusion-thumbnail~dark@2x.png)

![Apple image 24 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-writing-thumbnail@2x.png)

![Apple image 25 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-writing-thumbnail~dark@2x.png)

![Apple image 26 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 27 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inclusion.svg)

![Apple image 28 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 29 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/siri.svg)

![Apple image 30 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-siri-thumbnail@2x.png)

![Apple image 31 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-siri-thumbnail~dark@2x.png)

![Apple image 32 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 33 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

![Apple image 34 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/writing.svg)

</details>
