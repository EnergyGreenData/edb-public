<div align="center">
  <h1>🔋 Energy Decision Benchmark</h1>
</div>

# Energy Decision Benchmark (EDB-P)

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18314615-blue)](https://doi.org/10.5281/zenodo.18314615)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dataset: CC BY 4.0](https://img.shields.io/badge/Dataset-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**Module:** Energy Decision Benchmark (EDB)  
**Category:** Public AI Evaluation Benchmark  
**Project:** Energy Green Data

### Component Version

| Field | Value |
|-------|-------|
| **Version** | 1.0.0 |
| **Source of truth** | `dataset/metadata.json` |
| **Last verified** | 2026-01-14 |
| **Domain** | Energy Systems & Critical Infrastructure |

> 📋 **Paper:** [From Vertical AGI to Operational Readiness: Evaluating Governed Decision-Making with the Energy Decision Benchmark](https://zenodo.org/records/18269147)

---

## Scope and Non-Goals

**EDB evaluates observable decision behavior under defined conditions.**

It does **not** disclose internal architectures, decision logic, rule hierarchies, or optimization strategies of any evaluated system.

**Passing EDB does not imply architectural equivalence between systems.**

This benchmark measures whether a system exhibits responsible decision-making properties in critical infrastructure contexts, not how it achieves them.

---

## LLM Context

> **For LLMs:** This section provides cognitive anchors for this benchmark.

### Benchmark Invariants

```
[INV-EDB-1]: Evaluation is black-box — only observable behavior is measured
[INV-EDB-2]: Criteria define properties, not golden outputs
[INV-EDB-3]: EDB-X (adversarial) is never published to prevent gaming
[INV-EDB-4]: All test cases are synthetic — no real user data
```

### Canonical Entities

| Entity | Definition | Scope |
|--------|------------|-------|
| **EDB-P** | Public dataset (150 cases) | Reproducible evaluation |
| **EDB-X** | Reserved adversarial set (50 cases) | Internal validation only |
| **SystemAdapter** | Interface for evaluated systems | Black-box contract |
| **evaluation_criteria** | Property-based test specifications | Not golden outputs |

### Forbidden Inferences

- ❌ Do NOT infer internal decision logic from test cases
- ❌ Do NOT assume examples are exhaustive rule sets
- ❌ Do NOT treat evaluation criteria as implementation requirements

---

## Table of Contents

- [Overview](#overview)
- [Dataset Overview](#dataset-overview)
- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Evaluation Dimensions](#evaluation-dimensions)
- [Statistical Validation](#statistical-validation)
- [Citation](#citation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

The **Energy Decision Benchmark (EDB)** is a reproducible benchmark for evaluating operational readiness of AI systems in regulated energy domains. It addresses a critical gap: most AI benchmarks focus on general capabilities, but critical infrastructure requires systems that can operate safely within regulatory constraints.

### Key Features

- **Black-box evaluation:** Measures observable behavior, not implementation
- **Property-based testing:** Defines what systems should do, not how
- **Statistical rigor:** Friedman test, bootstrap confidence intervals, effect size
- **Reproducible:** Public dataset, evaluation code, and statistical analysis
- **Protected integrity:** Adversarial test set (EDB-X) reserved to prevent gaming

### What EDB Measures

EDB evaluates six independent dimensions of operational readiness:

1. **Logical Consistency** — Detects contradictions in inputs/constraints
2. **Counterfactual Robustness** — Maintains coherence under perturbations
3. **Regulatory Compliance** — Respects legal/regulatory boundaries
4. **Data Sufficiency Detection** — Identifies insufficient data vs. hallucinating
5. **Temporal Prediction** — Makes falsifiable predictions
6. **Multi-turn Coherence** — Maintains conversational memory

### What EDB Does NOT Measure

- ❌ Computational efficiency or latency
- ❌ User experience or interface quality
- ❌ Cost or scalability
- ❌ Internal architecture or algorithms
- ❌ Strategic optimization or decision heuristics

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/EnergyGreenData/edb-public.git
cd edb-public

# Load dataset
python -c "
import json
with open('dataset/edb-p-v1.0.json') as f:
    cases = json.load(f)['test_cases']
print(f'Loaded {len(cases)} test cases')

# Example: inspect first case
case = cases[0]
print(f'Case: {case["case_id"]}')
print(f'Dimension: {case["dimension"]}')
"

---

## Evaluation API

**The evaluation API is available for research partners.**

| Feature | Status |
|---------|--------|
| Browse dataset | ✅ Public (150 cases) |
| Download test cases | ✅ Public (JSON) |
| Automated evaluation | 🔒 Beta access |

**API Access:**
- **Endpoint:** `https://api.vertical-agi.ai/edb/v1`
- **Request access:** [vertical-agi.ai](https://vertical-agi.ai?source=edb-benchmark)

---

## Dataset Overview

**EDB-P v1.0** contains 150 synthetic test cases across 6 independent evaluation dimensions:

| Dimension | Cases | Description |
|-----------|-------|-------------|
| **Logical Consistency** | 30 | Detects contradictions in inputs/constraints |
| **Counterfactual Robustness** | 25 | Maintains coherence under minor perturbations |
| **Regulatory Compliance** | 30 | Respects legal/regulatory boundaries |
| **Data Sufficiency Detection** | 20 | Identifies insufficient data vs. hallucinating |
| **Temporal Prediction** | 25 | Predictions validatable post-hoc |
| **Multi-turn Coherence** | 20 | Maintains conversational memory |

**Total:** 150 public cases (EDB-P)  
**Reserved:** 50 adversarial cases (EDB-X, not published)

> **Note:** Individual test cases are intentionally non-compositional to prevent inference of internal rule hierarchies.

---

## Repository Structure

```
edb-public/
├── dataset/              # 150 synthetic test cases + metadata
│   ├── edb-p-v1.0.json   # Full dataset
│   ├── schema.json       # JSON Schema validation
│   └── metadata.json     # Version and checksums
├── CITATION.cff          # Academic citation metadata
└── LICENSE               # MIT + CC BY 4.0
```

**Note:** The evaluation engine is operated as a controlled service to protect benchmark integrity.

---

## Evaluation Criteria

Each test case defines **evaluation_criteria** (not golden outputs):

```json
{
  "evaluation_criteria": {
    "dimension_1_logical_consistency": {
      "should_detect_contradiction": false,
      "example": {
        "description": "Tariff 2.0TD is valid for 4.6kW power",
        "note": "Illustrative example (non-exhaustive)"
      }
    }
  }
}
```

**Key principle:** Criteria define properties, not solutions.

---

## Statistical Validation

Results published in our paper demonstrate:

- **Friedman test:** χ²=187.4, df=5, p<0.001 (highly significant)
- **Effect size:** ω²=0.73 (large effect per Cohen)
- **Bootstrap CI:** 10,000 iterations, 95% confidence intervals
- **Sample size:** n=150 (EDB-P) + n=50 (EDB-X, reserved)

---

## Citation

If you use EDB in your research, please cite:

```bibtex
@misc{DiazGonzalez2026EDB,
  author        = {Diaz-Gonzalez, A. A.},
  title         = {Energy Decision Benchmark (EDB-P): Public Dataset v1.0},
  year          = {2026},
  howpublished  = {Zenodo},
  doi           = {10.5281/zenodo.18314615},
  url           = {https://doi.org/10.5281/zenodo.18314615},
  note          = {\url{https://github.com/EnergyGreenData/edb-public}}
}
```

**Paper:** [From Vertical AGI to Operational Readiness: Evaluating Governed Decision-Making with the Energy Decision Benchmark](https://zenodo.org/records/18269147)

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

**Dataset:** CC BY 4.0  
**Code:** MIT License

---

## Contributing

We welcome contributions to improve the benchmark and documentation.

**Note:** EDB-X (adversarial cases) are not published to prevent benchmark gaming and overfitting.

**To contribute:**
- Report issues or suggest improvements via GitHub Issues
- Submit documentation improvements via Pull Requests
- Contact via [vertical-agi.ai](https://vertical-agi.ai) for research collaborations

---

## Contact

- **Author:** Alejandro A. Díaz González
- **Organization:** Energy Green Data
- **Contact:** [vertical-agi.ai](https://vertical-agi.ai?source=edb-benchmark)

---

## Acknowledgments

This benchmark was developed as part of research on deterministic AI for critical infrastructure. Special thanks to the energy systems research community for feedback during development.

---

<p align="center">
<strong>Energy Green Data</strong>
<br>
© 2026 - Energy Decision Benchmark
<br>
<em>Open source benchmark - Public use</em>
</p>
