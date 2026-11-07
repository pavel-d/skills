# Gestures

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/gestures) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/gestures.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Honor familiar gesture meanings and respond promptly.
- Provide another way to complete important actions and communicate unavailable interactions.

## Source section outline

- Best practices
- Custom gestures
- Platform considerations
- iOS, iPadOS
- macOS
- tvOS
- visionOS
- Designing custom gestures in visionOS
- Working with system overlays in visionOS
- watchOS
- Double tap
- Specifications
- Standard gestures
- macOS trackpad and touch display gestures
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-intro@2x.png)

<details>
<summary>All 59 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-custom-spatial-gesture-happy-beam@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-hand-area-of-focus@2x.png)

![Apple image 5 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-hand-area-of-focus~dark@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-spatial-gesture-home-indicator@2x.png)

![Apple image 7 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-spatial-gesture-home-indicator~dark@2x.png)

![Apple image 8 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-spatial-gesture-control-center@2x.png)

![Apple image 9 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-spatial-gesture-control-center~dark@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/gestures-default-home-indicator@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/gestures-home-indicator-in-immersive-space@2x.png)

![Apple image 12 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/gestures-fully-immersive-game-with-glove@2x.png)

![Apple image 13 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/B38CC217-7635-48EF-B8C9-F7954F390CCE/9273_wide_250x141_1x.jpg)

![Apple image 14 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/B38CC217-7635-48EF-B8C9-F7954F390CCE/9273_wide_250x141_2x.jpg)

![Apple image 15 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/B38CC217-7635-48EF-B8C9-F7954F390CCE/9273_wide_250x141_3x.jpg)

![Apple image 16 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/8/B44DD0F5-C2D2-48D2-BD21-2E3B25CB88A3/11326_wide_250x141_1x.jpg)

![Apple image 17 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/8/B44DD0F5-C2D2-48D2-BD21-2E3B25CB88A3/11326_wide_250x141_2x.jpg)

![Apple image 18 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/8/B44DD0F5-C2D2-48D2-BD21-2E3B25CB88A3/11326_wide_250x141_3x.jpg)

![Apple image 19 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/C6CDCC79-CCD0-4D2F-A4D1-8FC70DC663DB/8127_wide_250x141_1x.jpg)

![Apple image 20 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/C6CDCC79-CCD0-4D2F-A4D1-8FC70DC663DB/8127_wide_250x141_2x.jpg)

![Apple image 21 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/C6CDCC79-CCD0-4D2F-A4D1-8FC70DC663DB/8127_wide_250x141_3x.jpg)

![Apple image 22 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/accessibility.svg)

![Apple image 23 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-and-scribble.svg)

![Apple image 24 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-notifications-thumbnail@2x.png)

![Apple image 25 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-notifications-thumbnail~dark@2x.png)

![Apple image 26 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/eyes.svg)

![Apple image 27 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/feedback.svg)

![Apple image 28 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail@2x.png)

![Apple image 29 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail~dark@2x.png)

![Apple image 30 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls.svg)

![Apple image 31 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/gestures.svg)

![Apple image 32 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-apple-pencil-and-scribble-thumbnail@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-apple-pencil-and-scribble-thumbnail~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-eyes-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-eyes-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-thumbnail@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-thumbnail~dark@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail@2x.png)

![Apple image 40 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail~dark@2x.png)

![Apple image 41 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-keyboards-thumbnail@2x.png)

![Apple image 42 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-keyboards-thumbnail~dark@2x.png)

![Apple image 43 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-pointing-devices-thumbnail@2x.png)

![Apple image 44 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-pointing-devices-thumbnail~dark@2x.png)

![Apple image 45 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-remotes-thumbnail@2x.png)

![Apple image 46 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-remotes-thumbnail~dark@2x.png)

![Apple image 47 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs@2x.png)

![Apple image 48 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs~dark@2x.png)

![Apple image 49 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/keyboards.svg)

![Apple image 50 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 51 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-feedback-thumbnail@2x.png)

![Apple image 52 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-feedback-thumbnail~dark@2x.png)

![Apple image 53 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-thumbnail@2x.png)

![Apple image 54 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-thumbnail~dark@2x.png)

![Apple image 55 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-haptics.svg)

![Apple image 56 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointing-devices.svg)

![Apple image 57 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/remotes.svg)

![Apple image 58 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-spatial-gesture-direct@2x.png)

![Apple image 59 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-spatial-gesture-indirect@2x.png)

</details>
