# HomeKit

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/homekit) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/homekit.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Represent homes, rooms, and accessories consistently with the system model.
- Support multiple homes and related accessory details without duplicating system home settings.

## Source section outline

- Terminology and layout
- Homes
- Rooms
- Accessories, services, and characteristics
- Actions and scenes
- Automations
- Zones
- Setup
- Help people choose useful names
- Siri interactions
- Custom functionality
- Cameras
- Using HomeKit icons
- Styles
- Black HomeKit icon
- White HomeKit icon
- Custom color HomeKit icon
- Referring to HomeKit
- Referencing HomeKit and the Home app
- Platform considerations
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-HomeKit-intro@2x.png)

<details>
<summary>All 36 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-HomeKit-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-HomeKit-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-glyph@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-glyph~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homeapp-icon@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/homeapp-icon~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-black-icon-set@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-white-icon-set@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-custom-color-icon-set@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-custom-color-icon-set~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-settings@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-settings~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-donot1@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-donot2@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-lights-right@2x.png)

![Apple image 18 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-lights-right~dark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-lights-wrong1@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-lights-wrong1~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-lights-wrong2@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-lights-wrong2~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-setup@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-setup~dark@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-apps@2x.png)

![Apple image 26 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit-apps~dark@2x.png)

![Apple image 27 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/119/8C81F0E7-2E4C-4F4F-82FE-A9EBC73A913D/5239_wide_250x141_1x.jpg)

![Apple image 28 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/119/8C81F0E7-2E4C-4F4F-82FE-A9EBC73A913D/5239_wide_250x141_2x.jpg)

![Apple image 29 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/119/8C81F0E7-2E4C-4F4F-82FE-A9EBC73A913D/5239_wide_250x141_3x.jpg)

![Apple image 30 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/homekit.svg)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 32 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-homekit-thumbnail@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-homekit-thumbnail~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

</details>
