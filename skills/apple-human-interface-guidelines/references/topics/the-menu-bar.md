# The menu bar

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Integrate application commands with established Mac menu structure and keyboard equivalents.
- Keep the command organization stable so availability changes do not make menu locations unpredictable.

## Source section outline

- Anatomy
- Best practices
- App menu
- File menu
- Edit menu
- Format menu
- View menu
- App-specific menus
- Window menu
- Help menu
- Dynamic menu items
- Platform considerations
- iPadOS
- macOS
- Menu bar extras
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/components-the-menu-bar-intro@2x.png)

<details>
<summary>All 49 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-the-menu-bar-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-the-menu-bar-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/menu-bar-ipad-overview@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/menu-bar-ipad-overview~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/menu-bar-extras@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/menu-bar-extras~dark@2x.png)

![Apple image 7 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/873F40BE-101A-4C0D-99F0-F5C7CE7B47A3/10046_wide_250x141_1x.jpg)

![Apple image 8 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/873F40BE-101A-4C0D-99F0-F5C7CE7B47A3/10046_wide_250x141_2x.jpg)

![Apple image 9 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/873F40BE-101A-4C0D-99F0-F5C7CE7B47A3/10046_wide_250x141_3x.jpg)

![Apple image 10 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-dock-menus-thumbnail@2x.png)

![Apple image 11 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-dock-menus-thumbnail~dark@2x.png)

![Apple image 12 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-menus-and-actions-thumbnail@2x.png)

![Apple image 13 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-menus-and-actions-thumbnail~dark@2x.png)

![Apple image 14 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-menus-thumbnail@2x.png)

![Apple image 15 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-menus-thumbnail~dark@2x.png)

![Apple image 16 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-panels-thumbnail@2x.png)

![Apple image 17 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-panels-thumbnail~dark@2x.png)

![Apple image 18 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-popovers-thumbnail@2x.png)

![Apple image 19 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-popovers-thumbnail~dark@2x.png)

![Apple image 20 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-sidebars-thumbnail@2x.png)

![Apple image 21 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-sidebars-thumbnail~dark@2x.png)

![Apple image 22 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-status-bars-thumbnail@2x.png)

![Apple image 23 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-status-bars-thumbnail~dark@2x.png)

![Apple image 24 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-tab-bars-thumbnail@2x.png)

![Apple image 25 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-tab-bars-thumbnail~dark@2x.png)

![Apple image 26 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-the-menu-bar-thumbnail@2x.png)

![Apple image 27 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-the-menu-bar-thumbnail~dark@2x.png)

![Apple image 28 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-toolbars-thumbnail@2x.png)

![Apple image 29 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-toolbars-thumbnail~dark@2x.png)

![Apple image 30 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components@2x.png)

![Apple image 31 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components~dark@2x.png)

![Apple image 32 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-icons-thumbnail@2x.png)

![Apple image 33 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-icons-thumbnail~dark@2x.png)

![Apple image 34 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 35 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 36 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/going-full-screen.svg)

![Apple image 37 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/help.svg)

![Apple image 38 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 39 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/icons.svg)

![Apple image 40 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/menus-and-actions.svg)

![Apple image 41 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 42 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-going-full-screen-thumbnail@2x.png)

![Apple image 43 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-going-full-screen-thumbnail~dark@2x.png)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-offering-help-thumbnail@2x.png)

![Apple image 45 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-offering-help-thumbnail~dark@2x.png)

![Apple image 46 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-settings-thumbnail@2x.png)

![Apple image 47 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-settings-thumbnail~dark@2x.png)

![Apple image 48 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/settings.svg)

![Apple image 49 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

</details>
