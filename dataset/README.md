# EDB-P Dataset v1.0

## Overview

The **Energy Decision Benchmark - Public (EDB-P)** dataset contains 150 synthetic test cases designed to evaluate operational readiness of AI systems in regulated energy domains.

## Dataset Composition

| Dimension | Cases | Easy | Medium | Hard |
|-----------|-------|------|--------|------|
| Logical Consistency | 30 | 15 | 10 | 5 |
| Counterfactual Robustness | 25 | 12 | 8 | 5 |
| Regulatory Compliance | 30 | 10 | 15 | 5 |
| Data Sufficiency Detection | 20 | 8 | 8 | 4 |
| Temporal Prediction | 25 | 10 | 10 | 5 |
| Multi-turn Coherence | 20 | 8 | 8 | 4 |
| **Total** | **150** | **63** | **59** | **28** |

## File Format

Each test case in `edb-p-v1.0.json` follows this structure:

```json
{
  "case_id": "edb-p-XXX",
  "dimension": "logical_consistency|counterfactual_robustness|regulatory_compliance|data_sufficiency|temporal_prediction|multiturn_coherence",
  "scenario_type": "energy_decision",
  "context": {
    "country": "ES",
    "domain": "electricity|gas|solar|mobility|water|equipment",
    "user_type": "residential|commercial|industrial"
  },
  "input_data": { ... }  // Structure varies by dimension (see below)
}
```

### Input Data Structure by Dimension

| Dimension | Fields in `input_data` |
|-----------|------------------------|
| **logical_consistency** | `tariff`, `contracted_power_p1`, `contracted_power_p2`, `annual_consumption`, `has_solar` |
| **counterfactual_robustness** | `baseline_consumption`, `solar_production`, `battery_capacity` |
| **regulatory_compliance** | `installation_power`, `tariff`, `has_certificate` |
| **data_sufficiency** | `income_data`, `consumption_data`, `missing_fields` |
| **temporal_prediction** | `historical_consumption[]`, `season`, `solar_installed` |
| **multiturn_coherence** | `previous_decision`, `new_information`, `context_changed` |

> **Note:** Each dimension tests different aspects of decision-making, hence the varied input structures.

## Evaluation

Evaluation is performed server-side via the API. Systems are evaluated on 6 independent dimensions:

1. **Logical Consistency** - Detect contradictions in inputs
2. **Counterfactual Robustness** - Stability under perturbations
3. **Regulatory Compliance** - Legal boundary respect
4. **Data Sufficiency Detection** - Identify missing data vs hallucinate
5. **Temporal Prediction** - Validatable predictions
6. **Multi-turn Coherence** - Conversational memory

Evaluation criteria are **not published** to maintain benchmark integrity

## What is NOT Published

To prevent benchmark gaming and protect evaluation integrity:

- ❌ **EDB-X:** 50 adversarial test cases (reserved)
- ❌ **Golden outputs:** Exact expected responses
- ❌ **Decision trees:** Internal reasoning paths
- ❌ **Rule combinations:** Complex multi-constraint cases

## Validation

Validate dataset integrity using the JSON Schema:

```bash
# Using any JSON Schema validator
jsonschema -i edb-p-v1.0.json schema.json
```

## Checksum

Dataset integrity can be verified using SHA256 checksum in `metadata.json`.

## License

Dataset: **CC BY 4.0**  
You are free to share and adapt with attribution.

## Citation

See [CITATION.cff](../CITATION.cff) in repository root.
