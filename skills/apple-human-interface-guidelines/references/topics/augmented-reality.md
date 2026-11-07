# Augmented reality

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/augmented-reality) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/augmented-reality.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Offer AR on capable hardware and make virtual content behave convincingly within the environment.
- Consider placement, lighting, reflection, and the person's physical movement as part of the interaction.

## Source section outline

- Best practices
- Providing coaching
- Helping people place objects
- Designing object interactions
- Offering a multiuser experience
- Reacting to real-world objects
- Communicating with people
- Handling interruptions
- Suggesting problem resolutions
- Icons and badges
- Platform considerations
- visionOS
- Resources
- Related
- Developer documentation
- Videos

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-augmented-reality-intro@2x.png)

<details>
<summary>All 65 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-augmented-reality-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-augmented-reality-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-measure-carrots@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-coaching-overlay@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-app-specific-indicator@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-user-interaction-direct@2x.png)

![Apple image 7 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-user-interaction-direct~dark@2x.png)

![Apple image 8 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-user-interaction-indirect@2x.png)

![Apple image 9 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-user-interaction-indirect~dark@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-plane-movement@2x.png)

![Apple image 11 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-plane-movement~dark@2x.png)

![Apple image 12 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-axis-rotation@2x.png)

![Apple image 13 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-axis-rotation~dark@2x.png)

![Apple image 14 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-3d-hint@2x.png)

![Apple image 15 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-3d-hint~dark@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-2d-hint@2x.png)

![Apple image 17 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-2d-hint~dark@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-labels@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-popover@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-popover~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-vertical-orientation@2x.png)

![Apple image 22 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-sufficient-lighting@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-insufficient-lighting@2x.png)

![Apple image 24 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-glyph@2x.png)

![Apple image 25 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-glyph~dark@2x.png)

![Apple image 26 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-glyph-button@2x.png)

![Apple image 27 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-glyph-button~dark@2x.png)

![Apple image 28 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-glyph-minimum-clear-space@2x.png)

![Apple image 29 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-glyph-minimum-clear-space~dark@2x.png)

![Apple image 30 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badging@2x.png)

![Apple image 31 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badging~dark@2x.png)

![Apple image 32 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badge-iconandtext@2x.png)

![Apple image 33 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badge-iconandtext~dark@2x.png)

![Apple image 34 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badge-icon@2x.png)

![Apple image 35 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badge-icon~dark@2x.png)

![Apple image 36 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badge-iconandtext-clear@2x.png)

![Apple image 37 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badge-iconandtext-clear~dark@2x.png)

![Apple image 38 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badge-icon-clear@2x.png)

![Apple image 39 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality-badge-icon-clear~dark@2x.png)

![Apple image 40 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/119/53F3827F-2C69-44D5-9D85-73AF3FF759FD/4965_wide_250x141_1x.jpg)

![Apple image 41 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/119/53F3827F-2C69-44D5-9D85-73AF3FF759FD/4965_wide_250x141_2x.jpg)

![Apple image 42 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/119/53F3827F-2C69-44D5-9D85-73AF3FF759FD/4965_wide_250x141_3x.jpg)

![Apple image 43 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/124/D9569ADB-FA90-4DB7-9987-A4366BA0E921/6628_wide_250x141_1x.jpg)

![Apple image 44 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/124/D9569ADB-FA90-4DB7-9987-A4366BA0E921/6628_wide_250x141_2x.jpg)

![Apple image 45 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/124/D9569ADB-FA90-4DB7-9987-A4366BA0E921/6628_wide_250x141_3x.jpg)

![Apple image 46 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/augmented-reality.svg)

![Apple image 47 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-immersive-experiences-thumbnail@2x.png)

![Apple image 48 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-immersive-experiences-thumbnail~dark@2x.png)

![Apple image 49 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/gestures.svg)

![Apple image 50 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 51 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/immersive-experiences.svg)

![Apple image 52 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail@2x.png)

![Apple image 53 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail~dark@2x.png)

![Apple image 54 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 55 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-audio-thumbnail@2x.png)

![Apple image 56 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-audio-thumbnail~dark@2x.png)

![Apple image 57 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-thumbnail@2x.png)

![Apple image 58 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-thumbnail~dark@2x.png)

![Apple image 59 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-audio.svg)

![Apple image 60 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-haptics.svg)

![Apple image 61 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-augmented-reality-thumbnail@2x.png)

![Apple image 62 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-augmented-reality-thumbnail~dark@2x.png)

![Apple image 63 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 64 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

![Apple image 65 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-augmented-reality-meteor@2x.png)

</details>
