# App Shortcuts

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Expose common high-value tasks in language and options people can understand.
- Check current app-schema guidance and provide appropriate clarification when a request needs more information.

## Source section outline

- Best practices
- Responding to App Shortcuts
- Editorial guidelines
- Platform considerations
- iOS, iPadOS
- macOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-intro@2x.png)

<details>
<summary>All 39 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/app-intents-parameter-diagram@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/app-intents-parameter-diagram~dark@2x.png)

![Apple image 5 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/05A21C8D-2A52-47BF-85A6-EB13E720EC85/9971_wide_250x141_1x.jpg)

![Apple image 6 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/05A21C8D-2A52-47BF-85A6-EB13E720EC85/9971_wide_250x141_2x.jpg)

![Apple image 7 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/05A21C8D-2A52-47BF-85A6-EB13E720EC85/9971_wide_250x141_3x.jpg)

![Apple image 8 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/4D88FD13-E491-4499-AA3F-8A84CF4BA607/9999_wide_250x141_1x.jpg)

![Apple image 9 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/4D88FD13-E491-4499-AA3F-8A84CF4BA607/9999_wide_250x141_2x.jpg)

![Apple image 10 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/4D88FD13-E491-4499-AA3F-8A84CF4BA607/9999_wide_250x141_3x.jpg)

![Apple image 11 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/9C184A72-5AD1-4D1C-9981-75A932050980/10856_wide_250x141_1x.jpg)

![Apple image 12 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/9C184A72-5AD1-4D1C-9981-75A932050980/10856_wide_250x141_2x.jpg)

![Apple image 13 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/9C184A72-5AD1-4D1C-9981-75A932050980/10856_wide_250x141_3x.jpg)

![Apple image 14 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/action-button.svg)

![Apple image 15 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/app-intents-PageImage-card@2x.png)

![Apple image 16 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/app-intents-PageImage-card~dark@2x.png)

![Apple image 17 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-thumbnail@2x.png)

![Apple image 18 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-thumbnail~dark@2x.png)

![Apple image 19 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-live-activities-thumbnail@2x.png)

![Apple image 20 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-live-activities-thumbnail~dark@2x.png)

![Apple image 21 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-snippets-thumbnail@2x.png)

![Apple image 22 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-snippets-thumbnail~dark@2x.png)

![Apple image 23 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-system-experiences-thumbnail@2x.png)

![Apple image 24 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-system-experiences-thumbnail~dark@2x.png)

![Apple image 25 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components@2x.png)

![Apple image 26 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components~dark@2x.png)

![Apple image 27 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/displaying-static-and-interactive-snippets-PageImage-card@2x.png)

![Apple image 28 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.AppIntents/displaying-static-and-interactive-snippets-PageImage-card~dark@2x.png)

![Apple image 29 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 30 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 32 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-action-button-thumbnail@2x.png)

![Apple image 33 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-action-button-thumbnail~dark@2x.png)

![Apple image 34 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 35 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

![Apple image 36 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/siri.svg)

![Apple image 37 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system.svg)

![Apple image 38 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-siri-thumbnail@2x.png)

![Apple image 39 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-siri-thumbnail~dark@2x.png)

</details>
