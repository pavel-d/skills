# Widgets

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/widgets) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/widgets.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Choose focused information and interactions that remain useful at a glance.
- Check each supported family and system context and route deeper work to the corresponding place in the app.

## Source section outline

- Anatomy
- System family widgets
- Accessory widgets
- Appearances
- Best practices
- Updating widget content
- Adding interactivity
- Choosing margins and padding
- Displaying text in widgets
- Using color
- Rendering modes
- Full-color
- Accented
- Vibrant
- Previews and placeholders
- Platform considerations
- iOS, iPadOS
- StandBy and CarPlay
- Apple HomeView
- visionOS
- Thresholds and sizes
- Mounting styles
- Treatment styles
- watchOS
- Specifications
- iOS dimensions
- iPadOS dimensions
- visionOS dimensions
- watchOS dimensions
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/components-widgets-intro@2x.png)

<details>
<summary>All 96 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-widgets-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-widgets-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-small@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-small~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-medium@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-medium~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-large@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-large~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-extra-large-landscape@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-extra-large-landscape~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-music-extra-large-portrait@2x.png)

![Apple image 12 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-accessory-calendar-circular@2x.png)

![Apple image 13 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-accessory-calendar-circular~dark@2x.png)

![Apple image 14 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-accessory-corner-widget-watch@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-accessory-calendar-inline@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-accessory-calendar-inline~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-accessory-calendar-rectangular@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-accessory-calendar-rectangular~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-default@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-default~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-clear@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-clear~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-tinted@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-tinted~dark@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-visionos-frame@2x.png)

![Apple image 26 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-ipad-lock-screen@2x.png)

![Apple image 27 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-ipad-lock-screen~dark@2x.png)

![Apple image 28 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-standby@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-standby-night-mode@2x.png)

![Apple image 30 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-rectangular-ios@2x.png)

![Apple image 31 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-rectangular-ios~dark@2x.png)

![Apple image 32 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-rectangular-watchos-complication@2x.png)

![Apple image 33 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-calendar-rectangular-watchos-smart-stack@2x.png)

![Apple image 34 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-ios-weather-small@2x.png)

![Apple image 35 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-reminders-large-unselected@2x.png)

![Apple image 36 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-reminders-large-unselected~dark@2x.png)

![Apple image 37 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-reminders-large-selected@2x.png)

![Apple image 38 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-reminders-large-selected~dark@2x.png)

![Apple image 39 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-stocks-medium@2x.png)

![Apple image 40 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-notes-light-appearance@2x.png)

![Apple image 41 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-notes-dark-appearance@2x.png)

![Apple image 42 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-tips-placeholder-content@2x.png)

![Apple image 43 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-tips-full-content@2x.png)

![Apple image 44 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-add-button-tint-color-notes@2x.png)

![Apple image 45 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-add-button-tint-color-notes~dark@2x.png)

![Apple image 46 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-add-button-tint-color-weather@2x.png)

![Apple image 47 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-add-button-tint-color-weather~dark@2x.png)

![Apple image 48 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widget-lock-screen-display-appearances@2x.png)

![Apple image 49 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/widget-lock-screen-display-appearances~dark@2x.png)

![Apple image 50 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-standby-removed-background-correct@2x.png)

![Apple image 51 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 52 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-standby-with-background-incorrect@2x.png)

![Apple image 53 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 54 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-standby-low-light@2x.png)

![Apple image 55 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-extra-large-portrait-far-proximity@2x.png)

![Apple image 56 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/widgets-extra-large-portrait-close-proximity@2x.png)

![Apple image 57 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/126547AE-9E47-4E15-AC05-5C50AB08CBEE/9952_wide_250x141_1x.jpg)

![Apple image 58 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/126547AE-9E47-4E15-AC05-5C50AB08CBEE/9952_wide_250x141_2x.jpg)

![Apple image 59 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/126547AE-9E47-4E15-AC05-5C50AB08CBEE/9952_wide_250x141_3x.jpg)

![Apple image 60 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/4D354E1F-5016-49F7-9296-3D3722626480/9957_wide_250x141_1x.jpg)

![Apple image 61 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/4D354E1F-5016-49F7-9296-3D3722626480/9957_wide_250x141_2x.jpg)

![Apple image 62 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/4D354E1F-5016-49F7-9296-3D3722626480/9957_wide_250x141_3x.jpg)

![Apple image 63 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.activitykit/ActivityKit-PageImage-card@2x.png)

![Apple image 64 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.activitykit/ActivityKit-PageImage-card~dark@2x.png)

![Apple image 65 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/C841E94B-3DBA-464C-A751-43F15ADC12A5/10804_wide_250x141_1x.jpg)

![Apple image 66 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/C841E94B-3DBA-464C-A751-43F15ADC12A5/10804_wide_250x141_2x.jpg)

![Apple image 67 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/C841E94B-3DBA-464C-A751-43F15ADC12A5/10804_wide_250x141_3x.jpg)

![Apple image 68 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.WidgetKit/Developing-a-WidgetKit-strategy-PageImage-card@2x.png)

![Apple image 69 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.WidgetKit/Developing-a-WidgetKit-strategy-PageImage-card~dark@2x.png)

![Apple image 70 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-PageImage-card@2x.png)

![Apple image 71 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-PageImage-card~dark@2x.png)

![Apple image 72 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-complications-thumbnail@2x.png)

![Apple image 73 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-complications-thumbnail~dark@2x.png)

![Apple image 74 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-live-activities-thumbnail@2x.png)

![Apple image 75 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-live-activities-thumbnail~dark@2x.png)

![Apple image 76 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-system-experiences-thumbnail@2x.png)

![Apple image 77 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-system-experiences-thumbnail~dark@2x.png)

![Apple image 78 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-widgets-thumbnail@2x.png)

![Apple image 79 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-widgets-thumbnail~dark@2x.png)

![Apple image 80 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components@2x.png)

![Apple image 81 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components~dark@2x.png)

![Apple image 82 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/dark-mode.svg)

![Apple image 83 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-dark-mode-thumbnail@2x.png)

![Apple image 84 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-dark-mode-thumbnail~dark@2x.png)

![Apple image 85 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-layout-thumbnail@2x.png)

![Apple image 86 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-layout-thumbnail~dark@2x.png)

![Apple image 87 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 88 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 89 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-typography-thumbnail@2x.png)

![Apple image 90 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-typography-thumbnail~dark@2x.png)

![Apple image 91 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 92 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/layout.svg)

![Apple image 93 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 94 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

![Apple image 95 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/system.svg)

![Apple image 96 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/typography.svg)

</details>
