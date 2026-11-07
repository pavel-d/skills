# Designing for iPhone Duo

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Preserve the current task when the device changes display configuration.
- Consult the current device article for display and transition guidance; avoid fixed-size assumptions that discard context.

## Source section outline

- Anatomy
- Device poses
- Best practices
- Dynamic layouts
- Reserved regions
- Split views
- Arrangement views
- Vertical controls
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-iphone-intro@2x.png)

<details>
<summary>All 71 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-iphone-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-iphone-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-hero-outside@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-hero-outside~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-hero-inside@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-hero-inside~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-device-layout-outer@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-device-layout-outer~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-device-layout-inner@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-device-layout-inner~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-poses@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-poses~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-mail-compact@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-mail-compact~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-mail-full@2x.png)

![Apple image 16 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-mail-full~dark@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-safe-area-outer-camera@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-safe-area-outer-camera~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-safe-area-inner-camera@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-safe-area-inner-camera~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-notes-sidebar-open@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-notes-sidebar-open~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-notes-sidebar-folded@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-notes-sidebar-folded~dark@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-view-layout-split@2x.png)

![Apple image 26 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-view-layout-split~dark@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-view-layout-overlay@2x.png)

![Apple image 28 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-view-layout-overlay~dark@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-tab-bar-toolbar-layout@2x.png)

![Apple image 30 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-tab-bar-toolbar-layout~dark@2x.png)

![Apple image 31 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-multitasking@2x.png)

![Apple image 32 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-multitasking~dark@2x.png)

![Apple image 33 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-calculator-full-screen@2x.png)

![Apple image 34 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-calculator-full-screen~dark@2x.png)

![Apple image 35 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-pane-controls@2x.png)

![Apple image 36 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-pane-controls~dark@2x.png)

![Apple image 37 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-compact-layout-tab-bar@2x.png)

![Apple image 38 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-compact-layout-tab-bar~dark@2x.png)

![Apple image 39 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-compact-layout-toolbar@2x.png)

![Apple image 40 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone-compact-layout-toolbar~dark@2x.png)

![Apple image 41 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/8/DC792262-D58D-41A5-9B4A-A13D311F69E1/11309_wide_250x141_1x.jpg)

![Apple image 42 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/8/DC792262-D58D-41A5-9B4A-A13D311F69E1/11309_wide_250x141_2x.jpg)

![Apple image 43 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/8/DC792262-D58D-41A5-9B4A-A13D311F69E1/11309_wide_250x141_3x.jpg)

![Apple image 44 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/8/E21064E2-BC9B-4D00-8713-4BDFAA05EA72/11313_wide_250x141_1x.jpg)

![Apple image 45 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/8/E21064E2-BC9B-4D00-8713-4BDFAA05EA72/11313_wide_250x141_2x.jpg)

![Apple image 46 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/8/E21064E2-BC9B-4D00-8713-4BDFAA05EA72/11313_wide_250x141_3x.jpg)

![Apple image 47 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/8/FB8AD507-3A1E-473D-ACFE-1B682C432928/11314_wide_250x141_1x.jpg)

![Apple image 48 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/8/FB8AD507-3A1E-473D-ACFE-1B682C432928/11314_wide_250x141_2x.jpg)

![Apple image 49 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/8/FB8AD507-3A1E-473D-ACFE-1B682C432928/11314_wide_250x141_3x.jpg)

![Apple image 50 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-split-views-thumbnail@2x.png)

![Apple image 51 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-split-views-thumbnail~dark@2x.png)

![Apple image 52 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-toolbars-thumbnail@2x.png)

![Apple image 53 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-toolbars-thumbnail~dark@2x.png)

![Apple image 54 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-games.svg)

![Apple image 55 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-iphone.svg)

![Apple image 56 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-layout-thumbnail@2x.png)

![Apple image 57 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-layout-thumbnail~dark@2x.png)

![Apple image 58 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 59 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ios.svg)

![Apple image 60 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/layout.svg)

![Apple image 61 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 62 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-games-thumbnail@2x.png)

![Apple image 63 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-games-thumbnail~dark@2x.png)

![Apple image 64 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-ios-thumbnail@2x.png)

![Apple image 65 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-ios-thumbnail~dark@2x.png)

![Apple image 66 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-iphone-thumbnail@2x.png)

![Apple image 67 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-iphone-thumbnail~dark@2x.png)

![Apple image 68 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms@2x.png)

![Apple image 69 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms~dark@2x.png)

![Apple image 70 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/preparing-your-app-for-iphone-duo-pageimage-card@2x.png)

![Apple image 71 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/preparing-your-app-for-iphone-duo-pageimage-card~dark@2x.png)

</details>
