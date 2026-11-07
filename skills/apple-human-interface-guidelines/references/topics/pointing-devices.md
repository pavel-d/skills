# Pointing devices

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/pointing-devices.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Preserve standard mouse and trackpad gestures and provide coherent behavior across other supported inputs.
- Verify hover, pointer access to hidden controls, and the transition between pointer and touch interaction.

## Source section outline

- Best practices
- Platform considerations
- iPadOS
- Pointer shape and content effects
- Pointer accessories
- Standard pointers and effects
- Customizing pointers
- macOS
- Pointers
- Touch support for hidden controls
- visionOS
- Resources
- Related
- Developer documentation
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-pointing-devices-intro@2x.png)

<details>
<summary>All 63 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-pointing-devices-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-pointing-devices-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/padding-for-button-with-bezel@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/padding-for-button-with-bezel~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/padding-for-glyph@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/padding-for-glyph~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/padding-for-button-without-bezel@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/padding-for-button-without-bezel~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/useful-pointer-annotation@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/useful-pointer-annotation~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-default@2x.png)

![Apple image 14 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-closed-hand@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-contextual-menu@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-crosshair@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-disappearing-item@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-drag-copy@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-drag-link@2x.png)

![Apple image 20 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-horizontal-i-beam@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-open-hand@2x.png)

![Apple image 22 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-operation-not-allowed@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-pointing-hand@2x.png)

![Apple image 24 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-down@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-east@2x.png)

![Apple image 26 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-east-west@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-left@2x.png)

![Apple image 28 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-left-right@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-north@2x.png)

![Apple image 30 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-north-south@2x.png)

![Apple image 31 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-northeast@2x.png)

![Apple image 32 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-northeast-southwest@2x.png)

![Apple image 33 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-northwest@2x.png)

![Apple image 34 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-northwest-southeast@2x.png)

![Apple image 35 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-right@2x.png)

![Apple image 36 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-south@2x.png)

![Apple image 37 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-southeast@2x.png)

![Apple image 38 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-southwest@2x.png)

![Apple image 39 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-up@2x.png)

![Apple image 40 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-resize-up-down@2x.png)

![Apple image 41 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-west@2x.png)

![Apple image 42 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-vertical-i-beam@2x.png)

![Apple image 43 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-zoom-in@2x.png)

![Apple image 44 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointers-zoom-out@2x.png)

![Apple image 45 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-context-menus-thumbnail@2x.png)

![Apple image 46 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-context-menus-thumbnail~dark@2x.png)

![Apple image 47 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/data-entry.svg)

![Apple image 48 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/gestures.svg)

![Apple image 49 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 50 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail@2x.png)

![Apple image 51 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail~dark@2x.png)

![Apple image 52 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-keyboards-thumbnail@2x.png)

![Apple image 53 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-keyboards-thumbnail~dark@2x.png)

![Apple image 54 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-pointing-devices-thumbnail@2x.png)

![Apple image 55 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-pointing-devices-thumbnail~dark@2x.png)

![Apple image 56 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs@2x.png)

![Apple image 57 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs~dark@2x.png)

![Apple image 58 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/keyboards.svg)

![Apple image 59 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 60 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-entering-data-thumbnail@2x.png)

![Apple image 61 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-entering-data-thumbnail~dark@2x.png)

![Apple image 62 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/pointing-devices.svg)

![Apple image 63 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-trackpad-pointer-input@2x.png)

</details>
