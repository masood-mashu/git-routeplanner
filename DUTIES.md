# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitRoutePlanner** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitRoutePlanner Automation Engine`
* **Responsibilities**:
  * Sequences delivery stops, calculates driving transit durations, and balances trailer cargo weight.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitRoutePlanner Verification & Policy Enforcer`
* **Responsibilities**:
  * Verifies driver Hours of Service (HOS) regulatory compliance and mandatory rest breaks.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Fleet Logistics Operations Director / Freight Dispatch Manager (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
