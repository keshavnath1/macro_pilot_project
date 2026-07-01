# Consolidated System Design Q&A — One-Slide Reference

**Purpose:** A single-page cheat sheet consolidating all 23 system-design questions into a compact table you can keep visible during the meeting.

---

## Slide Title Suggestion: "Anticipated Technical Questions & Enterprise Readiness"

---

| # | Question (What They'll Ask) | One-Line Answer (Your BLUF) | Theme |
|---|---|---|---|
| 1 | "50 data scientists pulling 50GB datasets — won't local cache explode?" | Shared EFS cache with symlinks deduplicates; only one copy exists per unique hash. | Storage |
| 2 | "Can DVC run 10 parallel hyperparameter jobs?" | No — DVC is a DAG tracker, not a compute engine. Kubeflow handles parallelism. | Compute |
| 3 | "How do credentials get into Kubeflow pods securely?" | Kubernetes Secrets mounted at runtime; never in Git or DVC YAML. | Security |
| 4 | "If Kubeflow orchestrates, why do we need DVC at all?" | Kubeflow is the engine (executes); DVC is the ledger (versions and proves). | Architecture |
| 5 | "Monorepo with 20 models — does DVC survive submodules?" | One DVC root per Git repo; submodules unsupported. Architectural decision needed. | Structure |
| 6 | "Walk me through what `dvc push` actually does on a 50GB file." | Hashes file → checks if hash exists on S3 → uploads only if new. One file = one request. | Internals |
| 7 | "Two scientists run `dvc repro` on different branches — conflict?" | Each produces a different `dvc.lock`; reconciled via Git merge. By design. | Concurrency |
| 8 | "10 rows change in 50GB CSV — does DVC store a full second copy?" | Yes. File-level granularity. Mitigation: partition data into smaller files. | Storage Cost |
| 9 | "lakeFS acquired DVC — long-term deprecation risk?" | Apache 2.0 license protects us. We validated a pattern, not just a product. | Risk |
| 10 | "How does DVC decide which stages to re-run?" | Compares current MD5 hashes vs `dvc.lock`. Mismatch = re-run that stage + downstream. | Execution |
| 11 | "Tune succeeds, Refit fails — do we lose Tune outputs?" | No. Each stage is independently cached. Re-run skips Tune, retries only Refit. | Fault Tolerance |
| 12 | "Can DVC trigger Refit automatically if drift is detected?" | No. DVC is a static DAG. Conditional logic requires Kubeflow. | Limitations |
| 13 | "Who is source of truth — Kubeflow run history or DVC lock file?" | DVC = what data/code produced what result. Kubeflow = when/where/how long it ran. | Governance |
| 14 | "How does Kubeflow trigger the pipeline — schedule or manual?" | All three supported. Start manual → scheduled → event-driven as maturity grows. | Operations |
| 15 | "Pod crashes mid-run — does DVC lose state?" | No. DVC state lives in Git + S3. Pod restart re-runs only the failed stage. | Resilience |
| 16 | "How do we freeze the fragile conda environment?" | Bake into a Docker image tagged with Git commit hash. Immutable and versioned. | Reproducibility |
| 17 | "SR 11-7 independent validation — how does a separate team reproduce?" | Clone repo → `dvc pull` → `dvc repro` → compare output hashes. Two commands. | Compliance |
| 18 | "Show me the lineage for an OCC examiner." | Git log (code) + `dvc.lock` (data hashes) + CloudTrail (access) + Kubeflow (execution). | Audit |
| 19 | "Can someone tamper with production data undetected?" | Impossible. Any change alters the hash → breaks `dvc.lock` → requires a Git commit. | Integrity |
| 20 | "Bus factor — if you leave, can someone else run this?" | `dvc.yaml` is the operational knowledge. New hire reads YAML, runs `dvc repro`. Done. | Sustainability |
| 21 | "S3 goes down — are we blocked?" | No. Local cache enables offline execution. Only sharing is blocked. | DR |
| 22 | "How do we catch silent wrong results?" | Add validation stages to the DAG that fail loudly if metrics breach thresholds. | Quality |
| 23 | "Single Family team adopts too — shared data dependencies?" | DVC Data Registry pattern: central repo, teams import pinned versions via `dvc import`. | Multi-Team |

---

## Visual Layout Suggestion for the Slide

If you want to present this as a single PowerPoint/deck slide, use this structure:

```
┌─────────────────────────────────────────────────────────────┐
│  Title: "Enterprise Readiness — Key Technical Questions"    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  STORAGE &   │  │  EXECUTION   │  │  KUBEFLOW    │      │
│  │  SCALABILITY │  │  & DAG       │  │  INTEGRATION │      │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤      │
│  │ • Shared     │  │ • Hash-based │  │ • DVC =      │      │
│  │   cache      │  │   re-run     │  │   ledger     │      │
│  │ • File-level │  │ • Stage-     │  │ • Kubeflow = │      │
│  │   dedup      │  │   atomic     │  │   engine     │      │
│  │ • Partition  │  │ • Static DAG │  │ • Secrets    │      │
│  │   large data │  │   (no cond.) │  │   via K8s    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │  GOVERNANCE  │  │  OPERATIONS  │                        │
│  │  & SR 11-7   │  │  & DR        │                        │
│  ├──────────────┤  ├──────────────┤                        │
│  │ • Crypto     │  │ • Bus factor │                        │
│  │   lineage    │  │   = the repo │                        │
│  │ • Tamper-    │  │ • Offline-   │                        │
│  │   proof      │  │   first      │                        │
│  │ • 2-command  │  │ • Validation │                        │
│  │   validation │  │   stages     │                        │
│  └──────────────┘  └──────────────┘                        │
│                                                             │
│  Footer: "Prototype validated the pattern. Remaining work  │
│           is organizational, not technical."                │
└─────────────────────────────────────────────────────────────┘
```

---

## How to Use This Slide

This slide is **not meant to be presented line-by-line**. It serves as:

1. **A backup slide** — Keep it at the end of your deck. If Jim asks any of these questions, you can say: "I anticipated that question — let me pull up the reference."
2. **A confidence signal** — Showing you've thought through 23 enterprise-level concerns demonstrates depth without needing to explain each one.
3. **A conversation starter** — If Jim says "what about scalability?", you point to the Storage column and deliver the BLUF.

---

## The One Sentence Per Theme (If You Only Get 30 Seconds)

| Theme | Your One Sentence |
|---|---|
| Storage | "DVC deduplicates via content-addressable hashing; shared cache eliminates redundant copies." |
| Execution | "Stage-level idempotency means failures only re-run what failed, never the whole pipeline." |
| Kubeflow | "DVC versions the what; Kubeflow orchestrates the when and where." |
| Governance | "Any data change breaks the hash chain — tamper-proof by math, not by policy." |
| Operations | "The `dvc.yaml` file *is* the operational knowledge — bus factor becomes the repo itself." |
