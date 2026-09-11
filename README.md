# AiAgent.Skill.SoftwareDevelopment

`software-development` is an agent skill for deciding what to explore,
what to make dependable, and what to simplify in software engineering.
It supplies judgment principles rather than a prescribed workflow.

The complete skill lives in one [SKILL.md](src/skills/software-development/SKILL.md).
Its name remains `software-development`; no supporting reference files are
required to use it.

## What it contributes

The skill helps distinguish intended meaning, observed behavior, chosen
policy, and commitments that others depend on. These distinctions matter
when a specification is incomplete, when an integration's behavior is
uncertain, or when simplifying an established system.

It complements product requirements and project obligations. An observation
can establish what happens; an authorized decision can establish what should
happen. Neither alone proves that the implementation fulfills its promises.

## Three modes

| Mode | Engineering objective |
| --- | --- |
| Bootstrap | Learn while the capability's purpose or meaning remains uncertain. |
| Harden | Give established meaning a dependable expression. |
| Distill | Simplify that expression while preserving the duties it carries. |

Modes apply to capabilities and current changes, not whole projects. They
are not a mandatory sequence. A routine edit needs no stage ceremony, and
a mode does not enlarge the user's task or authorize additional actions.

The shared principles and mode descriptions are kept together so the agent
can apply them without navigating a separate policy tree. The
[rationale](src/RATIONALE.md) explains the design and its limitations; it is
background reading, not a prerequisite for every installation or task.

## Install

Ask an agent:

```text
Read and proceed:
https://github.com/pgsounds9006/AiAgent.Skill.SoftwareDevelopment/blob/main/src/INSTALL-SKILL.md
```

For an environment with native skill support, place the
`src/skills/software-development/` directory in its skill search path.
The [release archive](https://github.com/pgsounds9006/AiAgent.Skill.SoftwareDevelopment/releases/latest/download/software-development.skill)
contains the same folder with a single `SKILL.md`.

Installation, invocation, and usefulness are separate things to check.
Confirm placement and discovery using the environment's supported mechanism;
check invocation when needed; evaluate usefulness through relevant work.
Add an environment-specific pointer only to address an identified integration
gap. Repeating the skill in other settings creates another copy to maintain.

## Codex plugin

The `src/` directory is also a Codex plugin. Its `.codex-plugin/plugin.json`
points to `skills/`, so both installations use the same source file.

A Codex marketplace can reference this repository with this entry:

```json
{
  "name": "software-development",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/pgsounds9006/AiAgent.Skill.SoftwareDevelopment.git",
    "path": "./src",
    "ref": "main"
  },
  "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
  "category": "Productivity"
}
```

Install from the marketplace that lists it, then start a new Codex task
to use `software-development:software-development`.
When releasing a new skill version, update `src/.codex-plugin/plugin.json`
to match the version in `SKILL.md`. CI checks this agreement.

## Remove

Remove the installed `software-development` folder and any pointer added
specifically for it. Preserve unrelated configuration and project records.
The [installation guide](src/INSTALL-SKILL.md) describes these boundaries.

## Maintain and release

- [SKILL.md](src/skills/software-development/SKILL.md) contains the complete
  installed guidance and its release version.
- [INSTALL-SKILL.md](src/INSTALL-SKILL.md) covers placement and integration.
- [RATIONALE.md](src/RATIONALE.md) records the reasons behind the design.

Run `python scripts/package-skill.py` to build `software-development.skill`.
The archive contains only `software-development/SKILL.md`. The existing
`bash scripts/package-skill.sh` entry point calls the same packager.

CI checks the frontmatter, single-file structure, and package. A change to
`SKILL.md` on `main` creates a release when its `version` has no release yet;
bump that field when publishing a new skill revision. These checks establish
package integrity, not the quality of an agent's engineering decisions.
