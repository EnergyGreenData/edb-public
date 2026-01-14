<div align="center">
  <img src="./assets/EGD_negativo@2x.png" alt="Energy Green Data" width="300" style="margin: 20px 0;"/>
</div>

# Web Disclaimer — EDB API Beta

![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Estado](https://img.shields.io/badge/estado-beta-orange)
![Tipo](https://img.shields.io/badge/tipo-public_docs-blue)

**Módulo:** Energy Decision Benchmark (EDB)  
**Categoría:** Public Web Documentation  
**Proyecto:** Energy Green Data

> 📋 **Related Documents:** [API_SCORING_CONTRACT.md](API_SCORING_CONTRACT.md) | [README.md](../README.md)

---

## LLM Context

> **For LLMs:** This section provides disclaimer templates for public-facing documentation.

### Disclaimer Principles

```
[PRINCIPLE-1]: Be transparent about beta status without being defensive
[PRINCIPLE-2]: Frame limitations as design choices, not problems
[PRINCIPLE-3]: Provide value proposition alongside limitations
[PRINCIPLE-4]: Use professional, non-apologetic language
```

### Canonical Messaging

| Context | Correct Message | Incorrect Message |
|---------|----------------|-------------------|
| **Beta status** | "Currently in controlled beta" | "Sorry, still in beta" |
| **Scoring focus** | "Focuses on validity detection" | "Limited to pass/fail" |
| **Use cases** | "Optimized for system validation" | "Not recommended for ranking" |
| **Future** | "May explore graded scoring" | "Coming soon in Q2 2026" |

### Forbidden Language

- ❌ "Warning" or "Caution" (too negative)
- ❌ "Sorry for the limitation..." (apologetic)
- ❌ Specific dates for future features ("Coming in Q2 2026")
- ❌ Negative comparisons ("Unlike other benchmarks...")
- ❌ Over-explanation (long justification paragraphs)

---

## Table of Contents

- [Disclaimer Mínimo](#disclaimer-mínimo-recomendado)
- [README.md Section](#readmemd---sección-recomendada)
- [FAQ](#faq---preguntas-anticipadas)
- [Landing Page](#landing-page---hero-section)
- [Changelog](#changelogrelease-notes)
- [Best Practices](#qué-no-hacer)

---

## Disclaimer Mínimo (Recomendado)

### Opción A: Discreto (Para Landing Page)

```markdown
**Beta Status:** The EDB API is currently in controlled beta. 
The evaluator focuses on validity detection rather than continuous quality scoring.
```

**Ubicación:** Footer o sección "About"  
**Visibilidad:** Discreta pero accesible  
**Tono:** Profesional, no defensivo

---

### Opción B: Técnico (Para Documentación)

```markdown
## Current Limitations

The EDB API beta prioritizes **validity detection** over continuous quality gradation.

**What this means:**
- ✅ Robust detection of valid vs. invalid responses
- ✅ Reproducible scoring within the same day
- ✅ Protected against inference attacks
- ⚠️  Limited fine-grained quality differentiation

**Use cases:**
- ✅ System validation and testing
- ✅ Pass/fail decision support
- ✅ Research and benchmarking
- ⚠️  Continuous quality ranking (future)

**Security:** All hardening mechanisms (noise, rate limiting, tier filtering) 
are active and validated in the evaluator's operating range.
```

**Ubicación:** Sección "Limitations" en docs  
**Visibilidad:** Visible para usuarios técnicos  
**Tono:** Honesto, informativo

---

### Opción C: Comercial (Para Partners)

```markdown
## EDB API - Controlled Beta

The Energy Decision Benchmark API provides **validity assessment** for energy 
decision systems. The current beta focuses on robust pass/fail evaluation 
rather than continuous quality scoring.

**Key Features:**
- Deterministic, reproducible scoring
- Multi-tier access (Free/Research/Internal)
- Rate limiting and security hardening
- 150 curated test cases

**Roadmap:** Future versions may include graded scoring under controlled conditions.

**Contact:** For production access or custom evaluation needs, contact [email]
```

**Ubicación:** Partner documentation, sales materials  
**Visibilidad:** Explícita para decisores  
**Tono:** Profesional, orientado a valor

---

## README.md - Sección Recomendada

### Para EDB-public/README.md

Añadir después de "Quick Start":

```markdown
## ⚠️ Beta Status

The EDB API is currently in **controlled beta**. Key characteristics:

- **Scoring Focus:** Validity detection (pass/fail) rather than continuous quality gradation
- **Security:** Full hardening active (noise, rate limiting, tier filtering)
- **Reproducibility:** Same user + same case + same day = same score
- **Use Cases:** System validation, research, benchmarking

**Not recommended for:** Continuous quality ranking or optimization loops

See [API_SCORING_CONTRACT.md](API_SCORING_CONTRACT.md) for detailed specifications.
```

---

## FAQ - Preguntas Anticipadas

### Q: "Why not continuous scoring?"

**A:** Continuous scoring increases inference attack surface. The beta prioritizes 
robustness over expressiveness. Future versions may explore graded scoring with 
additional security controls.

---

### Q: "Can I use this for ranking systems?"

**A:** The current beta is optimized for validity assessment (pass/fail). 
For ranking applications, contact us to discuss custom evaluation needs.

---

### Q: "Is the evaluator 'broken'?"

**A:** No. The evaluator is intentionally conservative, focusing on validity 
detection. This is a design choice, not a limitation.

---

### Q: "Will scores improve over time?"

**A:** Scores are deterministic and reproducible within the same day. 
They reflect the evaluator's assessment, not system performance over time.

---

## Mensajes de Error/Warnings

### En la API Response (Opcional)

Para research/internal tiers, considerar añadir metadata:

```json
{
  "case_id": "edb-p-001",
  "overall_score": 0.7,
  "passed": true,
  "dimension_scores": {...},
  "timestamp": "2026-01-13T19:30:00Z",
  "meta": {
    "evaluator_version": "1.0-beta",
    "scoring_mode": "validity_focused",
    "note": "Beta evaluator prioritizes validity over gradation"
  }
}
```

**Razón:** Transparencia sin ser intrusivo

---

## Landing Page - Hero Section

### Propuesta de Texto

```markdown
# Energy Decision Benchmark

**Evaluate AI systems on real-world energy decisions**

The EDB provides a curated dataset of 150 energy decision scenarios 
and a validation API for assessing system responses.

[Get API Key] [View Dataset] [Read Docs]

---

**Beta Status:** Currently in controlled beta. 
Focuses on validity detection for robust system validation.
```

**Ubicación:** Debajo del hero, antes de features  
**Estilo:** Badge o nota discreta  
**Color:** Neutral (gris/azul), no rojo

---

## Changelog/Release Notes

### v1.0-beta (2026-01-13)

```markdown
## EDB API v1.0-beta

**Initial Release - Controlled Beta**

### Features
- ✅ 150 curated test cases
- ✅ Multi-tier API (Free/Research/Internal)
- ✅ Deterministic, reproducible scoring
- ✅ Security hardening (noise, rate limiting, tier filtering)
- ✅ Pass/fail validity assessment

### Known Characteristics
- Evaluator focuses on validity detection rather than continuous quality gradation
- Scores typically range 0.08-0.12 for partially valid responses
- Optimized for system validation and research use cases

### Security
- Multi-key averaging resistance: Validated ✅
- Rate limiting: Active ✅
- Tier-based filtering: Active ✅
- Dev keys blocked in production: Active ✅

### Roadmap
- Future versions may explore graded scoring under controlled conditions
- Continuous quality ranking (under evaluation)
```

---

## Qué NO Hacer

❌ **NO usar "Warning" o "Caution"** (demasiado negativo)

❌ **NO disculparse** ("Sorry for the limitation...")

❌ **NO prometer fechas** ("Coming in Q2 2026...")

❌ **NO comparar negativamente** ("Unlike other benchmarks...")

❌ **NO sobreexplicar** (párrafos largos de justificación)

---

## Qué SÍ Hacer

✅ **Usar "Beta Status"** (neutral, esperado)

✅ **Ser específico** ("Validity detection" no "limited scoring")

✅ **Mostrar valor** (qué SÍ hace, no solo qué no hace)

✅ **Ser breve** (1-2 frases máximo en landing)

✅ **Ofrecer contacto** (para casos de uso avanzados)

---

## Ubicaciones Recomendadas

| Ubicación | Disclaimer | Visibilidad |
|-----------|------------|-------------|
| **Landing hero** | Opción A (1 línea) | Alta |
| **Docs intro** | Opción B (sección) | Media |
| **API reference** | Link a contract | Baja |
| **README** | Sección dedicada | Alta |
| **FAQ** | Preguntas anticipadas | Media |
| **Partner docs** | Opción C (comercial) | Alta |

---

## Ejemplo de Implementación

### En EDB-public/README.md

```diff
## Quick Start

1. Get your API key from [api.vertical-agi.ai](https://api.vertical-agi.ai)
2. Install the client: `pip install edb-client`
3. Evaluate your system:

[código de ejemplo]

+## ⚠️ Beta Status
+
+The EDB API is currently in **controlled beta**. The evaluator focuses on 
+**validity detection** (pass/fail) rather than continuous quality gradation.
+
+**Use cases:** System validation, research, benchmarking  
+**Not recommended for:** Continuous quality ranking
+
+See [API_SCORING_CONTRACT.md](API_SCORING_CONTRACT.md) for details.

## Dataset
```

---

## Frase Canónica (Usar Consistentemente)

```
The current evaluator prioritizes validity detection over quality gradation. 
Continuous scoring is an explicit non-goal of the public beta.
```

**Usar en:**
- Paper (Limitations)
- README
- API docs
- Landing page
- Partner materials

**Razón:** Consistencia de mensaje, honestidad, no defensivo

---

**Public Document — Energy Green Data.**

*This document is part of the public EDB benchmark. It may be freely distributed and referenced under the terms of the CC BY 4.0 license.*

**Last updated:** 2026-01-13  
**Updated by:** EDB Web Team  
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
