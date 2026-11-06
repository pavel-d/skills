# Live Activities

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/live-activities) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/live-activities.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Represent a real ongoing event with a defined start and finish using concise current information.
- Avoid advertising and unnecessary exposure of sensitive content on these glanceable surfaces.

## Source section outline

- Anatomy
- Compact
- Minimal
- Expanded
- Lock Screen
- StandBy
- Best practices
- Creating Live Activity layouts
- Choosing colors
- Adding transitions and animating content updates
- Offering interactivity
- Starting, updating, and ending a Live Activity
- Presentation
- Compact presentation
- Minimal presentation
- Expanded presentation
- Lock Screen presentation
- StandBy presentation
- CarPlay
- Platform considerations
- macOS
- watchOS
- Specifications
- CarPlay dimensions
- iOS dimensions
- iPadOS dimensions
- macOS dimensions
- watchOS dimensions
- Resources
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/components-live-activities-intro@2x.png)

<details>
<summary>All 84 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-live-activities-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-live-activities-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/type-compact@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/type-compact~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/type-minimal@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/type-minimal~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/type-expanded@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/type-expanded~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-lock-screen@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-lock-screen~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-notch@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-notch~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-standby-default-outline@2x.png)

![Apple image 14 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-text-incorrect-size@2x.png)

![Apple image 15 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-text-incorrect-size~dark@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-text-correct-size@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-text-correct-size~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 20 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-margins@2x.png)

![Apple image 21 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-margins~dark@2x.png)

![Apple image 22 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-rounded-shapes@2x.png)

![Apple image 23 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-rounded-shapes~dark@2x.png)

![Apple image 24 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-content-incorrect-position@2x.png)

![Apple image 25 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-content-incorrect-position~dark@2x.png)

![Apple image 26 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-content-correct-position@2x.png)

![Apple image 27 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-content-correct-position~dark@2x.png)

![Apple image 28 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-separating-content-incorrect@2x.png)

![Apple image 29 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-separating-content-incorrect~dark@2x.png)

![Apple image 30 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-separating-content-pill@2x.png)

![Apple image 31 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-separating-content-pill~dark@2x.png)

![Apple image 32 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-separating-content-separator@2x.png)

![Apple image 33 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-separating-content-separator~dark@2x.png)

![Apple image 34 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-blur-content-incorrect-position@2x.png)

![Apple image 35 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-blur-content-incorrect-position~dark@2x.png)

![Apple image 36 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-blur-content-correct-position@2x.png)

![Apple image 37 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-blur-content-correct-position~dark@2x.png)

![Apple image 38 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-unbalanced-content@2x.png)

![Apple image 39 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-unbalanced-content~dark@2x.png)

![Apple image 40 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-balanced-content@2x.png)

![Apple image 41 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-balanced-content~dark@2x.png)

![Apple image 42 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-layout-incorrect@2x.png)

![Apple image 43 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-layout-incorrect~dark@2x.png)

![Apple image 44 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-layout-correct@2x.png)

![Apple image 45 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-layout-correct~dark@2x.png)

![Apple image 46 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-standby-night-mode@2x.png)

![Apple image 47 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-ios-dynamic-island-default@2x.png)

![Apple image 48 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activities-ios-dynamic-island-default~dark@2x.png)

![Apple image 49 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-watch-default-implementation@2x.png)

![Apple image 50 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-watch-default-implementation~dark@2x.png)

![Apple image 51 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-watch-custom-implementation@2x.png)

![Apple image 52 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/live-activity-watch-custom-implementation~dark@2x.png)

![Apple image 53 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/126547AE-9E47-4E15-AC05-5C50AB08CBEE/9952_wide_250x141_1x.jpg)

![Apple image 54 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/126547AE-9E47-4E15-AC05-5C50AB08CBEE/9952_wide_250x141_2x.jpg)

![Apple image 55 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/126547AE-9E47-4E15-AC05-5C50AB08CBEE/9952_wide_250x141_3x.jpg)

![Apple image 56 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/3AE21C44-8831-4C0A-BCBE-68C437FB8FC8/9903_wide_250x141_1x.jpg)

![Apple image 57 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/3AE21C44-8831-4C0A-BCBE-68C437FB8FC8/9903_wide_250x141_2x.jpg)

![Apple image 58 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/3AE21C44-8831-4C0A-BCBE-68C437FB8FC8/9903_wide_250x141_3x.jpg)

![Apple image 59 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/88E22B76-610C-4EBC-8E36-16E02B76781B/10734_wide_250x141_1x.jpg)

![Apple image 60 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/88E22B76-610C-4EBC-8E36-16E02B76781B/10734_wide_250x141_2x.jpg)

![Apple image 61 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/88E22B76-610C-4EBC-8E36-16E02B76781B/10734_wide_250x141_3x.jpg)

![Apple image 62 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.activitykit/ActivityKit-PageImage-card@2x.png)

![Apple image 63 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.activitykit/ActivityKit-PageImage-card~dark@2x.png)

![Apple image 64 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.WidgetKit/Developing-a-WidgetKit-strategy-PageImage-card@2x.png)

![Apple image 65 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.WidgetKit/Developing-a-WidgetKit-strategy-PageImage-card~dark@2x.png)

![Apple image 66 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-PageImage-card@2x.png)

![Apple image 67 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-PageImage-card~dark@2x.png)

![Apple image 68 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/always-on.svg)

![Apple image 69 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-thumbnail@2x.png)

![Apple image 70 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-thumbnail~dark@2x.png)

![Apple image 71 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-live-activities-thumbnail@2x.png)

![Apple image 72 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-live-activities-thumbnail~dark@2x.png)

![Apple image 73 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-system-experiences-thumbnail@2x.png)

![Apple image 74 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-system-experiences-thumbnail~dark@2x.png)

![Apple image 75 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components@2x.png)

![Apple image 76 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components~dark@2x.png)

![Apple image 77 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode.svg)

![Apple image 78 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-dark-mode-thumbnail@2x.png)

![Apple image 79 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-dark-mode-thumbnail~dark@2x.png)

![Apple image 80 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 81 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 82 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system.svg)

![Apple image 83 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-always-on-thumbnail@2x.png)

![Apple image 84 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-always-on-thumbnail~dark@2x.png)

</details>
