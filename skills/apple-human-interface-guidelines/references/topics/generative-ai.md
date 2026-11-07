# Generative AI

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/generative-ai.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Give people meaningful control over generative features and set understandable expectations for their results.
- Evaluate inclusion, responsibility, and usefulness in the actual task rather than adding generation without a clear purpose.

## Source section outline

- Best practices
- Transparency
- Privacy
- Models and datasets
- Inputs
- Outputs
- Continuous improvement
- Platform considerations
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-generative-ai-intro@2x.png)

<details>
<summary>All 37 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-generative-ai-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-generative-ai-intro~dark@2x.png)

![Apple image 3 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/143DC470-4893-4DDE-AADA-2BEEFD879C9D/10764_wide_250x141_1x.jpg)

![Apple image 4 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/143DC470-4893-4DDE-AADA-2BEEFD879C9D/10764_wide_250x141_2x.jpg)

![Apple image 5 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/143DC470-4893-4DDE-AADA-2BEEFD879C9D/10764_wide_250x141_3x.jpg)

![Apple image 6 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/6F92E66E-52A5-4289-9F76-A3E6983F9250/10049_wide_250x141_1x.jpg)

![Apple image 7 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/6F92E66E-52A5-4289-9F76-A3E6983F9250/10049_wide_250x141_2x.jpg)

![Apple image 8 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/6F92E66E-52A5-4289-9F76-A3E6983F9250/10049_wide_250x141_3x.jpg)

![Apple image 9 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/Apple-Intelligence-Machine_Learning_overview-PageImage-card@2x.png)

![Apple image 10 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.TechnologyOverviews/Apple-Intelligence-Machine_Learning_overview-PageImage-card~dark@2x.png)

![Apple image 11 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/B8C03E29-6A50-4550-B592-3E1FD6C3C5C8/10738_wide_250x141_1x.jpg)

![Apple image 12 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/B8C03E29-6A50-4550-B592-3E1FD6C3C5C8/10738_wide_250x141_2x.jpg)

![Apple image 13 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/9B2E82C5-4DDF-4B9A-9459-328D8E297696/B8C03E29-6A50-4550-B592-3E1FD6C3C5C8/10738_wide_250x141_3x.jpg)

![Apple image 14 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/accessibility.svg)

![Apple image 15 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.foundationmodels/foundation-models-framework-landing-PageImage-card@2x.png)

![Apple image 16 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.foundationmodels/foundation-models-framework-landing-PageImage-card~dark@2x.png)

![Apple image 17 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail@2x.png)

![Apple image 18 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-accessibility-thumbnail~dark@2x.png)

![Apple image 19 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-inclusion-thumbnail@2x.png)

![Apple image 20 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-inclusion-thumbnail~dark@2x.png)

![Apple image 21 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-privacy-thumbnail@2x.png)

![Apple image 22 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/foundations-privacy-thumbnail~dark@2x.png)

![Apple image 23 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/generative-ai.svg)

![Apple image 24 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 25 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inclusion.svg)

![Apple image 26 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/loading.svg)

![Apple image 27 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/machine-learning.svg)

![Apple image 28 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 29 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-loading-thumbnail@2x.png)

![Apple image 30 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/patterns-loading-thumbnail~dark@2x.png)

![Apple image 31 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/privacy.svg)

![Apple image 32 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-generative-ai-thumbnail@2x.png)

![Apple image 33 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-generative-ai-thumbnail~dark@2x.png)

![Apple image 34 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-machine-learning-thumbnail@2x.png)

![Apple image 35 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-machine-learning-thumbnail~dark@2x.png)

![Apple image 36 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 37 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

</details>
