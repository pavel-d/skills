# Multitasking

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/multitasking.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Preserve state as people switch tasks, resize windows, or encounter audio interruptions.
- Finish appropriate initiated work in the background while pausing activities that need active participation.

## Source section outline

- Best practices
- Platform considerations
- iOS
- iPadOS
- macOS
- tvOS
- visionOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-multitasking-intro@2x.png)

<details>
<summary>All 38 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-multitasking-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-multitasking-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/multitasking-app-switcher-iphone@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/multitasking-app-switcher-iphone~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/multitasking-pip-iphone@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/multitasking-pip-iphone~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/multitasking-ipad-app-switcher@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/multitasking-ipad-app-switcher~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/multitasking-ipad-windows-maps-landmarks@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/multitasking-ipad-windows-maps-landmarks~dark@2x.png)

![Apple image 11 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/873F40BE-101A-4C0D-99F0-F5C7CE7B47A3/10046_wide_250x141_1x.jpg)

![Apple image 12 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/873F40BE-101A-4C0D-99F0-F5C7CE7B47A3/10046_wide_250x141_2x.jpg)

![Apple image 13 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/873F40BE-101A-4C0D-99F0-F5C7CE7B47A3/10046_wide_250x141_3x.jpg)

![Apple image 14 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/A8CAF870-197F-4982-83D8-56513E5D7D0B/10000_wide_250x141_1x.jpg)

![Apple image 15 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/A8CAF870-197F-4982-83D8-56513E5D7D0B/10000_wide_250x141_2x.jpg)

![Apple image 16 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/A8CAF870-197F-4982-83D8-56513E5D7D0B/10000_wide_250x141_3x.jpg)

![Apple image 17 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-windows-thumbnail@2x.png)

![Apple image 18 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-windows-thumbnail~dark@2x.png)

![Apple image 19 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-layout-thumbnail@2x.png)

![Apple image 20 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-layout-thumbnail~dark@2x.png)

![Apple image 21 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 22 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/layout.svg)

![Apple image 23 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/managing-notifications.svg)

![Apple image 24 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/multitasking.svg)

![Apple image 25 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 26 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-managing-notifications-thumbnail@2x.png)

![Apple image 27 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-managing-notifications-thumbnail~dark@2x.png)

![Apple image 28 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-multitasking-thumbnail@2x.png)

![Apple image 29 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-multitasking-thumbnail~dark@2x.png)

![Apple image 30 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-audio-thumbnail@2x.png)

![Apple image 31 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-audio-thumbnail~dark@2x.png)

![Apple image 32 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-video-thumbnail@2x.png)

![Apple image 33 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-video-thumbnail~dark@2x.png)

![Apple image 34 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns@2x.png)

![Apple image 35 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns~dark@2x.png)

![Apple image 36 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-audio.svg)

![Apple image 37 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-video.svg)

![Apple image 38 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-multiple-windows@2x.png)

</details>
