<div align="center">
  <img src="./docs/assets/EGD_negativo@2x.png" alt="Energy Green Data" width="300" style="margin: 20px 0;"/>
</div>

# Energy Decision Benchmark (EDB-P)

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.XXXXXXX-blue)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dataset: CC BY 4.0](https://img.shields.io/badge/Dataset-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**Módulo:** Energy Decision Benchmark (EDB)  
**Categoría:** Public AI Evaluation Benchmark  
**Proyecto:** Energy Green Data

### Versión del Componente

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0.0 |
| **Fuente de verdad** | `dataset/metadata.json` |
| **Última verificación** | 2026-01-14 |
| **Dominio** | Energy Systems & Critical Infrastructure |

> 📋 **Paper:** [Towards a Deterministic Vertical AGI for Energy Systems](https://www.researchgate.net/publication/395835564)

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

# Install client
pip install -r client/requirements.txt

# Evaluate your system
python -c "
from client.edb_client import EDBClient, SystemResponse

# Initialize client
client = EDBClient(api_key='your-api-key')

# Get a test case
case = client.get_case('edb-p-001')

# Your system generates response
response = SystemResponse(
    decision='La configuración es válida',
    reasoning='Tarifa 2.0TD permite hasta 15kW',
    confidence=0.92
)

# Evaluate
result = client.evaluate_case('edb-p-001', response)
print(f'Score: {result[\"overall_score\"]:.2%}')
"
```

See [`client/README.md`](client/README.md) for complete documentation.

---

## ⚠️ API Status

**Note:** The evaluation API is currently in **controlled beta** with selected research partners.

**Current capabilities:**
- ✅ **Browse dataset** - Available now (150 test cases)
- ✅ **Download test cases** - Available now (JSON format)
- ✅ **Review methodology** - Available now (full documentation)
- ✅ **Automated evaluation** - Beta access (controlled)

**API Access:**
- **Beta Access:** Available for research partners and academic institutions
- **Public Access:** Planned for Q2 2026 (pending evaluator improvements)
- **Endpoint:** `https://api.vertical-agi.ai/edb/v1`
- **Contact:** research@energygreendata.com for beta access

**Beta Status Details:**
- ✅ Security hardening validated (P0 tests passed)
- ✅ Rate limiting and tier system active
- ✅ Reproducibility guaranteed (same user + case + day = same score)
- ⚠️ Evaluator focuses on validity detection (pass/fail) rather than continuous scoring
- 📋 See [API_SCORING_CONTRACT.md](docs/API_SCORING_CONTRACT.md) for tier specifications

**For early access to evaluation services:**  
Contact: research@energygreendata.com

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
├── client/               # Python client for API evaluation
├── docs/                 # Methodology and API documentation
└── CITATION.cff          # Academic citation metadata
```

**Note:** The evaluation engine and statistical analysis tools are operated as controlled services to protect benchmark integrity.

---

## Evaluation Criteria

Each test case defines **evaluation_criteria** (not golden outputs):

```json
{
  "evaluation_criteria": {
    "dimension_1_logical_consistency": {
      "should_detect_contradiction": false,
      "example": {
        "description": "Tarifa 2.0TD es válida para potencia 4.6kW",
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
  doi           = {10.5281/zenodo.XXXXXXX},
  url           = {https://doi.org/10.5281/zenodo.XXXXXXX},
  note          = {\url{https://github.com/EnergyGreenData/edb-public}}
}
```

**Paper:** [Towards a Deterministic Vertical AGI for Energy Systems](https://www.researchgate.net/publication/395835564)

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

**Dataset:** CC BY 4.0  
**Code:** MIT License

---

## Repository Structure (Detailed)

```
edb-public/
├── README.md                          # This document
├── LICENSE                            # MIT + CC BY 4.0
├── CITATION.cff                       # Academic citation
├── .gitignore
│
├── dataset/                           # Public dataset
│   ├── README.md                      # Dataset documentation
│   ├── edb-p-v1.0.json               # 150 test cases
│   ├── edb-p-example-001.json        # Example test case
│   ├── metadata.json                  # Version, stats, checksums
│   └── schema.json                    # JSON Schema validation
│
├── client/                            # Evaluation client
│   ├── edb_client.py                  # Python client for API
│   ├── requirements.txt               # Client dependencies
│   └── README.md                      # Client documentation
│
└── docs/                              # Documentation
    ├── METHODOLOGY.md                 # Detailed methodology
    ├── API_SCORING_CONTRACT.md        # API scoring specification by tier
    ├── PAPER_LIMITATIONS_SECTION.md   # Limitations section for academic papers
    └── WEB_DISCLAIMER.md              # Disclaimers for web/documentation
```

**Note:** The evaluation engine and statistical analysis tools are operated as controlled services to protect benchmark integrity. Systems are evaluated through the official API using the client provided in `client/`.

---

## API Documentation

### Scoring Contract

The API provides three tiers of access with different levels of detail and rate limits. See [`docs/API_SCORING_CONTRACT.md`](docs/API_SCORING_CONTRACT.md) for complete specifications:

- **Free Tier:** Public access, quantized scores, generic rate limit messages
- **Research Tier:** Academic/research access, dimension scores included
- **Internal Tier:** Full precision, debug information, higher rate limits

### Beta Status

The EDB API is currently in **controlled beta**. Key characteristics:

- **Scoring Focus:** Validity detection (pass/fail) rather than continuous quality gradation
- **Security:** Full hardening active (noise, rate limiting, tier filtering)
- **Reproducibility:** Same user + same case + same day = same score
- **Use Cases:** System validation, research, benchmarking

See [`docs/WEB_DISCLAIMER.md`](docs/WEB_DISCLAIMER.md) for detailed beta status information.

---

## Evaluation Dimensions

### Dimension 1: Logical Consistency

**Measures:** Detection of contradictions in inputs/constraints

**Example:**
- ❌ Invalid: Tarifa 2.0TD (max 15kW) + Potencia 20kW
- ✅ Valid: Tarifa 2.0TD + Potencia 4.6kW

**Scoring:** Binary (1.0 = correct, 0.0 = incorrect)

### Dimension 2: Counterfactual Robustness

**Measures:** Stability under minor perturbations

**Test method:**
1. Evaluate with original values
2. Perturb input slightly (±5%)
3. Check if recommendation changes

**Scoring:** 1.0 if stable, 0.0 if unstable

### Dimension 3: Regulatory Compliance

**Measures:** Respect for legal/regulatory boundaries

**Test method:**
- Define forbidden actions
- Check system output for violations

**Scoring:** 1.0 if compliant, 0.0 if violation detected

### Dimension 4: Data Sufficiency Detection

**Measures:** Ability to identify insufficient data vs. hallucinating

**Anti-pattern:** Confident answer with insufficient data

**Scoring:** 1.0 if detects insufficiency, 0.0 if hallucinates

### Dimension 5: Temporal Prediction

**Measures:** Predictions validatable post-hoc

**Requirement:** Falsifiable predictions with quantitative metrics

**Scoring:** 1.0 if makes falsifiable prediction, 0.0 otherwise

### Dimension 6: Multi-turn Coherence

**Measures:** Conversational memory without degradation

**Test method:** Reference information from turn N in turn N+K

**Scoring:** 1.0 if coherent, 0.0 if memory lost

---

## Statistical Validation

Results published in our paper demonstrate:

- **Friedman test:** χ²=187.4, df=5, p<0.001 (highly significant)
- **Effect size:** ω²=0.73 (large effect per Cohen)
- **Bootstrap CI:** 10,000 iterations, 95% confidence intervals
- **Sample size:** n=150 (EDB-P) + n=50 (EDB-X, reserved)

**Note:** Statistical analysis scripts are maintained internally to protect benchmark integrity. Results are fully documented in the published paper.

---

## Citation

If you use EDB in your research, please cite:

```bibtex
@misc{DiazGonzalez2026EDB,
  author        = {Diaz-Gonzalez, A. A.},
  title         = {Energy Decision Benchmark (EDB-P): Public Dataset v1.0},
  year          = {2026},
  howpublished  = {Zenodo},
  doi           = {10.5281/zenodo.XXXXXXX},
  url           = {https://doi.org/10.5281/zenodo.XXXXXXX},
  note          = {\url{https://github.com/EnergyGreenData/edb-public}}
}
```

**Paper:** [Towards a Deterministic Vertical AGI for Energy Systems](https://www.researchgate.net/publication/395835564)

---

## Contributing

We welcome contributions to improve the benchmark and documentation.

**Note:** EDB-X (adversarial cases) are not published to prevent benchmark gaming and overfitting.

**To contribute:**
- Report issues or suggest improvements via GitHub Issues
- Submit documentation improvements via Pull Requests
- Contact research@energygreendata.com for research collaborations

---

## License

**Code:** MIT License  
**Dataset:** CC BY 4.0

See [LICENSE](LICENSE) for details.

---

## Contact

- **Author:** Alejandro A. Díaz González
- **Organization:** Energy Green Data
- **Email:** a.diaz@energygreendata.com
- **Website:** https://vertical-agi.ai/benchmark-2025

---

## Acknowledgments

This benchmark was developed as part of research on deterministic AI for critical infrastructure. Special thanks to the energy systems research community for feedback during development.

---

<p align="center">
<img src="docs/assets/EGD.png" width="200">
<br>
<strong>Energy Green Data - Public Project</strong>
<br>
© 2026 - Energy Decision Benchmark
<br>
<em>Open source benchmark - Public use</em>
</p>
