# Activity rings

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/activity-rings) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/activity-rings.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Use Activity rings for their established activity measurements and a single person's progress.
- Preserve their system meaning and appearance instead of repurposing them as generic metrics.

## Source section outline

- Best practices
- Platform considerations
- iOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/components-activity-ring-intro@2x.png)

<details>
<summary>All 32 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-activity-ring-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-activity-ring-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/activity-rings-summary@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/activity-rings-color-swatch-red@2x.png)

![Apple image 5 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/activity-rings-color-swatch-red~dark@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/activity-rings-color-swatch-green@2x.png)

![Apple image 7 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/activity-rings-color-swatch-green~dark@2x.png)

![Apple image 8 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/activity-rings-color-swatch-blue@2x.png)

![Apple image 9 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/activity-rings-color-swatch-blue~dark@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/activity-rings-watch-paired@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/activity-rings-no-watch-paired@2x.png)

![Apple image 12 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/12499BF9-8217-4A56-81CA-5E7CB66904DD/9856_wide_250x141_1x.jpg)

![Apple image 13 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/12499BF9-8217-4A56-81CA-5E7CB66904DD/9856_wide_250x141_2x.jpg)

![Apple image 14 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/12499BF9-8217-4A56-81CA-5E7CB66904DD/9856_wide_250x141_3x.jpg)

![Apple image 15 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/119/30D3C2CB-B24D-467A-9B20-A369641E966F/4850_wide_250x141_1x.jpg)

![Apple image 16 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/119/30D3C2CB-B24D-467A-9B20-A369641E966F/4850_wide_250x141_2x.jpg)

![Apple image 17 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/119/30D3C2CB-B24D-467A-9B20-A369641E966F/4850_wide_250x141_3x.jpg)

![Apple image 18 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/50551741-78CD-4E8A-9550-7D0EC29D7882/8035_wide_250x141_1x.jpg)

![Apple image 19 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/50551741-78CD-4E8A-9550-7D0EC29D7882/8035_wide_250x141_2x.jpg)

![Apple image 20 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/D35E0E85-CCB6-41A1-B227-7995ECD83ED5/50551741-78CD-4E8A-9550-7D0EC29D7882/8035_wide_250x141_3x.jpg)

![Apple image 21 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-activity-rings-thumbnail@2x.png)

![Apple image 22 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-activity-rings-thumbnail~dark@2x.png)

![Apple image 23 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-status-thumbnail@2x.png)

![Apple image 24 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-status-thumbnail~dark@2x.png)

![Apple image 25 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components@2x.png)

![Apple image 26 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components~dark@2x.png)

![Apple image 27 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 28 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 29 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-workouts-thumbnail@2x.png)

![Apple image 30 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-workouts-thumbnail~dark@2x.png)

![Apple image 31 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/status.svg)

![Apple image 32 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/workouts.svg)

</details>
