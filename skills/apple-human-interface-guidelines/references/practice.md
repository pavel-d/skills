# Applying Apple's design guidance

These are original application notes based on the linked HIG topics. They help select the right
questions and references; Apple's complete articles contain additional rules and exceptions.

## Establish the platform contract

Start with the task and platform, not a screenshot to reproduce. An iPhone prioritizes reachable
touch interactions; iPad accommodates resizing, multiple windows, and multiple inputs; Mac apps
participate in keyboard, menu, window, and document workflows. TV interfaces need legibility at a
distance and predictable remote focus. Watch interfaces need brief, glanceable interactions.
Spatial interfaces require attention to viewing comfort, surroundings, and immersion transitions.
Read each relevant platform article in [Getting started](topics/getting-started.md).

Share the underlying task model across platforms while adapting its presentation. Do not copy an
iPhone navigation arrangement into a Mac window without checking whether a sidebar, split view,
toolbar, menu, or inspector better supports that work. Current platform guidance also includes
devices with changing display configurations; consult the relevant article instead of encoding
assumptions about a fixed device width. See [layout](topics/layout.md),
[multitasking](topics/multitasking.md), and [windows](topics/windows.md).

## Establish hierarchy before adding visual effects

Give the primary task and content a clear place. Use alignment and grouping to express structure,
with progressive disclosure for secondary detail. Evaluate window resizing, larger accessibility
text, localization, keyboard presentation, and safe areas before choosing fixed dimensions.
Start with platform text styles, semantic colors, and system controls. Brand expression should
reinforce the product's identity while leaving controls recognizable. See
[layout](topics/layout.md), [typography](topics/typography.md), and [branding](topics/branding.md).

Treat material as a signal of interface structure. Apple's current material guidance distinguishes
the layer containing controls and navigation from the content layer. Check when Liquid Glass is
appropriate rather than applying transparency to every surface. Assess readable content behind
controls in both appearances and with accessibility settings. Do not freeze implementation choices
to a particular screenshot's blur or color. See [materials](topics/materials.md),
[color](topics/color.md), and [Dark Mode](topics/dark-mode.md).

## Select components by their meaning

| User need                           | Starting point                                                                                             | Design question                                                          |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Move among primary destinations     | [Tab bars](topics/tab-bars.md), [sidebars](topics/sidebars.md)                                             | Is the selection a location in the app?                                  |
| Show hierarchy and detail together  | [Split views](topics/split-views.md), [outline views](topics/outline-views.md)                             | What remains selected as space changes?                                  |
| Run an immediate action             | [Buttons](topics/buttons.md), [toolbars](topics/toolbars.md)                                               | Is the label, prominence, and role clear?                                |
| Choose a value                      | [Pickers](topics/pickers.md), [pop-up buttons](topics/pop-up-buttons.md)                                   | How many choices exist, and must they remain visible?                    |
| Change a binary state               | [Toggles](topics/toggles.md)                                                                               | Is the affected setting and current state obvious?                       |
| Choose among a few related options  | [Segmented controls](topics/segmented-controls.md)                                                         | Is the grouping coherent and compact?                                    |
| Offer contextual commands           | [Context menus](topics/context-menus.md), [pull-down buttons](topics/pull-down-buttons.md)                 | Can people also discover essential commands elsewhere?                   |
| Complete a short temporary task     | [Sheets](topics/sheets.md), [popovers](topics/popovers.md)                                                 | Is interruption justified, and is dismissal safe?                        |
| Resolve a critical decision         | [Alerts](topics/alerts.md)                                                                                 | Does this require interruption rather than inline feedback?              |
| Convey ongoing work                 | [Progress indicators](topics/progress-indicators.md)                                                       | Is progress measurable, and can work continue?                           |
| Present information outside the app | [Widgets](topics/widgets.md), [Live Activities](topics/live-activities.md), [controls](topics/controls.md) | Is this glanceable information, a bounded event, or an immediate action? |

