# Playing haptics

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/playing-haptics.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Use established haptic meanings consistently and sparingly.
- Complement other feedback so understanding the result does not depend on feeling a vibration.

## Source section outline

- Best practices
- Custom haptics
- Platform considerations
- iOS
- Notification
- Impact
- Selection
- macOS
- watchOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-intro@2x.png)

<details>
<summary>All 45 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-intro~dark@2x.png)

![Apple image 3 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/119/100FA6DD-1A48-485A-AFC2-47FDB92376D3/5210_wide_250x141_1x.jpg)

![Apple image 4 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/119/100FA6DD-1A48-485A-AFC2-47FDB92376D3/5210_wide_250x141_2x.jpg)

![Apple image 5 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/119/100FA6DD-1A48-485A-AFC2-47FDB92376D3/5210_wide_250x141_3x.jpg)

![Apple image 6 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/48/9EEAE751-B5EE-4934-8F3A-38361FBA05DE/3277_wide_250x141_1x.jpg)

![Apple image 7 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/48/9EEAE751-B5EE-4934-8F3A-38361FBA05DE/3277_wide_250x141_2x.jpg)

![Apple image 8 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/48/9EEAE751-B5EE-4934-8F3A-38361FBA05DE/3277_wide_250x141_3x.jpg)

![Apple image 9 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-and-scribble.svg)

![Apple image 10 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/error@2x.png)

![Apple image 11 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/error~dark@2x.png)

![Apple image 12 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/feedback.svg)

![Apple image 13 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls.svg)

![Apple image 14 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/gestures.svg)

![Apple image 15 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 16 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-heavy@2x.png)

![Apple image 17 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-heavy~dark@2x.png)

![Apple image 18 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-light@2x.png)

![Apple image 19 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-light~dark@2x.png)

![Apple image 20 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-medium@2x.png)

![Apple image 21 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-medium~dark@2x.png)

![Apple image 22 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-rigid@2x.png)

![Apple image 23 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-rigid~dark@2x.png)

![Apple image 24 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-soft@2x.png)

![Apple image 25 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/impact-soft~dark@2x.png)

![Apple image 26 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-apple-pencil-and-scribble-thumbnail@2x.png)

![Apple image 27 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-apple-pencil-and-scribble-thumbnail~dark@2x.png)

![Apple image 28 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-thumbnail@2x.png)

![Apple image 29 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-thumbnail~dark@2x.png)

![Apple image 30 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail@2x.png)

![Apple image 31 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-gestures-thumbnail~dark@2x.png)

![Apple image 32 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-feedback-thumbnail@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-feedback-thumbnail~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-haptics-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns~dark@2x.png)

![Apple image 39 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-haptics.svg)

![Apple image 40 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/retarget@2x.png)

![Apple image 41 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/retarget~dark@2x.png)

![Apple image 42 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/success@2x.png)

![Apple image 43 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/success~dark@2x.png)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/warning@2x.png)

![Apple image 45 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/warning~dark@2x.png)

</details>
