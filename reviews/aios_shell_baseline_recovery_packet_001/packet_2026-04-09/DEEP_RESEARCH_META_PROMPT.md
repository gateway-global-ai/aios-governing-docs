# ChatGPT Deep Research meta prompt

Use the attached shell-baseline packet zip as the sole evidence package for this task.

## Role

You are performing a governance-aligned deep research and planning pass on the **AI OS shell baseline thin slice**.

Treat:

- `aios-governing-docs` as governing authority
- `ai-os-voice-interface` as implementation evidence

Do **not** treat current code as automatic authority. Do **not** invent doctrine that is not present in the governing package.

## Mission

Extract the current shell environment as-built, map it to governing doctrine, evaluate it against the required baseline operating-system capabilities, and recommend the smallest reviewable foundation artifact set needed before broader AI OS work proceeds.

## Required focus

Focus only on the shell baseline thin slice:

- shell entry and greeting
- new vs returning classification
- voice-first shell behavior
- command rail and menu systems
- shell state and separation of power
- account-related shell requirements
- document/file baseline requirements
- current schemas, routes, storage/state
- output artifacts and screen primitives
- dual-lane voice system expectations
- single-option and multi-option flow behavior

## Required boundaries

1. Separate **ratified doctrine**, **draft doctrine**, and **implementation evidence**.
2. Distinguish what already exists from what is implied or missing.
3. Do not propose broad platform redesign beyond the shell baseline.
4. Do not treat future tenant or marketplace work as part of this baseline.
5. If doctrine is insufficient, identify the narrowest doctrine delta required.

## Required deliverables

Return a report with these sections:

1. **Shell baseline verdict**
   - Is the current shell sufficient to serve as the baseline foundation if bounded, or is it still too incomplete?

2. **Doctrine-to-implementation map**
   - For each major shell surface, map governing anchors to current implementation evidence.

3. **Current shell extraction**
   - Describe the shell as-built today: controls, views, state, routes, schemas, storage, and operator/admin boundaries.

4. **Gap map against the 14 required baseline capabilities**
   - Mark each capability as present, partial, or missing.
   - Explain the exact blocker.

5. **Foundation artifact recommendation**
   - Define the minimum artifact set that should exist and be approved before any broader system work continues.

6. **Governance vehicle recommendation**
   - Answer whether this should remain a supporting packet or become a narrow addendum/amendment after review.

7. **Approval gate recommendation**
   - State the exact approval condition that should block or permit forward movement.

## Analytical method

- Start from governing docs first.
- Then inspect the shell implementation files.
- Then reconcile the packet inventories and gap map.
- Explicitly call out conflicts between doctrine and implementation.
- Prefer repo truth over speculation.

## Required tone

Be rigorous, specific, and architecture-aware.

Do not write marketing copy. Do not provide vague product advice. Produce a planning-quality report suitable for governance review.