These are starting points, not interchangeable styles. A navigation destination should remain
navigation; a command menu should not masquerade as a value picker. The exact platform-specific
presentation belongs to the relevant component article.

## Design the state transitions

Launch into useful content and restore relevant context. Teach unfamiliar interactions when they
are needed. Account creation, permission requests, rating prompts, and setup should appear at a
moment that explains their value, with alternatives where the task permits them. See
[launching](topics/launching.md), [onboarding](topics/onboarding.md),
[managing accounts](topics/managing-accounts.md), and [privacy](topics/privacy.md).

For each task, identify what the person sees while work is pending, how success becomes visible,
and how errors can be resolved. Keep existing useful content available during a refresh when the
task permits it. Pick a progress representation that reflects what is actually known. Do not claim
a percentage without measurable progress. Account for cancellation and preserve entered work.
See [loading](topics/loading.md), [feedback](topics/feedback.md), and
[progress indicators](topics/progress-indicators.md).

Use reversible actions and clear undo history where the task supports them. When loss is
unexpected and irreversible, make its consequence explicit before commitment. Avoid asking people
to confirm routine reversible steps. A modal task needs a clear completion or cancellation path
and should return people to an understandable context. See [undo and redo](topics/undo-and-redo.md),
[modality](topics/modality.md), [alerts](topics/alerts.md), and [sheets](topics/sheets.md).

## Make input and accessibility part of the interaction

Use system interaction conventions so that people can transfer existing skills. Check focus order,
keyboard shortcuts, pointer behavior, gesture alternatives, and how the interface works when a
person cannot perform a particular gesture. On TV and spatial platforms, verify the focus or
targeting model with the actual interaction methods. See [inputs](topics/inputs.md),
[keyboards](topics/keyboards.md), and [focus and selection](topics/focus-and-selection.md).

Accessibility review needs more than accessible names. Check logical reading order, meaningful
labels and values, adjustable text, contrast, motion alternatives, reachable targets, and whether
meaning survives without color, sound, or haptics alone. Test important workflows with the relevant
assistive technology when available. An implementation inspection cannot establish that VoiceOver
navigation or device targeting works. See [accessibility](topics/accessibility.md),
[VoiceOver](topics/voiceover.md), and [motion](topics/motion.md).

Use semantic direction and test right-to-left layouts. Text, numeric content, directional symbols,
and time sequences do not all mirror in the same way. Include longer localized labels in layout
checks rather than assuming the English design will fit. See [right to left](topics/right-to-left.md),
[writing](topics/writing.md), and [inclusion](topics/inclusion.md).

## Integrate with the system deliberately

Prefer existing system experiences for sharing, printing, authentication, payment, file handling,
and media playback when they support the task. Their recognizable interfaces carry expectations
about scope, permissions, and results. HIG recommendations describe presentation and interaction;
verify technical requirements in the corresponding developer documentation. See
[technologies](topics/technologies.md) and [system experiences](topics/system-experiences.md).

Treat sensitive data and AI-generated output as explicit design considerations. Explain access
requests at the relevant moment, minimize disclosure on glanceable surfaces, and give people a way
to understand and control generative features. Do not silently send personal content elsewhere as
part of an interface enhancement. See [privacy](topics/privacy.md),
[generative AI](topics/generative-ai.md), and [Always On](topics/always-on.md).

## Review and communicate evidence

For a finding, state the concrete task, observed behavior and location, practical consequence,
relevant official HIG link, and proposed correction. Distinguish an observed accessibility failure
from an untested risk. Identify whether a recommendation comes from Apple's guidance or your own
judgment. Describe applicable exceptions and deployment-version constraints.

A useful handoff says which platforms, window sizes, appearances, input methods, and accessibility
flows were exercised. Do not describe a screenshot review as device testing or a source-code change
as proof that the interaction now works.
