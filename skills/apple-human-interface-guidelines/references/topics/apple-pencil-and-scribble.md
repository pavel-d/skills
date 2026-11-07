# Apple Pencil and Scribble

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Respond immediately and naturally to drawing or writing input.
- Honor the person's choices about Pencil and finger behavior and account for supported pressure or device interactions.

## Source section outline

- Best practices
- Hover
- Double tap
- Squeeze
- Barrel roll
- Scribble
- Custom drawing
- Platform considerations
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-apple-pencil-and-scribble-intro@2x.png)

<details>
<summary>All 48 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-apple-pencil-and-scribble-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-apple-pencil-and-scribble-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-altitude@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-altitude~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-pressure@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-pressure~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-azimuth@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-azimuth~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-controls-moved-right@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-controls-moved-right~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-controls-moved-left@2x.png)

![Apple image 12 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-controls-moved-left~dark@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-preview-small@2x.png)

![Apple image 14 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-preview-small~dark@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-preview-medium@2x.png)

![Apple image 17 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-preview-medium~dark@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-preview-large@2x.png)

![Apple image 20 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-preview-large~dark@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-scribble@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-scribble~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-undo-redo-buttons@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-undo-redo-buttons~dark@2x.png)

![Apple image 25 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/4C1F7C67-D2D9-437D-996E-09DE396732DC/10929_wide_250x141_1x.jpg)

![Apple image 26 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/4C1F7C67-D2D9-437D-996E-09DE396732DC/10929_wide_250x141_2x.jpg)

![Apple image 27 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/4C1F7C67-D2D9-437D-996E-09DE396732DC/10929_wide_250x141_3x.jpg)

![Apple image 28 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/6ED9BC5C-E7FF-430B-9BAF-AA46710565A4/10705_wide_250x141_1x.jpg)

![Apple image 29 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/6ED9BC5C-E7FF-430B-9BAF-AA46710565A4/10705_wide_250x141_2x.jpg)

![Apple image 30 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/6ED9BC5C-E7FF-430B-9BAF-AA46710565A4/10705_wide_250x141_3x.jpg)

![Apple image 31 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/BE1C66C1-9D8C-4EF7-BE9A-A36251A00B86/10006_wide_250x141_1x.jpg)

![Apple image 32 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/BE1C66C1-9D8C-4EF7-BE9A-A36251A00B86/10006_wide_250x141_2x.jpg)

![Apple image 33 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/BE1C66C1-9D8C-4EF7-BE9A-A36251A00B86/10006_wide_250x141_3x.jpg)

![Apple image 34 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-pencil-and-scribble.svg)

![Apple image 35 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-thumbnail@2x.png)

![Apple image 36 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/components-app-shortcuts-thumbnail~dark@2x.png)

![Apple image 37 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/data-entry.svg)

![Apple image 38 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 39 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-apple-pencil-and-scribble-thumbnail@2x.png)

![Apple image 40 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-apple-pencil-and-scribble-thumbnail~dark@2x.png)

![Apple image 41 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs@2x.png)

![Apple image 42 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs~dark@2x.png)

![Apple image 43 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 44 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-entering-data-thumbnail@2x.png)

![Apple image 45 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-entering-data-thumbnail~dark@2x.png)

![Apple image 46 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-undo-and-redo-thumbnail@2x.png)

![Apple image 47 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-undo-and-redo-thumbnail~dark@2x.png)

![Apple image 48 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/undo-and-redo.svg)

</details>
