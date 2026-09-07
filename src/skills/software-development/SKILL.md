---
name: software-development
version: 0.2.0
description: >
  Software engineering guided by evidence, commitments, and capability
  maturity. Use for implementation, debugging, and refactoring to decide
  what to explore, what to make dependable, and what to simplify.
---

# Software Development

Software brings intent, behavior, contracts, and implementation into
agreement. Good engineering keeps their differences visible until the
evidence and decisions justify closing them.

## Kernel

**Treat diagnoses as hypotheses, regardless of their source.**
Confidence and authority do not establish a cause. Ask what would confirm
or refute an explanation, and distinguish what the evidence shows from
what it merely permits. Question the assumptions behind an apparent
success as readily as those behind a failure.

**Distinguish intended meaning from demonstrated behavior.**
A declaration can establish an obligation; it cannot prove that the system
fulfills it. Keep requirements, observations, and unresolved assumptions
distinct when making or evaluating a guarantee.

**Ground commitments without freezing exploration.**
Provisional choices need room to change. When a choice becomes something
others rely on, its basis matters: distinguish an observed constraint from
a chosen policy. Do not let a convenient assumption acquire the appearance
of an external fact.

**Place authority where the meaning and its rate of change belong.**
A fact needs an authoritative home appropriate to its scope and lifetime.
Multiple expressions can serve different readers or duties; competing
definitions create drift. Separate information by what governs it, not
merely by how it is currently written.

**Preserve the duties an expression carries.**
Behavior is not the only thing a system must sustain. Declared project
obligations and operational needs also give artifacts a purpose.
Documentation earns its place by adding understanding or fulfilling a
duty, especially where sound inference would otherwise mislead.

**Technical risk and product importance are separate judgments.**
Difficulty does not diminish value. An important but fragile capability
calls for stronger evidence and assurance, not a lower estimate of its
importance merely because it is difficult to support.

**Judge reversibility by dependency, not sunk effort.**
An extensive internal experiment may remain cheap to replace. A small
promise can become costly to change once others depend on it. Let that
boundary shape how freely to explore and how carefully to commit.

**Separate lasting meaning from temporary compensation.**
Domain truths and accommodations for present limitations have different
lifetimes. Keep accommodations removable and their reasons recognizable,
so they can be reconsidered when those reasons change. Avoid turning a
current limitation into a permanent ceiling.

## Stage awareness

Maturity belongs to the capability being changed, not to the repository as
a whole. Choose the approach from its purpose, existing commitments, and
available evidence. The three modes are lenses for judgment, not a fixed
sequence or an obligation to classify every small edit.

- **Bootstrap**: purpose or meaning is uncertain. Learn while
  keeping commitments revisable.
- **Harden**: intended or validated meaning is established, but
  dependable guarantees are incomplete. Bring promises and behavior into
  agreement.
- **Distill**: meaning is established and sufficiently protected.
  Reduce the cost of expressing it without losing what matters.

These judgments can differ within a single task. Change the approach when
the evidence warrants it; missing protection does not erase established
meaning, and a new uncertainty does not invalidate existing commitments.
Completion concerns the capability and scope under consideration, not an
idealized final state of the whole system.

### Bootstrap

Purpose: discover what an uncertain capability should mean through a
working candidate whose commitments remain easy to revise.

**Judgment**

Minimize premature promises, not necessarily implementation size. The
useful question is what the candidate can teach and what would justify
accepting, revising, or rejecting it.

Distinguish an unnecessary capability from one whose right form is not yet
known. The latter calls for deferred commitment, not dismissal. Prefer
forms that let evidence change the design without carrying speculative
assumptions into lasting contracts.

Exploration still carries responsibility for its actual effects and any
existing dependencies. Experimental status is not evidence that a change
is inconsequential.

**Completion**

The work has served its purpose when it resolves the uncertainty relevant
to the task, or makes the remaining uncertainty explicit. Hardening becomes
appropriate when enough meaning is established to support dependable
commitments. A candidate need not become permanent to have been useful.

### Harden

Purpose: give established meaning a dependable expression at the layer
best able to uphold it.

**Judgment**

Distinguish making a guarantee dependable from adding robustness without
a demonstrated need. Requirements can establish what must hold; evidence
establishes whether and under what conditions it does hold.

Prefer an existing expression of the intended meaning when it fits. Put
each guarantee where it can be sustained most reliably, rather than where
it happens to be easiest to describe. Separate semantic obligations from
strategies that may change independently.

Growth is justified when it closes a real gap between the promise and the
system. The strength of verification should match both the consequence of
being wrong and the uncertainty that remains.

Consolidate superseded definitions as stronger ones take effect. Useful
explanations and independent duties may remain; duplication is a problem
when authority competes, not merely when the same subject appears twice.

**Completion**

The relevant commitments are explicit, upheld, and supported by evidence
appropriate to their consequences. Remaining uncertainty is visible.
Further additions need their own justification rather than momentum from
the hardening effort.

### Distill

Purpose: express established meaning with less unnecessary structure.

**Judgment**

Before removing or reshaping an element, understand what duty it carries
and how that duty survives. Familiarity is not sufficient reason to keep
something; apparent redundancy is not sufficient reason to remove it.

Judge simplicity by the clarity and coherence of the resulting system,
not by size alone. Structure that explains present meaning can earn its
place. Structure whose reason has disappeared can obscure that meaning.

Equivalence includes the commitments and operational qualities that
matter, not just the behavior easiest to observe. If their protection is
insufficient, strengthen the basis for judgment before relying on removal.
Temporary growth can support a simpler result.

Simplification preserves meaning; a deliberate change of meaning needs to
be recognized and evaluated as such rather than hidden inside cleanup.

**Completion**

Stop when further reduction would weaken understanding, an established
guarantee, or a necessary responsibility. The objective is the least
expression that serves the system well, not the least expression possible.

## Capability State

A stage record preserves a judgment and its evidence, not an instruction
that overrides reality. Use it when reconstructing that judgment would be
costly, or when the project requires a record. Routine edits need not
produce one.

Keep the record with the project and follow its existing convention. Where
no convention exists, `CAPABILITIES.md` is an optional home. Preserve the
capability, the judgment, its non-obvious basis, and what would warrant
reconsideration; the exact format is secondary.

Treat a recorded stage as revisable. When current evidence conflicts with
it, resolve the conflict and update the judgment. Preserve useful changes
in understanding rather than a narration of activity or a second copy of
facts already clear elsewhere.
