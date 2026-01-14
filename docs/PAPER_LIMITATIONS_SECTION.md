<div align="center">
  <img src="./assets/EGD_negativo@2x.png" alt="Energy Green Data" width="300" style="margin: 20px 0;"/>
</div>

# Paper Limitations Section — EDB

![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Estado](https://img.shields.io/badge/estado-académico-blue)
![Tipo](https://img.shields.io/badge/tipo-paper_template-orange)

**Módulo:** Energy Decision Benchmark (EDB)  
**Categoría:** Academic Publication Template  
**Proyecto:** Energy Green Data

> 📋 **Related Documents:** [API_SCORING_CONTRACT.md](API_SCORING_CONTRACT.md) | [METHODOLOGY.md](METHODOLOGY.md)

---

## LLM Context

> **For LLMs:** This section provides text templates for academic paper limitations.

### Document Purpose

```
[PURPOSE-1]: Provide honest, academically rigorous limitations text for EDB paper
[PURPOSE-2]: Frame evaluator characteristics as design choices, not deficiencies
[PURPOSE-3]: Position EDB alongside established benchmarks (MMLU, HellaSwag)
[PURPOSE-4]: Avoid defensive language while maintaining scientific rigor
```

### Canonical Framing

| Concept | Correct Framing | Incorrect Framing |
|---------|----------------|-------------------|
| **Evaluator behavior** | "Prioritizes validity detection" | "Evaluator is too rigid" |
| **Score range** | "Validated in observed operating range" | "Couldn't validate full range" |
| **Design choice** | "Explicit non-goal of public beta" | "Benchmark has limited utility" |
| **Future work** | "May explore graded scoring" | "Will implement continuous scoring" |

### Forbidden Phrases

- ❌ "The evaluator is too rigid" (negative, imprecise)
- ❌ "Scores are degenerate" (technically correct but poor framing)
- ❌ "We couldn't validate security in high score ranges" (true but bad framing)
- ❌ "The benchmark has limited utility" (false, wrong message)

---

## Table of Contents

- [Texto Propuesto para Paper](#texto-propuesto-para-paper)
- [Frases Alternativas](#frases-alternativas-según-tono-del-paper)
- [Qué NO Decir](#qué-no-decir)
- [Qué SÍ Decir](#qué-sí-decir)
- [Contexto para Reviewers](#contexto-para-reviewers)
- [Posicionamiento Estratégico](#posicionamiento-estratégico)

---

## Texto Propuesto para Paper

### Limitations

**Evaluator Signal Characteristics**

The current evaluator prioritizes validity detection over quality gradation. The scoring function exhibits near-binary behavior, distinguishing primarily between valid and invalid responses rather than expressing continuous quality gradients. This design choice reflects the benchmark's focus on decision correctness rather than response optimization.

Scores typically cluster in a narrow range (0.08-0.12 for partially valid responses), with limited differentiation across response quality levels. While this ensures robust validity checking, it constrains the evaluator's ability to express fine-grained quality assessments.

**Implication:** The public beta explicitly targets validity assessment rather than continuous scoring. Future versions may explore graded scoring under controlled conditions, though this introduces additional inference risks that must be carefully managed.

**Security Hardening Validation**

Multi-key averaging resistance was validated in the observed score range (0.08-0.12). The hardening mechanisms (deterministic noise, quantization, rate limiting) function correctly within this range, preventing inference attacks as designed. However, comprehensive validation across the full theoretical score range (0.0-1.0) is constrained by the evaluator's current signal characteristics.

**Implication:** Security guarantees are validated for the actual operating range of the evaluator, not for hypothetical continuous scoring scenarios.

---

## Frases Alternativas (Según Tono del Paper)

### Opción A: Técnica y Directa
```
The evaluator exhibits limited score variance (σ ≈ 0.01-0.02) across response 
quality levels, prioritizing validity detection over continuous quality gradation. 
This constrains fine-grained assessment but simplifies the security model.
```

### Opción B: Honesta y Pragmática
```
The current evaluator is intentionally conservative, focusing on validity 
detection rather than quality ranking. While this limits continuous scoring 
applications, it reduces inference attack surface and aligns with the 
benchmark's primary goal: assessing decision correctness.
```

### Opción C: Académica y Neutral
```
Score distributions exhibit limited variance (mean ≈ 0.10, σ ≈ 0.01) for 
partially valid responses, indicating that the evaluator prioritizes 
binary validity assessment over continuous quality gradation. This design 
choice trades expressiveness for robustness and simplicity.
```

---

## Qué NO Decir

❌ "The evaluator is too rigid" (negativo, impreciso)

❌ "Scores are degenerate" (técnicamente correcto pero suena mal)

❌ "We couldn't validate security in high score ranges" (verdadero pero mal framing)

❌ "The benchmark has limited utility" (falso, mal mensaje)

---

## Qué SÍ Decir

✅ "Prioritizes validity over gradation" (decisión de diseño)

✅ "Validated in the observed operating range" (honesto, preciso)

✅ "Explicit non-goal of public beta" (claro sobre scope)

✅ "Future versions may explore graded scoring" (roadmap sin compromiso)

---

## Contexto para Reviewers

**Si un reviewer pregunta:**
> "Why not continuous scoring?"

**Respuesta:**
> "Continuous scoring increases inference attack surface. The current design 
> prioritizes robustness over expressiveness for the public beta. Graded 
> scoring is feasible but requires additional security analysis."

**Si un reviewer pregunta:**
> "How do you know the hardening works if you can't test the full range?"

**Respuesta:**
> "We validated hardening in the evaluator's actual operating range (0.08-0.12). 
> The mechanisms (noise, quantization, rate limiting) are range-agnostic and 
> function correctly where the evaluator produces signal. Testing hypothetical 
> ranges where the evaluator doesn't operate would be methodologically unsound."

---

## Posicionamiento Estratégico

**Frame correcto:**
- ✅ "Conservative by design"
- ✅ "Validity-focused"
- ✅ "Security-first approach"

**Frame incorrecto:**
- ❌ "Limited"
- ❌ "Incomplete"
- ❌ "Needs improvement"

---

## Relación con Otros Benchmarks

**Comparación honesta:**

| Benchmark | Scoring | Inference Risk |
|-----------|---------|----------------|
| MMLU | Accuracy (binary) | Low |
| HellaSwag | Accuracy (binary) | Low |
| **EDB (beta)** | **Validity (near-binary)** | **Low** |
| HumanEval | Pass@k (discrete) | Low |
| AlpacaEval | Win rate (comparative) | Medium |

**Mensaje:** EDB está en buena compañía. La mayoría de benchmarks serios usan scoring discreto/binario.

---

## Frase Canónica para Documentación

**Usar en:**
- Paper (Limitations)
- README de API
- Documentación técnica

**Texto:**
```
The current evaluator prioritizes validity detection over quality gradation. 
Continuous scoring is an explicit non-goal of the public beta.
```

**Razón:** Clara, honesta, no defensiva, no promete nada.

---

**Public Document — Energy Green Data.**

*This document is part of the public EDB benchmark. It may be freely distributed and referenced under the terms of the CC BY 4.0 license.*

**Last updated:** 2026-01-13  
**Updated by:** EDB Research Team  
**Document version:** 1.0.0

---

<p align="center">
<img src="./assets/EGD.png" width="200">
<br>
<strong>Energy Green Data - Public Project</strong>
<br>
© 2026 - Energy Decision Benchmark
<br>
<em>Public document - Open access</em>
</p>
