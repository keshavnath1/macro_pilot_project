# Legacy Migration: Understand First, Rewrite Second

Morgan Stanley's DevGen.AI example highlights a familiar problem: **before we can replace legacy code, we need to understand the business behavior inside it.** Writing the replacement is only part of the work.

## What Morgan Stanley Did

Morgan Stanley described using DevGen.AI to turn legacy code into plain-English specifications that engineers could use to build modern implementations. It also supported direct translation of smaller sections, but human judgment remained important: translated code is not automatically a well-designed replacement. [Morgan Stanley leadership interview, via WSJ](https://www.itiger.com/news/2540775365)

The basic idea is **legacy code → understandable specifications → modern implementation**. AI helps with reverse engineering; it does not remove the need to check what the old system actually does.

## Where SAS Agent Mastery Fits

SAS Agent Mastery follows the same understand-first principle, with an explicit path from requirements to validation:

| Step | What it answers | Skills |
|---|---|---|
| Agree the intent | What are we migrating, and what counts as success? | **Interview**, **Specify**, **Decide** |
| Reconstruct behavior | What does the SAS actually do? | **Trace**, **Map**, **Model** |
| Build and prove | Does the Python implementation preserve the agreed behavior? | **Generate**, **Test**, **Validate** |

**Trace**, **Map**, and **Model** are the closest match to the reverse-engineering work described for DevGen.AI. **Interview**, **Specify**, and **Decide** establish the migration intent; they do not replace investigation of the source behavior.

### The Canonical Skill Sequence

The repository's `config/workflow.yaml` organizes the lifecycle into five acts:

1. Align: **Interview** → **Specify** → **Decide**
2. Reuse and reconstruct: **Harvest** → **Import** *(optional reuse steps)* → **Trace** → **Map** → **Model**
3. Build and prove: **Generate** → **Test** → **Validate**
4. Adapt and operate: **Adapt** → **Ingest** → **Review** → **Release**
5. Improve: **Learn**

**Orchestrate** controls progression across this sequence: check the recorded state and prior gate, select one permitted skill, and stop at required human approvals. The sequence is not permission to execute every step in one uninterrupted run; runtime work and release claims must stay within the approved scope.

On failure, the recovery sequence is **Ingest** → **Diagnose** → **Repair** → **Review**, followed by re-running the earliest failed gate. Recovery is bounded to three attempts, with an earlier stop after two occurrences of the same failure without new evidence.

Learning is also governed: **Learn** prepares a proposal, **Review** independently checks it, and a human decides whether to promote it. A lesson does not automatically become a new standard.

For example, saying a SAS program “calculates probability of default” is not enough to reproduce it. We need to capture the event being scored, category reference levels, missing-value handling, and coefficient precision. The tie-out then compares Python results with approved reference outputs on an agreed population and tolerance.

**The agent produces artifacts and evidence. Humans review assumptions, approve the relevant decisions, and remain accountable for release.** A passing sample comparison supports that specific claim, not automatic production readiness.

This is a comparison of approaches, not a claim that our controls are stronger. The public DevGen.AI material does not describe its validation and approval mechanisms in enough detail to make that judgment.

## What We Can Claim Today

We are experimenting with **one module in the IARP model**. As we try more modules, mismatches and review feedback will help us improve the workflow.

Morgan Stanley's reported savings are useful context, not a forecast for our project. Reock's slide cites more than 280,000 hours annually; the June 2025 leadership interview describes 280,000 hours saved that year so far. Those different reporting periods should not be treated as a single benchmark. [Reock's presentation, slide 44](https://leaddev.com/wp-content/uploads/2025/10/Leadership-in-AI-Assisted-Engineering-Justin-Reock-LeadDev-New-York-2025.pdf)

To establish our own estimate, we need to measure preparation, hands-on effort, reviews, execution, and rework **through to an accepted tie-out**, against a comparable manual approach.

**Our takeaway: the opportunity is not just faster code generation. It is less effort understanding legacy behavior, with a traceable path to a verified replacement. We still need to measure the time savings.**
