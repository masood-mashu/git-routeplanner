# Explainability, Auditability & Decision Logic: GitRoutePlanner

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitRoutePlanner**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitRoutePlanner** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Customer**: Customer delivery order manifests (pallets, weights, dock receiving hours).
- **Real-time**: Real-time geographic road network constraints and commercial truck bridge clearances.
- **Federal**: Federal Motor Carrier Safety Administration (FMCSA) Hours of Service regulations.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **solve_dispatch_windows**: Uses `dispatch-window-solver` to calculate verifies that scheduled stop arrival times fall within customer receiving hours.
   - **minimize_fuel_idling**: Uses `fuel-idle-minimizer` to calculate computes estimated fuel savings from optimized stop sequencing and avoiding left turns.
   - **balance_payload_weight**: Uses `payload-weight-balancer` to calculate verifies steer, drive, and trailer tandem axle weights against 80,000 lb gvwr limit.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When a delivery manifest is submitted for dispatch, the agent runs dispatch_window_solver, fuel_idle_minimizer, and payload_weight_balancer. If all receiving windows are met and axle weight is compliant, it issues APPROVED. If tight delivery margins (< 15 mins) threaten SLA, it issues NEEDS_REVIEW. If gross vehicle weight exceeds bridge ratings or breaks HOS laws, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on physical routing and weight calculations.
- **Assumes**: Assumes commercial semi-truck speed limits (65 mph max) on highway transit corridors.
- **Does**: Does not override emergency weather road closures issued by state DOT authorities.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
