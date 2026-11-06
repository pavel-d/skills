# Camera Control

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/camera-control) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/camera-control.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Keep capture controls recognizable with short names, suitable symbols, and meaningful value units.
- Identify important slider values and verify the hardware interaction on supported devices.

## Source section outline

- Anatomy
- Best practices
- Platform considerations
- Resources
- Related
- Developer documentation
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-camera-control-intro@2x.png)

<details>
<summary>All 44 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-camera-control-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-camera-control-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-button-callout@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-button-callout~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-picker@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-picker~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-slider-control@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-slider-control~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-picker-control@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-picker-control~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-control-type-zoom-factor@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-control-type-zoom-factor~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-control-type-exposure-bias@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-control-type-exposure-bias~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-picker-sf-symbols-flash@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-picker-sf-symbols-flash~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-picker-sf-symbols-filters@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-picker-sf-symbols-filters~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-control-with-label@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-control-with-label~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 22 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-control-no-label@2x.png)

![Apple image 23 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/system-control-no-label~dark@2x.png)

![Apple image 24 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-portrait-landscape-orientation@2x.png)

![Apple image 26 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-portrait-landscape-orientation~dark@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-screen-ui-good-example@2x.png)

![Apple image 28 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-screen-ui-good-example~dark@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-screen-ui-bad-example@2x.png)

![Apple image 30 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control-screen-ui-bad-example~dark@2x.png)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.avfoundation/camera-control-PageImage-card@2x.png)

![Apple image 32 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.avfoundation/camera-control-PageImage-card~dark@2x.png)

![Apple image 33 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/camera-control.svg)

![Apple image 34 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-controls-thumbnail@2x.png)

![Apple image 35 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-controls-thumbnail~dark@2x.png)

![Apple image 36 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 37 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 38 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-camera-control-thumbnail@2x.png)

![Apple image 40 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-camera-control-thumbnail~dark@2x.png)

![Apple image 41 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs@2x.png)

![Apple image 42 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs~dark@2x.png)

![Apple image 43 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 44 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

</details>
