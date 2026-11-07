# Game Center

[Apple HIG](https://developer.apple.com/design/human-interface-guidelines/game-center) · [Official full Markdown](https://developer.apple.com/design/human-interface-guidelines/game-center.md)

[Topic catalog](../catalog.md) · [Practical guidance](../practice.md)

## Design notes

Original application notes; consult Apple for the full guidance.

- Place system game access where it fits menu interaction without conflicting with game controls.
- Account for overlay presentation and use the provided artwork for relevant links.

## Source section outline

- Accessing Game Center
- Integrating the access point
- Using custom UI
- Achievements
- Integrating achievements into your game
- Creating achievement images
- Leaderboards
- Challenges
- Multiplayer activities
- Platform considerations
- tvOS
- watchOS
- Resources
- Related
- Developer documentation
- Videos
- Change log

## Image references

Apple-hosted images; copyright Apple. Variants are labeled with source traits.

![Apple article illustration](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Game-Center-intro@2x.png)

<details>
<summary>All 59 image references and variants</summary>

![Apple image 1 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Game-Center-intro@2x.png)

![Apple image 2 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-Game-Center-intro~dark@2x.png)

![Apple image 3 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-access-point-collapsed@2x.png)

![Apple image 4 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-game-overlay@2x.png)

![Apple image 5 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-game-overlay~dark@2x.png)

![Apple image 6 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-achievement-overlay@2x.png)

![Apple image 7 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-achievement-overlay-detail@2x.png)

![Apple image 8 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-achievement-anatomy@2x.png)

![Apple image 9 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-achievement-anatomy~dark@2x.png)

![Apple image 10 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/ios-achievement-image-layout@2x.png)

![Apple image 11 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/ios-achievement-image-layout~dark@2x.png)

![Apple image 12 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tvos-achievement-image-layout@2x.png)

![Apple image 13 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tvos-achievement-image-layout~dark@2x.png)

![Apple image 14 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-leaderboards-overlay@2x.png)

![Apple image 15 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-leaderboards-detail@2x.png)

![Apple image 16 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/leaderboard-image-layout-general@2x.png)

![Apple image 17 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/leaderboard-image-layout-general~dark@2x.png)

![Apple image 18 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tvos-multi-layered-leaderboard-image@2x.png)

![Apple image 19 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tvos-multi-layered-leaderboard-image~dark@2x.png)

![Apple image 20 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-challenges-overlay@2x.png)

![Apple image 21 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-challenges-overlay-detail@2x.png)

![Apple image 22 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-challenge-anatomy@2x.png)

![Apple image 23 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-challenge-anatomy~dark@2x.png)

![Apple image 24 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-challenge-image-specs@2x.png)

![Apple image 25 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-challenge-image-specs~dark@2x.png)

![Apple image 26 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-multiplayer-overlay@2x.png)

![Apple image 27 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-multiplayer-overlay-detail@2x.png)

![Apple image 28 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-multiplayer-custom-code@2x.png)

![Apple image 29 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-multiplayer-in-game-ui@2x.png)

![Apple image 30 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-multiplayer-anatomy@2x.png)

![Apple image 31 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-multiplayer-anatomy~dark@2x.png)

![Apple image 32 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-multiplayer-image-specs@2x.png)

![Apple image 33 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/games-multiplayer-image-specs~dark@2x.png)

![Apple image 34 (article; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/tvos-dashboard-image@2x.png)

![Apple image 35 (article; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/tvos-dashboard-image~dark@2x.png)

![Apple image 36 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/0BEC1E9E-5221-48F9-853B-BEDA2BE23D63/9892_wide_250x141_1x.jpg)

![Apple image 37 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/0BEC1E9E-5221-48F9-853B-BEDA2BE23D63/9892_wide_250x141_2x.jpg)

![Apple image 38 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/0BEC1E9E-5221-48F9-853B-BEDA2BE23D63/9892_wide_250x141_3x.jpg)

![Apple image 39 (related or metadata; 1x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/0C96EE37-E8A0-46DB-88B3-3BF6C3F633DD/9893_wide_250x141_1x.jpg)

![Apple image 40 (related or metadata; 2x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/0C96EE37-E8A0-46DB-88B3-3BF6C3F633DD/9893_wide_250x141_2x.jpg)

![Apple image 41 (related or metadata; 3x)](https://devimages-cdn.apple.com/wwdc-services/images/3055294D-836B-4513-B7B0-0BC5666246B0/0C96EE37-E8A0-46DB-88B3-3BF6C3F633DD/9893_wide_250x141_3x.jpg)

![Apple image 42 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.gamekit/creating-engaging-challenges-from-leaderboards-PageImage-card@2x.png)

![Apple image 43 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.gamekit/creating-engaging-challenges-from-leaderboards-PageImage-card~dark@2x.png)

![Apple image 44 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/designing-for-games.svg)

![Apple image 45 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/focus-and-selection.svg)

![Apple image 46 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-center.svg)

![Apple image 47 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/game-controls.svg)

![Apple image 48 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/human-interface-guidelines-page-image-card@2x.png)

![Apple image 49 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-focus-and-selection-thumbnail@2x.png)

![Apple image 50 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-focus-and-selection-thumbnail~dark@2x.png)

![Apple image 51 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-thumbnail@2x.png)

![Apple image 52 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/inputs-game-controls-thumbnail~dark@2x.png)

![Apple image 53 (related or metadata; 1x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/overview.svg)

![Apple image 54 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-games-thumbnail@2x.png)

![Apple image 55 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/platforms-designing-for-games-thumbnail~dark@2x.png)

![Apple image 56 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-game-center-thumbnail@2x.png)

![Apple image 57 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies-game-center-thumbnail~dark@2x.png)

![Apple image 58 (related or metadata; 2x, light)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies@2x.png)

![Apple image 59 (related or metadata; 2x, dark)](https://developer.apple.com/tutorials/images/com.apple.HIG/technologies~dark@2x.png)

</details>
