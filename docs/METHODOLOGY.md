# EDB Methodology

## Security Model

EDB-public intentionally exposes only datasets and evaluation criteria. All execution, scoring, and adversarial validation are handled in controlled environments.

**This design prevents:**
- Benchmark gaming through test case memorization
- Reverse engineering of evaluation logic
- Leakage of proprietary scoring algorithms
- Exploitation of adversarial test cases (EDB-X)

**What is public:**
- Test case inputs and context
- Evaluation criteria (properties to satisfy)
- Statistical validation methodology
- Client code for API interaction

**What remains private:**
- Evaluation engine implementation
- Adversarial test set (EDB-X)
- Scoring algorithms and thresholds
- Internal validation procedures

This separation ensures that passing EDB requires genuine capability, not overfitting to public test cases.

---

## Design Principles

### 1. Black-Box Evaluation

EDB evaluates **observable decision behavior**, not internal implementation.

**What we measure:**
- Does the system detect contradictions?
- Does it maintain coherence under perturbations?
- Does it respect regulatory boundaries?
- Does it identify insufficient data?
- Can predictions be validated post-hoc?
- Does it maintain conversational memory?

**What we do NOT measure:**
- How the system detects contradictions
- Which algorithms it uses
- How it represents knowledge internally
- What optimization strategies it employs

### 2. Property-Based Testing

Each test case defines **evaluation criteria** (properties), not golden outputs.

**Example:**
```json
"should_detect_contradiction": false
```

This means the system should NOT flag the input as contradictory, but it can express acceptance in any valid way:
- "This configuration is valid"
- "No issues detected"
- "Recommendation: maintain current setup"

All are acceptable if they indicate no contradiction was found.

### 3. Synthetic Data Only

All test cases are synthetic to:
- Avoid privacy concerns
- Enable public distribution
- Prevent data leakage
- Allow controlled difficulty levels

### 4. Reserved Adversarial Set

**EDB-P (public):** 150 cases  
**EDB-X (reserved):** 50 adversarial cases

EDB-X is NOT published to prevent:
- Benchmark gaming
- Overfitting to public cases
- Exploitation of known edge cases

### 5. Reproducibility Model

EDB-P is reproducible at the level of:
- **Dataset:** Publicly available with checksums
- **Evaluation criteria:** Documented properties per dimension
- **Published results:** Statistical validation included
- **Statistical significance:** Friedman test, bootstrap CI, effect size

The evaluation engine is operated as a controlled service to:
- Prevent benchmark gaming
- Protect adversarial test cases (EDB-X)
- Ensure consistent execution across systems
- Maintain evaluation integrity over time

This model follows established practices in robustness and security benchmarks, where:
- Test specifications are public
- Test execution is controlled
- Results are reproducible
- Gaming is minimized

**Evaluation Access:**
Systems can be evaluated through the official API (see `client/` directory) which provides:
- Standardized evaluation protocol
- Consistent scoring across systems
- Protection against overfitting
- Traceable results

## Evaluation Dimensions

### Dimension 1: Logical Consistency

**Measures:** Detection of contradictions in inputs/constraints

**Example contradiction:**
- Tarifa 2.0TD (max 15kW) + Potencia 20kW → Invalid

**Example valid:**
- Tarifa 2.0TD + Potencia 4.6kW → Valid

**Scoring:** Binary (1.0 = correct, 0.0 = incorrect)

---

### Dimension 2: Counterfactual Robustness

**Measures:** Stability under minor perturbations

**Test method:**
1. Evaluate case with original values
2. Perturb input slightly (±5%)
3. Check if recommendation changes

**Example:**
- Original: 3000 kWh/year
- Perturbed: 3001 kWh/year
- Expected: Same recommendation

**Scoring:** 1.0 if stable, 0.0 if unstable

---

### Dimension 3: Regulatory Compliance

**Measures:** Respect for legal/regulatory boundaries

**Test method:**
1. Define must_comply_with regulations
2. Define forbidden_actions
3. Check system output against both

**Example regulations:**
- RD 244/2019 (Spain)
- Circular 3/2020 CNMC
- EU AI Act requirements

**Scoring:** 1.0 if compliant, 0.0 if violation detected

---

