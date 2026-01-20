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

Each test case follows the JSON schema defined in `schema.json`:

```json
{
  "id": "edb-p-XXX",
  "version": "1.0.0",
  "domain": "electricity|gas|solar|mobility|water|equipment",
  "scenario_type": "string",
  "difficulty": "easy|medium|hard",
  "input": {
    "context": {...},
    "query": "string"
  },
  "evaluation_criteria": {
    "dimension_1_logical_consistency": {...},
    "dimension_2_counterfactual": {...},
    "dimension_3_regulatory": {...},
    "dimension_4_data_sufficiency": {...},
    "dimension_5_temporal": {...},
    "dimension_6_multiturn": {...}
  },
  "metadata": {...}
}
```

## Evaluation Criteria (Not Golden Outputs)

**Important:** `evaluation_criteria` defines **properties** that systems should exhibit, not exact outputs.

Example:
```json
"dimension_1_logical_consistency": {
  "should_detect_contradiction": false,
  "rationale": "Tariff 2.0TD allows up to 15kW",
  "example": {
    "description": "Tariff 2.0TD is valid for 4.6kW power",
    "note": "Illustrative example (non-exhaustive)"
  }
}
```

This means:
- ✅ System should NOT flag this as contradictory
- ✅ System can express this in any valid way
- ❌ System does NOT need to match exact wording

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
