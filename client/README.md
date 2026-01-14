# EDB-P Evaluation Client

Python client for evaluating AI systems against the Energy Decision Benchmark (EDB-P).

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from edb_client import EDBClient, SystemResponse

# Initialize client with your API key
client = EDBClient(api_key="your-api-key")

# Get dataset information
info = client.get_dataset_info()
print(f"Total cases: {info['total_cases']}")

# Get a test case
case = client.get_case("edb-p-001")

# Your system processes the case and generates a response
response = SystemResponse(
    decision="La configuración es válida",
    reasoning="Tarifa 2.0TD permite hasta 15kW y potencia es 4.6kW",
    confidence=0.92
)

# Evaluate the response
result = client.evaluate_case("edb-p-001", response)
print(f"Score: {result['overall_score']:.2%}")
```

## API Key

To obtain an API key for evaluation:

1. Visit: https://vertical-agi.ai/benchmark-2025
2. Register your system
3. Receive your API key via email

**Note:** API keys are required for evaluation but not for browsing the dataset.

## Response Format

All system responses must follow this format:

```python
SystemResponse(
    decision="Main decision or recommendation",
    reasoning="Explanation of the decision",
    confidence=0.85,  # Float between 0.0 and 1.0
    metadata={}  # Optional additional data
)
```

## Evaluation Workflow

### 1. Browse Dataset (No API Key Required)

```python
client = EDBClient()  # No API key needed

# Get dataset info
info = client.get_dataset_info()

# List all cases
cases = client.list_cases()

# Get specific case
case = client.get_case("edb-p-001")
```

### 2. Evaluate Single Case

```python
client = EDBClient(api_key="your-api-key")

case = client.get_case("edb-p-001")
response = your_system.process(case)

result = client.evaluate_case("edb-p-001", response)
```

### 3. Evaluate All Cases

```python
def my_system(case):
    """Your system implementation"""
    # Process case and return SystemResponse
    return SystemResponse(
        decision="...",
        reasoning="...",
        confidence=0.85
    )

# Evaluate on complete dataset
results = client.evaluate_all(
    system_name="MyEnergyAI v1.0",
    system_callable=my_system
)

print(f"Overall score: {results['overall_score']:.2%}")
print(f"Pass rate: {results['summary']['pass_rate']:.2%}")
```

## Evaluation Dimensions

EDB evaluates systems across 6 independent dimensions:

1. **Logical Consistency** - Detects contradictions in inputs/constraints
2. **Counterfactual Robustness** - Maintains coherence under perturbations
3. **Regulatory Compliance** - Respects legal/regulatory boundaries
4. **Data Sufficiency Detection** - Identifies insufficient data vs. hallucinating
5. **Temporal Prediction** - Makes falsifiable predictions
6. **Multi-turn Coherence** - Maintains conversational memory

## Results Format

### Single Case Evaluation

```json
{
  "case_id": "edb-p-001",
  "overall_score": 0.83,
  "dimension_scores": {
    "logical_consistency": 1.0,
    "counterfactual_robustness": 0.8,
    "regulatory_compliance": 0.9,
    "data_sufficiency": 0.7,
    "temporal_prediction": 0.8,
    "multiturn_coherence": 0.8
  },
  "passed": true
}
```

### Batch Evaluation

```json
{
  "system_name": "MyEnergyAI v1.0",
  "overall_score": 0.78,
  "dimension_scores": {
    "logical_consistency": 0.85,
    "counterfactual_robustness": 0.75,
    "regulatory_compliance": 0.80,
    "data_sufficiency": 0.72,
    "temporal_prediction": 0.78,
    "multiturn_coherence": 0.80
  },
  "summary": {
    "total_cases": 150,
    "passed": 120,
    "failed": 30,
    "pass_rate": 0.80
  }
}
```

## Best Practices

### 1. Handle Cases Independently

Each test case should be processed independently without cross-case learning or optimization.

### 2. Provide Reasoning

Always include clear reasoning in your responses. This is evaluated as part of the benchmark.

### 3. Express Uncertainty

Use the `confidence` field honestly. Systems that express appropriate uncertainty score better than overconfident systems.

### 4. Respect Data Limitations

If a case has insufficient data, your system should detect this rather than hallucinate values.

### 5. Batch Evaluation

For complete evaluation, use `evaluate_all()` or `evaluate_batch()` rather than individual calls.

## Rate Limits

- **Dataset browsing:** Unlimited
- **Single evaluations:** 100 requests/hour
- **Batch evaluations:** 10 requests/hour

For higher limits, contact: research@energygreendata.com

## Support

- **Documentation:** https://vertical-agi.ai/benchmark-2025
- **Paper:** https://www.researchgate.net/publication/395835564
- **Issues:** https://github.com/EGD2024/edb-public/issues
- **Email:** research@energygreendata.com

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
  note          = {\url{https://github.com/EGD2024/edb-public}}
}
```

## License

- **Client Code:** MIT License
- **Dataset:** CC BY 4.0

See [LICENSE](../LICENSE) for details.
