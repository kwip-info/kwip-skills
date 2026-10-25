---
name: design-led-development
description: Design and implement user-facing tools or substantial workflow changes with reviewable interaction plans, meaningful TDD, compatibility checks and a finite hands-on checkpoint.
---

# Design-led development

Read the product contract, current design system, existing adjacent workflow and authorized task.
Update its current work record before implementation and at milestones/waits/closure. Use the
existing tracker or work file; capture only bounded status and evidence references.

Start from the user's job and the smallest complete workflow that delivers it. Identify required
inputs, configuration ownership, execution, outputs, failure/cancellation and persistence. Include
relevant accessibility, learning/help and automation clients rather than treating a new palette
entry or screen as a finished feature.

For a substantial new interaction, make the design concrete before implementation: a state/layout
proposal, mockup or prototype that follows the established controls. Use image generation when
requested or useful for visual exploration; label sample values and metrics as illustrative.
Resolve narrow layouts, invalid drafts, close/reopen and loading states in the review. Once the
user approves the direction, continue within that scope without another approval loop for routine
implementation choices. A small bug fix can reuse established patterns without inventing a new
design ceremony. Backend-only work needs a contract/interaction plan, not decorative mockups.

Keep configuration, results and instructions in their established places. Reuse standard viewers
and data types where they already express the output. Introduce a larger editor only when actual
configuration complexity justifies it. Preserve drafts, save/revert ownership, keyboard close and
responsive navigation; do not bury normal work under large instruction paragraphs.

Before changing behavior, define a finite acceptance slice and create a meaningful failing check
against the actual boundary. Then implement the smallest correction and run the relevant checks.
An assertion matching new wording is not behavioral proof. Preserve original failures; do not
invent a RED result after the implementation or weaken an independent oracle to make it pass.

Test the complete changed workflow with nondefault inputs and relevant negative cases. Include
real numerical, authority, export, restart and new-data reuse witnesses when they are part of the
feature. A fake callback or source test alone does not qualify a native picker or packaged app.
Keep immutable fixture bytes shareable, but mutable models, RNG and operation state private.

Check responsiveness while the intended work runs: navigation, live inspection, resize, cancel,
single-action close and menus as applicable. Distinguish an interaction round trip from frame-rate
or uncontended performance measurements. Do not claim responsiveness from a passing unit suite.

Update product guidance and lessons to match the actual state of the workflow and existing
projects. Record test scope, actual results, skips, native observations and limitations. Stop at
the requested review checkpoint, with a usable artifact or app state. A feature checkpoint does
not authorize a merge, release or publication; unrelated polish should not prolong accepted work.
