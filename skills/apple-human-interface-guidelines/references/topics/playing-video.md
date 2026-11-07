# Playing video

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/playing-video) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/playing-video.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Prefer familiar playback controls and preserve the video's aspect ratio.
- Evaluate presentation, captions, transport controls, and interruptions for the supported platforms.

## Source section outline

- Best practices
- Integrating with the TV app
- Loading content
- Exiting playback
- Platform considerations
- tvOS
- visionOS
- watchOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-video-intro@2x.png)

<details>
<summary>All 38 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-video-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-video-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/video-fill-4-3-right@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/video-fill-4-3-right~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/video-fill-4-3-wrong@2x.png)

![Apple image 7 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/video-fill-4-3-wrong~dark@2x.png)

![Apple image 8 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/legend-letter-pillar@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/legend-letter-pillar~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/video-fit-21-9-right@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/video-fit-21-9-right~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/video-fit-21-9-wrong@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/video-fit-21-9-wrong~dark@2x.png)

![Apple image 15 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/124/344FB830-5184-4C63-8D0C-D8861D31A70D/6645_wide_250x141_1x.jpg)

![Apple image 16 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/124/344FB830-5184-4C63-8D0C-D8861D31A70D/6645_wide_250x141_2x.jpg)

![Apple image 17 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/124/344FB830-5184-4C63-8D0C-D8861D31A70D/6645_wide_250x141_3x.jpg)

![Apple image 18 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/3F1BA6AB-BC74-4A1A-A440-90BA4AE5A23D/10042_wide_250x141_1x.jpg)

![Apple image 19 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/3F1BA6AB-BC74-4A1A-A440-90BA4AE5A23D/10042_wide_250x141_2x.jpg)

![Apple image 20 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/3F1BA6AB-BC74-4A1A-A440-90BA4AE5A23D/10042_wide_250x141_3x.jpg)

![Apple image 21 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/119/53F0161E-DB14-4A7D-8A94-B76244201AB8/5102_wide_250x141_1x.jpg)

![Apple image 22 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/119/53F0161E-DB14-4A7D-8A94-B76244201AB8/5102_wide_250x141_2x.jpg)

![Apple image 23 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/119/53F0161E-DB14-4A7D-8A94-B76244201AB8/5102_wide_250x141_3x.jpg)

![Apple image 24 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-ornaments-thumbnail@2x.png)

![Apple image 25 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-ornaments-thumbnail~dark@2x.png)

![Apple image 26 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/feedback.svg)

![Apple image 27 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 28 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 29 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-feedback-thumbnail@2x.png)

![Apple image 30 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-feedback-thumbnail~dark@2x.png)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-audio-thumbnail@2x.png)

![Apple image 32 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-audio-thumbnail~dark@2x.png)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-video-thumbnail@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-playing-video-thumbnail~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns~dark@2x.png)

![Apple image 37 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-audio.svg)

![Apple image 38 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/playing-video.svg)

</details>
