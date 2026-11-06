# Designing for visionOS

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Choose windows, volumes, and immersion according to the task and the person's physical surroundings.
- Evaluate targeting, viewing comfort, passthrough, and transitions with spatial input rather than assuming a flat-screen layout transfers unchanged.

## Source section outline

- Best practices
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-visionOS-intro@2x.png)

<details>
<summary>All 34 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-visionOS-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-visionOS-intro~dark@2x.png)

![Apple image 3 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_1x.jpg)

![Apple image 4 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_2x.jpg)

![Apple image 5 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/15489B11-8744-483D-AD38-EF78D8962FF4/8126_wide_250x141_3x.jpg)

![Apple image 6 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/A207EE2A-D9E6-4FAB-A557-ABEAA68840AB/9197_wide_250x141_1x.jpg)

![Apple image 7 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/A207EE2A-D9E6-4FAB-A557-ABEAA68840AB/9197_wide_250x141_2x.jpg)

![Apple image 8 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/A207EE2A-D9E6-4FAB-A557-ABEAA68840AB/9197_wide_250x141_3x.jpg)

![Apple image 9 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/B2E0763D-C5D2-4191-AC0B-F99D56BE781F/9208_wide_250x141_1x.jpg)

![Apple image 10 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/B2E0763D-C5D2-4191-AC0B-F99D56BE781F/9208_wide_250x141_2x.jpg)

![Apple image 11 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/C03E6E6D-A32A-41D0-9E50-C3C6059820AA/B2E0763D-C5D2-4191-AC0B-F99D56BE781F/9208_wide_250x141_3x.jpg)

![Apple image 12 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.visionOS/Creating-your-first-visionOS-app-PageImage-card@2x.png)

![Apple image 13 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.visionOS/Creating-your-first-visionOS-app-PageImage-card~dark@2x.png)

![Apple image 14 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/accessibility.svg)

![Apple image 15 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-windows-thumbnail@2x.png)

![Apple image 16 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-windows-thumbnail~dark@2x.png)

![Apple image 17 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/digital-crown.svg)

![Apple image 18 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/eyes.svg)

![Apple image 19 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail@2x.png)

![Apple image 20 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail~dark@2x.png)

![Apple image 21 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-immersive-experiences-thumbnail@2x.png)

![Apple image 22 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-immersive-experiences-thumbnail~dark@2x.png)

![Apple image 23 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 24 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/immersive-experiences.svg)

![Apple image 25 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-digital-crown-thumbnail@2x.png)

![Apple image 26 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-digital-crown-thumbnail~dark@2x.png)

![Apple image 27 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-eyes-thumbnail@2x.png)

![Apple image 28 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-eyes-thumbnail~dark@2x.png)

![Apple image 29 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 30 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-visionos-thumbnail@2x.png)

![Apple image 31 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-visionos-thumbnail~dark@2x.png)

![Apple image 32 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms@2x.png)

![Apple image 33 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms~dark@2x.png)

![Apple image 34 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos.svg)

</details>
