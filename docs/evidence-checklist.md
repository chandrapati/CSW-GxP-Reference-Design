# GxP (Annex 11 · 21 CFR Part 11) — CSW Evidence Checklist

A printable worklist for the evidence owner. For each item: **what** to export, **where** from in CSW, and the **cadence**. Tick as you collect; file exports to immutable storage (not screenshots taken during inspection week).

> Legend — 🟢 Direct · 🟠 Supporting · ⚪ Evidence Required *(supplied outside CSW)*. CSW evidence is an input to GxP control assurance, not an attestation.

> **Read the boundary first.** Everything below is evidence about the **segmentation control**. None of it is evidence about the GxP **record** — no ALCOA+ attributes, no electronic signatures, no application audit trail. Those come from the regulated application and its validation package.

---

## Phase 1 — Coverage (Days 1–10)

- [ ] Validated-system host list reconciled to **CSW Inventory** against the Validated System Inventory (VSI)
- [ ] Labels applied with validation status first: `gxp:validated | supporting | non-gxp | external-partner`, then `system:*`, `owner:*`, `env:*`
- [ ] CSW scope tree created with the four top-level scopes keyed on validation status
- [ ] **Cannot-instrument register** recorded (legacy instrument controllers, vendor appliances)
- [ ] **Export:** inventory CSV + agent-status view → `evidence/01-coverage/`

## Phase 2 — Baseline (Days 11–28)

- [ ] ADM running on the validated scope for ≥ 2 weeks, spanning a full batch or month-end cycle
- [ ] Unexpected flows documented — instrument-vendor remote support, CDMO/CRO paths, corporate-IT reach into validated systems
- [ ] System owners and QA signed the cluster-to-system mapping
- [ ] **Export:** ADM diagram + flow samples with process context → `evidence/02-baseline/`

## Phase 3 — Policy (Days 29–45)

- [ ] Default-deny posture defined for `GxP-Validated`
- [ ] The `Non-GxP-Corporate` → `GxP-Validated` boundary policy authored explicitly
- [ ] **Simulation** run ≥ 1 week; output attached to the change record as pre-implementation impact evidence (Annex 11 §10)
- [ ] Change tickets raised for every would-deny; exception register updated
- [ ] **Export:** policy export + simulation report → `evidence/03-policy/`

## Phase 4 — Operate (ongoing)

- [ ] Enforcement enabled; negative test recorded in **Denied Connections**
- [ ] Drift detection demonstrated against a deliberate out-of-band change (Annex 11 §12.2)
- [ ] NTP reachability from validated workloads confirmed (Annex 11 §9 time-source evidence)
- [ ] SIEM integration verified with sample events
- [ ] Periodic-evaluation pack assembled (Annex 11 §11)
- [ ] **Export:** enforcement view + evaluation pack → `evidence/04-operate/`

---

## Recurring evidence pack

| # | Evidence item | CSW location | Cadence | Collected |
|---|---|---|---|:--:|
| 1 | Validated-estate inventory with validation-status labels | Inventory → Export | Monthly, and before each periodic evaluation | ☐ |
| 2 | Validated-boundary policy export | Defend → Policy Workspaces | Quarterly + after each change | ☐ |
| 3 | Pre-implementation simulation output | Defend → Policy Analysis | Per change request | ☐ |
| 4 | Policy drift / out-of-sync report | Defend → Enforcement Status | Weekly | ☐ |
| 5 | Control-plane audit trail (scopes, policies, enforcement) | Manage → Audit Log | Quarterly | ☐ |
| 6 | Vulnerability + reachability on validated systems | Investigate → Vulnerability | Monthly | ☐ |
| 7 | Compensating-control register for deferred CVEs | Vulnerability export + matching policy export | Monthly | ☐ |
| 8 | NTP reachability confirmation | Investigate → Flow Search | Quarterly | ☐ |
| 9 | ADM dependency map for validated systems | Investigate → ADM | Per evaluation cycle | ☐ |
| 10 | Incident reconstruction sample | Investigate → Flow + Process Search | Per incident; one sample per cycle | ☐ |

The clause-by-clause mapping is in the [Reference Design](../CSW-GxP-Reference-Design.md).

```
evidence/
├── 01-coverage/   inventory.csv, vsi-reconciliation.xlsx, cannot-instrument-register.md
├── 02-baseline/   adm-map.pdf, flow-samples.csv
├── 03-policy/     policy-export.json, simulation-report.pdf, exceptions.xlsx
└── 04-operate/    <cycle>/  (evaluation pack: items 1–10)
```

---

*Validate sufficiency of every item with quality and validation. CSW does not replace Computer System Validation, record-level ALCOA+ evidence, electronic signatures, application audit trails, QMS processes, or supplier qualification.*
