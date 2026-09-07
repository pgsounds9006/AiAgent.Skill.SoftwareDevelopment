# Rationale

This document explains the design choices behind
[software-development](skills/software-development/SKILL.md). It is background
for evaluating or changing the skill, not another set of runtime instructions.

## Principles rather than prescriptions

The skill should improve judgment across different systems without specifying
their implementation in advance. It therefore retains distinctions that
change decisions: hypothesis and evidence, intended and demonstrated meaning,
policy and external fact, authority and representation, lasting requirements
and temporary accommodations.

Examples, fixed sequences, and absolute mode permissions can make guidance
easy to follow while narrowing it to the situations its author imagined.
The loaded text instead describes what to consider and what an outcome must
preserve. This is a design choice, not a claim that examples or procedures are
generally unhelpful. More concrete guidance would need to earn its place through
a demonstrated ambiguity or failure.

## Why three modes

Exploration, protection, and simplification call for different judgments.
Capability maturity helps distinguish them without imposing a project-wide
lifecycle. Bootstrap, Harden, and Distill describe the objective of a change
in relation to what is known and already relied on.

Maturity is useful evidence, not the only consideration. Consequences,
dependencies, requirements, and scope still matter. A new uncertainty need
not reopen every established guarantee. A gap discovered during simplification
may need protection before removal can be justified.

The intellectual influences include Kent Beck's 3X, Simon Wardley's
pioneers/settlers/town-planners, and Martin Fowler's distinction between public
and published interfaces. This skill uses its own judgment axis rather than
claiming those approaches have the same purpose. Compatibility and deliberate
contract retirement remain concerns that a mode label alone cannot settle.

## Requirements and evidence have different authority

A specification can establish an intended obligation before an implementation
exists. Observation can establish facts about existing behavior. Dependency
can create a compatibility obligation even around behavior nobody would choose
today. Keeping these distinct avoids treating accidental behavior as desired
policy, or treating an authored requirement as proof that it is fulfilled.

The skill complements specification work without prescribing how product
requirements are authored or how teams organize delivery. It does not grant
permission to change scope or disregard existing obligations.

## One installed file

The core principles, three modes, and guidance on preserving judgments fit in
one file. Separating these short sections would add navigation and maintenance
without enough selective-loading benefit. The single-file layout is a practical
choice at the current size, not a universal rule against supporting resources.

Installation guidance and this rationale have different purposes and remain
outside the installed package. A bridge, if needed, points to the skill rather
than maintaining an independent summary of it. Native loading needs no such
compensation when it already supplies the required integration.

## Proportionate integration and records

Installing a skill should not require an audit of every resident instruction
or a controlled engineering experiment. Placement and discovery can be checked
mechanically; uncertain invocation calls for a focused check. Investigation
expands when there is evidence of a wider problem.

Records preserve judgments that would otherwise be costly to recover. They
do not turn a subjective interpretation into an unquestionable fact. Routine
work need not produce new artifacts, while a persistent integration workaround
benefits from preserving its reason and the conditions for reconsidering it.

## Limits and evaluation

Abstract guidance can be repeated fluently without helping a decision. It can
also consume attention, encourage unnecessary analysis, or lead different
readers to different maturity judgments. Neither the kernel nor the modes are
immune to these failures.

Use actual outcomes and the task's requirements to assess the skill. A comparison
with and without it can provide evidence, but a changed conclusion is neither
necessary nor sufficient for improvement. Consider correctness, the basis for
commitments, preserved obligations, and effort spent. One run does not establish
a general performance claim.

Revisit the design when useful distinctions repeatedly fail to affect judgment,
mode interpretations become unstable, or the guidance adds more burden than
value. That evidence should drive revision rather than an assumed need for more
rules, more records, or a larger framework.
