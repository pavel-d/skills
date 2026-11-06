# Sign in with Apple

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Ask for authentication at a point where account value is clear.
- Use the system sign-in presentation and consider linking an existing account without creating unnecessary friction.

## Source section outline

- Offering Sign in with Apple
- Collecting data
- Displaying buttons
- Using the system-provided buttons
- White
- White with outline
- Black
- Button size and corner radius
- Creating a custom Sign in with Apple button
- Custom buttons with a logo and text
- Custom logo-only buttons
- Platform considerations
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-SIWA-intro@2x.png)

<details>
<summary>All 56 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-SIWA-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-SIWA-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/create-account-after-purchase@2x.png)

![Apple image 4 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/create-account-after-purchase~dark@2x.png)

![Apple image 5 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-sign-in-with@2x.png)

![Apple image 6 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-sign-in-with~dark@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-sign-up-with@2x.png)

![Apple image 8 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-sign-up-with~dark@2x.png)

![Apple image 9 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-continue-with@2x.png)

![Apple image 10 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-continue-with~dark@2x.png)

![Apple image 11 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-watch-44mm-no-background@2x.png)

![Apple image 12 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-white-yes@2x.png)

![Apple image 13 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/checkmark@2x.png)

![Apple image 14 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-white-no@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/crossout@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-outline-yes@2x.png)

![Apple image 17 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-outline-no@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-black-yes@2x.png)

![Apple image 19 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-black-no@2x.png)

![Apple image 20 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-watch-44mm@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-minimum-corner-radii@2x.png)

![Apple image 22 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-minimum-corner-radii~dark@2x.png)

![Apple image 23 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-default-corner-radii@2x.png)

![Apple image 24 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-default-corner-radii~dark@2x.png)

![Apple image 25 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-maximum-corner-radii@2x.png)

![Apple image 26 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/apple-account-maximum-corner-radii~dark@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/custom-sign-in-screens@2x.png)

![Apple image 28 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/custom-sign-in-screens~dark@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/siwa-black-logo-only@2x.png)

![Apple image 30 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/siwa-white-logo-only@2x.png)

![Apple image 31 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/left-aligned-correct-proportions-2@2x.png)

![Apple image 32 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/left-aligned-correct-proportions-2~dark@2x.png)

![Apple image 33 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/left-aligned-correct-proportions-1@2x.png)

![Apple image 34 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/left-aligned-correct-proportions-1~dark@2x.png)

![Apple image 35 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/siwa-logo-masked-rounded-rect@2x.png)

![Apple image 36 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/siwa-logo-masked-rounded-rect~dark@2x.png)

![Apple image 37 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/siwa-logo-default@2x.png)

![Apple image 38 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/siwa-logo-default~dark@2x.png)

![Apple image 39 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/siwa-logo-masked-circle@2x.png)

![Apple image 40 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/siwa-logo-masked-circle~dark@2x.png)

![Apple image 41 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/119/AB014534-6C60-4B00-9D7D-E2EDD02E3D6E/5211_wide_250x141_1x.jpg)

![Apple image 42 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/119/AB014534-6C60-4B00-9D7D-E2EDD02E3D6E/5211_wide_250x141_2x.jpg)

![Apple image 43 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/119/AB014534-6C60-4B00-9D7D-E2EDD02E3D6E/5211_wide_250x141_3x.jpg)

![Apple image 44 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/119/B671AE75-5224-4AA1-BB31-F4CBA7E95342/5002_wide_250x141_1x.jpg)

![Apple image 45 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/119/B671AE75-5224-4AA1-BB31-F4CBA7E95342/5002_wide_250x141_2x.jpg)

![Apple image 46 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/119/B671AE75-5224-4AA1-BB31-F4CBA7E95342/5002_wide_250x141_3x.jpg)

![Apple image 47 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/48/D792218F-60EA-427D-8034-204243D383C7/2645_wide_250x141_1x.jpg)

![Apple image 48 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/48/D792218F-60EA-427D-8034-204243D383C7/2645_wide_250x141_2x.jpg)

![Apple image 49 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/48/D792218F-60EA-427D-8034-204243D383C7/2645_wide_250x141_3x.jpg)

![Apple image 50 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 51 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 52 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/sign-in-with-apple.svg)

![Apple image 53 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-sign-in-with-apple-thumbnail@2x.png)

![Apple image 54 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-sign-in-with-apple-thumbnail~dark@2x.png)

![Apple image 55 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 56 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

</details>
