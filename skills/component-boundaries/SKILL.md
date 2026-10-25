---
name: component-boundaries
description: Plan and incrementally migrate an application toward replaceable components and platform-independent contracts while reducing the tested impact of localized fixes.
---

# Component boundaries

Treat this as two coupled outcomes: reduce unnecessary verification cost and contain changes
through real production boundaries. A faster monolith does not establish replaceability; moving
types into a package does not establish a smaller, trustworthy test scope.

Read current ownership, dependency and state maps, then record the authorized slice in the task
system. For each slice name the real user journey, interface, implementation, mutable state,
provider dependencies, compatibility rules, expected test saving and finite exit. Keep unfinished
acceptance visible across sessions rather than resetting it at a convenient code checkpoint.

Prefer a small production-used seam over a new general framework. Separate portable semantic
contracts from platform mechanisms such as files, permissions, process launch, secrets and GPU
admission. Make ownership, cancellation, revision and terminal outcomes explicit. Presentation,
automation and agents should call the same application authority rather than own parallel engines.

"Service-like" organization within one application does not require network microservices.
Start with replaceable modules/providers and one composition root. A dynamic plugin system,
another process protocol or separately deployed service needs its own demonstrated reason and
trust/lifecycle design. Avoid adding operational cost merely to express an interface.

Move the actual production call path through the contract. The current provider and an independent
reference provider should pass shared semantic conformance, with real OS/security witnesses kept
for their platform-specific obligations. A reference implementation is not proof of equivalent
filesystem security, native UI or another operating system.

Enforce boundaries through build/import rules and tests, not naming alone. The pure contract
target should not reach broad UI, platform authority or unrelated model execution. Pin the
helpers, formats, fixtures and runtime identities needed to interpret qualification evidence.
See [the boundary record](references/boundary-record.md) for the minimum useful evidence.

Assign every expensive test obligation to semantic, numerical, lifecycle or real integration
work. Remove repeated setup without removing its assertions: reading/corrupting a frozen artifact
does not normally require fresh training each time; training correctness still trains. Dense
lifecycle decisions should exercise the production state owner, not a disconnected fake model.
Retain cold discovery, transport, cancellation, broker and packaged-authority witnesses.

Demonstrate change containment before trusting evidence reuse. Rehearse an internal fix, a
contract/schema change, a shared helper/fixture change, provider drift and an unknown addition.
Each must either reach its actual consumer closure or refuse. Compare selected outcomes with a
complete fresh run; fewer selected tests alone are not proof that selection is correct.

For a frozen release, a payload/source correction creates a new qualified candidate. Unchanged
component evidence may be reused only under an adopted policy with verified identities; old
signed payloads and provider submission IDs must not be relabeled as a new artifact.

Roadmap later migrations around the proven seams, one complete journey per slice. Preserve
existing projects/history and rollback until the next contract proves compatibility. Claim
platform independence only after a real second-platform provider passes the relevant conformance.
