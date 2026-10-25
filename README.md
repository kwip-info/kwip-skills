# KWIP Skills

Reusable agent workflows for building software deliberately: clear workspace ownership,
design review, meaningful TDD, replaceable components and verification that respects scope.

These are instructions, not an execution engine or a claim of achieved test timings.
Adapt them to a repository's actual contracts, tools, budget and user authorization.

| Skill | Use it for |
|---|---|
| [workspace-operations](skills/workspace-operations/SKILL.md) | Coordinating repositories, documentation and organizational decisions |
| [design-led-development](skills/design-led-development/SKILL.md) | Reviewing a design, then implementing and testing the intended workflow |
| [component-boundaries](skills/component-boundaries/SKILL.md) | Incremental replaceable architecture and smaller change impact |
| [verification-strategy](skills/verification-strategy/SKILL.md) | Test-cost analysis, resource isolation and evidence-backed qualification |
| [bounded-work-tracking](skills/bounded-work-tracking/SKILL.md) | Accurate tickets, milestones and privacy-preserving activity |

Install the selected skill directories through your agent's skill installer, or put them in
its configured skills directory. Each contains a standard `SKILL.md` entrypoint. They can
be used independently; installing this collection does not install a tracker, start a service,
configure hooks, grant access or authorize publication.

Keep a separate **private workspace adapter** for repository locations, owners, product contracts,
design tokens, tracker connections, deployment instructions and organization-specific policies.
The generic workflows should not need company identifiers or credentials to be useful. The
organization's own instructions and the user's scope remain authoritative.

## Validate or contribute

Run `python3 scripts/validate_publication.py` and
`python3 -m unittest discover -s tests -q`. The publication check accepts only reviewed package
paths and rejects common private-path, credential and binary leakage. It supplements a human
content/history review; pattern matching is not proof that a document is safe to publish.

Use synthetic examples. Do not submit company exports, real tickets, logs, datasets, credentials,
screenshots of private work or existing private Git history. New workflow advice should describe
the decision it improves and its limits, rather than add a universal rule for one incident.

MIT licensed. Copyright 2026 KWIP LLC.
