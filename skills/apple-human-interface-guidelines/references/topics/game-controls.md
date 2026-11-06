# Game controls

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/game-controls) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/game-controls.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Choose controls appropriate to the game and platform, with clear visual and tactile feedback.
- Check reachability and target size when virtual controls overlay gameplay.

## Source section outline

- Touch controls
- Physical controllers
- Keyboards
- Platform considerations
- visionOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-intro@2x.png)

<details>
<summary>All 47 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-touch-input-heat-map@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-press-state@2x.png)

![Apple image 5 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-press-state~dark@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-button-to-action@2x.png)

![Apple image 7 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-button-to-action~dark@2x.png)

![Apple image 8 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-thumbstick-in-motion@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-thumbstick-at-rest@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-power-up-action@2x.png)

![Apple image 11 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-power-up-action~dark@2x.png)

![Apple image 12 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-camera-thumbstick-zones@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-controller-anatomy@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-controller-anatomy~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-sf-symbols-gaming-category@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls-sf-symbols-gaming-category~dark@2x.png)

![Apple image 17 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/2DB746B8-E0B0-4ED1-B250-902DB7A0F3E7/9196_wide_250x141_1x.jpg)

![Apple image 18 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/2DB746B8-E0B0-4ED1-B250-902DB7A0F3E7/9196_wide_250x141_2x.jpg)

![Apple image 19 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/2DB746B8-E0B0-4ED1-B250-902DB7A0F3E7/9196_wide_250x141_3x.jpg)

![Apple image 20 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/51863C09-0E96-4230-91A3-B85E950FBF3D/9205_wide_250x141_1x.jpg)

![Apple image 21 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/51863C09-0E96-4230-91A3-B85E950FBF3D/9205_wide_250x141_2x.jpg)

![Apple image 22 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/51863C09-0E96-4230-91A3-B85E950FBF3D/9205_wide_250x141_3x.jpg)

![Apple image 23 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/7A9C7D51-DEF9-4C8E-A2B1-E771A34910A7/10908_wide_250x141_1x.jpg)

![Apple image 24 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/7A9C7D51-DEF9-4C8E-A2B1-E771A34910A7/10908_wide_250x141_2x.jpg)

![Apple image 25 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/7A9C7D51-DEF9-4C8E-A2B1-E771A34910A7/10908_wide_250x141_3x.jpg)

![Apple image 26 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-games.svg)

![Apple image 27 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 28 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 29 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls.svg)

![Apple image 30 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/gestures.svg)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 32 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-thumbnail@2x.png)

![Apple image 33 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-thumbnail~dark@2x.png)

![Apple image 34 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail@2x.png)

![Apple image 35 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail~dark@2x.png)

![Apple image 36 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-keyboards-thumbnail@2x.png)

![Apple image 37 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-keyboards-thumbnail~dark@2x.png)

![Apple image 38 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs@2x.png)

![Apple image 39 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs~dark@2x.png)

![Apple image 40 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/keyboards.svg)

![Apple image 41 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 42 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-thumbnail@2x.png)

![Apple image 43 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-thumbnail~dark@2x.png)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-games-thumbnail@2x.png)

![Apple image 45 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-games-thumbnail~dark@2x.png)

![Apple image 46 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-haptics.svg)

![Apple image 47 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

</details>
