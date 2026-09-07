# Install software-development

Make the skill available through the agent environment's supported loading
mechanism. Keep the installation proportionate to the integration work
actually needed. Placement, invocation, and usefulness are separate claims;
report only what has been checked.

## Place the skill

Read [SKILL.md](skills/software-development/SKILL.md) and use the environment's
documented skill location. The complete installed package is the
`software-development` directory containing that single file.

Use `skills/software-development/` from this repository, or unpack the
[release archive](https://github.com/pgsounds9006/AiAgent.Framework.SDD/releases/latest/download/software-development.skill).
The latest-release address changes with new releases; use a specific release
or commit when a reproducible source matters. The release version is in the
skill's frontmatter.

When updating an existing installation, account for local customizations and
remove only obsolete files belonging to the replaced package. Older versions
included reference files; this version contains all guidance in `SKILL.md`.
The [rationale](RATIONALE.md) is optional background for understanding or
changing the design and is not part of the installed package.

## Check integration at the relevant scope

Use the environment's discovery or loading evidence to check placement.
Where invocation remains uncertain, inspect a relevant task or run a focused
check. If a fresh session is needed, distinguish successful placement from
invocation that has not yet been checked; do not turn a routine installation
into an unrelated engineering assignment.

Inspect configuration that plausibly affects this skill. Expand the inquiry
when a finding warrants it, rather than surveying every installed instruction.
Agreement with existing guidance is not itself a fault. A routing gap or an
unresolved conflict may need attention; use the environment's existing
instruction hierarchy before adding another rule.

## Add a bridge only for an identified gap

Prefer native loading. If that is unavailable or an integration problem is
established, add the smallest pointer the environment supports. The pointer
owns when and where to consult the skill; `SKILL.md` owns its meaning.

Derive the trigger from the skill's description and point to `SKILL.md`.
Keep substantive guidance out of the pointer. It creates no new authority
over the environment's policies, project obligations, or user instructions.
Do not rewrite unrelated settings or other skills to accommodate it.

Keep enough context to explain why a bridge exists, where its source lives,
and what would justify changing or removing it. If source text must be copied
because the environment cannot consult a file, identify the copy's source
revision and how it will be refreshed or retired.

## Assess usefulness separately

Verify a bridge against the integration gap it addresses. A task that loads
the skill establishes invocation, not improved judgment. Small tasks should
remain small whether or not the environment loads the skill.

A with/without comparison can help investigate usefulness when that question
matters. Judge outcomes against the task's requirements and evidence, including
unnecessary effort. Different conclusions do not prove improvement, and equal
conclusions do not prove the skill added no value. A single comparison is
limited evidence rather than an installation gate.

Record findings when a persistent bridge, costly judgment, or project
requirement makes them useful. Routine checks can be reported briefly without
creating a new permanent record. State any material verification still missing.

## Remove

Remove the installed skill and the integration elements added specifically
for it. Preserve unrelated configuration, local work, and project records.
