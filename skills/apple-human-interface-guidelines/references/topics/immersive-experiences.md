# Immersive experiences

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Choose immersion deliberately and keep the person's awareness and comfort central to transitions.
- Use environmental dimming or unbounded content only when it supports attention and the intended spatial experience.

## Source section outline

- Immersion and passthrough
- Immersion styles
- Best practices
- Promoting comfort
- Transitioning between immersive styles
- Displaying virtual hands
- Creating an environment
- Platform considerations
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-immersive-experiences-intro@2x.png)

<details>
<summary>All 42 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-immersive-experiences-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-immersive-experiences-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/immersive-spaces-shared-space-regular-content@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/immersive-spaces-shared-space-dimmed-content@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/immersive-spaces-full-space-mixed-style@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/immersive-spaces-full-space-progressive-style@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/immersive-spaces-full-space-full-style@2x.png)

![Apple image 8 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/0BDEE063-38E4-4DFC-B55F-B68D8948B1C0/10757_wide_250x141_1x.jpg)

![Apple image 9 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/0BDEE063-38E4-4DFC-B55F-B68D8948B1C0/10757_wide_250x141_2x.jpg)

![Apple image 10 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/0BDEE063-38E4-4DFC-B55F-B68D8948B1C0/10757_wide_250x141_3x.jpg)

![Apple image 11 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg)

![Apple image 12 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_2x.jpg)

![Apple image 13 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_3x.jpg)

![Apple image 14 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/942191E7-9B98-487D-AE81-400D58285B31/8129_wide_250x141_1x.jpg)

![Apple image 15 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/942191E7-9B98-487D-AE81-400D58285B31/8129_wide_250x141_2x.jpg)

![Apple image 16 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/942191E7-9B98-487D-AE81-400D58285B31/8129_wide_250x141_3x.jpg)

![Apple image 17 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/accessibility.svg)

![Apple image 18 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/digital-crown.svg)

![Apple image 19 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail@2x.png)

![Apple image 20 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail~dark@2x.png)

![Apple image 21 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-immersive-experiences-thumbnail@2x.png)

![Apple image 22 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-immersive-experiences-thumbnail~dark@2x.png)

![Apple image 23 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-motion-thumbnail@2x.png)

![Apple image 24 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-motion-thumbnail~dark@2x.png)

![Apple image 25 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-privacy-thumbnail@2x.png)

![Apple image 26 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-privacy-thumbnail~dark@2x.png)

![Apple image 27 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-spatial-layout-thumbnail@2x.png)

![Apple image 28 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-spatial-layout-thumbnail~dark@2x.png)

![Apple image 29 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations@2x.png)

![Apple image 30 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations~dark@2x.png)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 32 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/immersive-experiences.svg)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-digital-crown-thumbnail@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-digital-crown-thumbnail~dark@2x.png)

![Apple image 35 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/motion.svg)

![Apple image 36 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-audio-thumbnail@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-audio-thumbnail~dark@2x.png)

![Apple image 39 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-audio.svg)

![Apple image 40 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy.svg)

![Apple image 41 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/spatial-layout.svg)

![Apple image 42 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-immersion-level-adjustment.png)

</details>
