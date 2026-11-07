# Buttons

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/buttons) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/buttons.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Make the action clear through its label, visual emphasis, semantic role, and interaction feedback.
- Check platform target sizes and custom pressed states; reserve destructive semantics for actions that can remove data.

## Source section outline

- Best practices
- Style
- Content
- Role
- Platform considerations
- iOS, iPadOS
- macOS
- Push buttons
- Square buttons
- Help buttons
- Image buttons
- visionOS
- watchOS
- Resources
- Related
- Developer documentation
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/components-buttons-intro@2x.png)

<details>
<summary>All 51 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-buttons-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-buttons-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/buttons-roles-alert@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/buttons-roles-alert~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-activity-indicator-hidden@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-activity-indicator-hidden~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-activity-indicator-visible@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/button-activity-indicator-visible~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-button-state-idle@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-button-state-hover@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-button-state-selected@2x.png)

![Apple image 12 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-button-state-unavailable@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/table-availability-checkmark~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/buttons-watch-full-width@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/buttons-watch-toolbar-corners@2x.png)

![Apple image 17 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-alerts-thumbnail@2x.png)

![Apple image 18 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-alerts-thumbnail~dark@2x.png)

![Apple image 19 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-buttons-thumbnail@2x.png)

![Apple image 20 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-buttons-thumbnail~dark@2x.png)

![Apple image 21 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-labels-thumbnail@2x.png)

![Apple image 22 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-labels-thumbnail~dark@2x.png)

![Apple image 23 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-menus-and-actions-thumbnail@2x.png)

![Apple image 24 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-menus-and-actions-thumbnail~dark@2x.png)

![Apple image 25 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-ornaments-thumbnail@2x.png)

![Apple image 26 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-ornaments-thumbnail~dark@2x.png)

![Apple image 27 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-pop-up-buttons-thumbnail@2x.png)

![Apple image 28 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-pop-up-buttons-thumbnail~dark@2x.png)

![Apple image 29 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-pull-down-buttons-thumbnail@2x.png)

![Apple image 30 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-pull-down-buttons-thumbnail~dark@2x.png)

![Apple image 31 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-segmented-controls-thumbnail@2x.png)

![Apple image 32 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-segmented-controls-thumbnail~dark@2x.png)

![Apple image 33 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-sheets-thumbnail@2x.png)

![Apple image 34 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-sheets-thumbnail~dark@2x.png)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-toggles-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-toggles-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-toolbars-thumbnail@2x.png)

![Apple image 38 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-toolbars-thumbnail~dark@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components@2x.png)

![Apple image 40 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components~dark@2x.png)

![Apple image 41 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail@2x.png)

![Apple image 42 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-sf-symbols-thumbnail~dark@2x.png)

![Apple image 43 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/help.svg)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 45 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/menus-and-actions.svg)

![Apple image 46 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 47 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-offering-help-thumbnail@2x.png)

![Apple image 48 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-offering-help-thumbnail~dark@2x.png)

![Apple image 49 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sf-symbols.svg)

![Apple image 50 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-button-dwell-tooltip@2x.png)

![Apple image 51 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/visionos-button-styles-animation@2x.png)

</details>