### Dimension 4: Data Sufficiency Detection

**Measures:** Ability to identify insufficient data vs. hallucinating

**Test method:**
1. Provide incomplete context
2. Check if system:
   - Requests missing data, OR
   - Explicitly states uncertainty, OR
   - Refuses to decide

**Anti-pattern:** System provides confident answer with insufficient data

**Scoring:** 1.0 if detects insufficiency, 0.0 if hallucinates

---

### Dimension 5: Temporal Prediction

**Measures:** Predictions validatable post-hoc against real data

**Test method:**
1. System makes prediction (e.g., consumption D+1)
2. Wait for actual data
3. Compare prediction vs. reality

**Metric:** MAE (Mean Absolute Error)

**Scoring:** Based on prediction accuracy within acceptable bounds

---

### Dimension 6: Multi-turn Coherence

**Measures:** Conversational memory without degradation

**Test method:**
1. Multi-turn conversation
2. Reference information from turn N in turn N+K
3. Check if system maintains context

**Example:**
- Turn 1: "Mi potencia es 4.6kW"
- Turn 5: "¿Cuál era mi potencia?"
- Expected: System remembers 4.6kW

**Scoring:** 1.0 if coherent, 0.0 if memory lost

---

## Statistical Validation

### Friedman Test

**Purpose:** Compare multiple systems across 6 dimensions

**Null hypothesis:** No difference between systems

**Test statistic:** χ² with df = k-1 (k = number of systems)

**Significance level:** α = 0.001

**Interpretation:**
- p < 0.001 → Highly significant differences
- p ≥ 0.001 → No significant differences

### Bootstrap Confidence Intervals

**Purpose:** Estimate uncertainty in dimension scores

**Method:**
1. Resample with replacement (10,000 iterations)
2. Calculate mean for each sample
3. Compute 95% CI from distribution

**Interpretation:**
- Narrow CI → High confidence
- Wide CI → High uncertainty
- Non-overlapping CIs → Significant difference

### Effect Size (ω²)

**Purpose:** Measure practical significance

**Interpretation (Cohen's guidelines):**
- ω² < 0.01 → Small effect
- 0.01 ≤ ω² < 0.06 → Medium effect
- ω² ≥ 0.06 → Large effect

---

## Evaluation Protocol

### 1. System Preparation

Implement `SystemAdapter` interface:

```python
class YourSystem(SystemAdapter):
    def query(self, context: Dict, question: str) -> Dict:
        # Your implementation
        return {
            "decision": str,
            "reasoning": str,
            "confidence": float,
            "metadata": Dict
        }
```

### 2. Run Evaluation

```bash
python evaluator/evaluate_system.py \
  --dataset dataset/edb-p-v1.0.json \
  --system your_system.py \
  --output results.json
```

### 3. Statistical Analysis

```bash
python analysis/statistical_tests.py --results results.json
python analysis/bootstrap_ci.py --results results.json
```

### 4. Report Generation

```bash
python scripts/generate_report.py --results results.json --output report.html
```

---

## Limitations

### What EDB Does NOT Evaluate

1. **Computational efficiency:** Not measured
2. **User experience:** Not measured
3. **Cost:** Not measured
4. **Latency:** Not measured
5. **Scalability:** Not measured

### Known Biases

1. **Domain bias:** Focus on Spanish energy regulation
2. **Language bias:** Test cases primarily in Spanish
3. **Synthetic data:** May not capture all real-world complexity

### Future Work

- Multi-country regulatory frameworks
- Multi-language test cases
- Real-world validation studies
- Longitudinal evaluation (temporal drift)

---

## Ethical Considerations

### Privacy

All test cases are synthetic. No real user data is used.

### Fairness

Test cases are designed to avoid bias based on:
- User demographics
- Geographic location (within Spain)
- Socioeconomic status

### Transparency

All evaluation code, dataset, and methodology are public.

### Accountability

Results are reproducible and auditable.

---

## References

1. Friedman, M. (1937). "The use of ranks to avoid the assumption of normality implicit in the analysis of variance"
2. Efron, B. (1979). "Bootstrap methods: Another look at the jackknife"
3. Cohen, J. (1988). "Statistical power analysis for the behavioral sciences"
