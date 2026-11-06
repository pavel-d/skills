# Charts

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/charts) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/charts.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Choose marks and axis ranges to preserve the meaning of the intended comparison.
- Check labels, scales, accessibility, and whether combined marks clarify rather than distort the data.

## Source section outline

- Anatomy
- Marks
- Axes
- Descriptive content
- Best practices
- Color
- Enhancing the accessibility of a chart
- Platform considerations
- watchOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/components-charts-intro@2x.png)

<details>
<summary>All 47 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-charts-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-charts-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-anatomy@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-anatomy~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-bar-marks@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-bar-marks~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-line-marks@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-line-marks~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-point-marks@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-point-marks~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-fixed-range-axis@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-fixed-range-axis~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-dynamic-range-axis-small@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-dynamic-range-axis-small~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-dynamic-range-axis-large@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-dynamic-range-axis-large~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-descriptive-content@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-colors@2x.png)

![Apple image 19 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-colors~dark@2x.png)

![Apple image 20 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-colors-stacked@2x.png)

![Apple image 21 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-colors-stacked~dark@2x.png)

![Apple image 22 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-bar-chart-with-voiceover-focus@2x.png)

![Apple image 23 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/charts-bar-chart-with-voiceover-focus~dark@2x.png)

![Apple image 24 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/124/4BBCB61E-65ED-43FE-8F7B-81524E0C96BE/6692_wide_250x141_1x.jpg)

![Apple image 25 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/124/4BBCB61E-65ED-43FE-8F7B-81524E0C96BE/6692_wide_250x141_2x.jpg)

![Apple image 26 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/124/4BBCB61E-65ED-43FE-8F7B-81524E0C96BE/6692_wide_250x141_3x.jpg)

![Apple image 27 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/89D5888B-58DA-4F47-8E3C-998253F6BA98/9954_wide_250x141_1x.jpg)

![Apple image 28 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/89D5888B-58DA-4F47-8E3C-998253F6BA98/9954_wide_250x141_2x.jpg)

![Apple image 29 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/89D5888B-58DA-4F47-8E3C-998253F6BA98/9954_wide_250x141_3x.jpg)

![Apple image 30 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/124/FA764D2D-4E15-4E91-91BA-BDAC80FB901B/6694_wide_250x141_1x.jpg)

![Apple image 31 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/124/FA764D2D-4E15-4E91-91BA-BDAC80FB901B/6694_wide_250x141_2x.jpg)

![Apple image 32 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/124/FA764D2D-4E15-4E91-91BA-BDAC80FB901B/6694_wide_250x141_3x.jpg)

![Apple image 33 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/accessibility.svg)

![Apple image 34 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/charting-data.svg)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-charts-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-charts-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-content-thumbnail@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-content-thumbnail~dark@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components@2x.png)

![Apple image 40 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components~dark@2x.png)

![Apple image 41 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/content.svg)

![Apple image 42 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail@2x.png)

![Apple image 43 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail~dark@2x.png)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 45 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 46 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-charting-data-thumbnail@2x.png)

![Apple image 47 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-charting-data-thumbnail~dark@2x.png)

</details>
