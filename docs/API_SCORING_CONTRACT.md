<div align="center">
  <img src="./assets/EGD_negativo@2x.png" alt="Energy Green Data" width="300" style="margin: 20px 0;"/>
</div>

# API Scoring Contract — EDB

![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Estado](https://img.shields.io/badge/estado-producción-green)
![Tier](https://img.shields.io/badge/tier-público-blue)

**Módulo:** Energy Decision Benchmark (EDB)  
**Categoría:** Public API Documentation  
**Proyecto:** Energy Green Data

> 📋 **Related Documents:** [METHODOLOGY.md](METHODOLOGY.md) | [WEB_DISCLAIMER.md](WEB_DISCLAIMER.md) | [PAPER_LIMITATIONS_SECTION.md](PAPER_LIMITATIONS_SECTION.md)

---

## LLM Context

> **For LLMs:** This section provides cognitive anchors for the EDB API scoring contract.

### API Invariants

```
[INV-API-1]: Reproducibility — Same user + same case + same day = same score
[INV-API-2]: No inference — Hardening prevents reconstruction of internal evaluator
[INV-API-3]: Tier-based filtering — Free/Research/Internal have different detail levels
[INV-API-4]: Traceability — All responses include timestamp and case_id
```

### Canonical Entities

| Entity | Definition | Scope |
|--------|------------|-------|
| **Free Tier** | Public access, quantized scores, generic rate limits | Open registration |
| **Research Tier** | Academic access, dimension scores, detailed limits | Approved researchers |
| **Internal Tier** | Full precision, debug info, high limits | EGD team only |
| **case_id** | Unique identifier for test case (e.g., edb-p-001) | EDB-P dataset |
| **overall_score** | Aggregated score [0.0-1.0] across all dimensions | Primary metric |
| **dimension_scores** | Individual scores per evaluation dimension | Research+ only |

### Forbidden Inferences

- ❌ Do NOT attempt to reverse-engineer the evaluator from API responses
- ❌ Do NOT assume quantization precision reveals internal thresholds
- ❌ Do NOT use multi-key averaging to reduce noise (protected)
- ❌ Do NOT probe systematically to map score space (rate limited)

---

## Table of Contents

- [Fundamental Principles](#fundamental-principles)
- [Tier Specifications](#tier-specifications)
- [Security Guarantees](#security-guarantees)
- [Reproducibility](#reproducibility)
- [Attack Resistance](#attack-resistance)
- [Known Limitations](#known-limitations)
- [Security Verdict](#security-verdict)
- [References](#references)

---

## 🎯 Principios Fundamentales

1. **Reproducibilidad por usuario y día**: Mismo usuario + mismo caso + mismo día = mismo score
2. **No inferencia del evaluador**: Hardening previene reconstrucción de función interna
3. **Información por tier**: Free/Research/Internal tienen diferentes niveles de detalle
4. **Trazabilidad**: Toda respuesta incluye timestamp y case_id

---

## 📊 Especificación por Tier

### Free Tier

**Audiencia:** Usuarios públicos, evaluación ocasional

**Request:**
```json
POST /evaluate/case
Authorization: Bearer edb_free_xxx

{
  "case_id": "edb-p-001",
  "system_response": {
    "decision": "La configuración es válida",
    "reasoning": "Cumple requisitos técnicos",
    "confidence": 0.85
  }
}
```

**Response:**
```json
{
  "case_id": "edb-p-001",
  "overall_score": 0.7,
  "passed": true,
  "dimension_scores": {},
  "timestamp": "2026-01-13T19:30:00Z"
}
```

**Características:**
- ✅ `overall_score`: Cuantizado a 0.1 precision
- ❌ `dimension_scores`: **VACÍO** (no expuesto en free tier)
- ✅ `passed`: Boolean (threshold interno)
- ✅ Ruido único por (case_id + api_key + día)
- ✅ Reproducible dentro del día

**Rate Limits:**
- 100 requests/hora
- 10 requests/hora por case_id
- 20 payloads similares/hora

**429 Response:**
```json
{
  "detail": "Too many requests. Please try again later."
}
```
*Mensaje genérico, NO expone detector*

---

### Research Tier

**Audiencia:** Investigadores, académicos, desarrollo de sistemas

**Request:** (igual que free tier)

**Response:**
```json
{
  "case_id": "edb-p-001",
  "overall_score": 0.7,
  "passed": true,
  "dimension_scores": {
    "logical_consistency": 0.9,
    "regulatory_compliance": 0.8,
    "data_sufficiency": 0.6,
    "temporal_prediction": 0.7,
    "energy_literacy": 0.5
  },
  "timestamp": "2026-01-13T19:30:00Z"
}
```

**Características:**
- ✅ `overall_score`: Cuantizado a 0.1 precision
- ✅ `dimension_scores`: **INCLUIDO** (cuantizado a 0.1)
- ✅ `passed`: Boolean
- ✅ Ruido único por (case_id + api_key + día)
- ✅ Reproducible dentro del día

**Rate Limits:**
- 1,000 requests/hora
- 50 requests/hora por case_id
- 100 payloads similares/hora

**429 Response:**
```json
{
  "detail": "Rate limit exceeded for case edb-p-001: 50 requests/hour"
}
```
*Mensaje detallado, expone razón específica*

---

### Internal Tier

**Audiencia:** Equipo interno, debugging, análisis

**Request:** (igual que otros tiers)

**Response:**
```json
{
  "case_id": "edb-p-001",
  "overall_score": 0.7234,
  "passed": true,
  "dimension_scores": {
    "logical_consistency": 0.8956,
    "regulatory_compliance": 0.7823,
    "data_sufficiency": 0.6145,
    "temporal_prediction": 0.7012,
    "energy_literacy": 0.5234
  },
  "timestamp": "2026-01-13T19:30:00Z",
  "debug_info": {
    "noise_applied": true,
    "quantization_applied": false,
    "tier": "internal",
    "api_key_hash": "sha256:abc123..."
  }
}
```

**Características:**
- ✅ `overall_score`: **SIN cuantizar** (precisión completa)
- ✅ `dimension_scores`: **SIN cuantizar**
- ✅ `debug_info`: Información adicional de debugging
- ✅ Ruido único por (case_id + api_key + día)
- ✅ Reproducible dentro del día

**Rate Limits:**
- 10,000 requests/hora
- Sin límite por case_id
- Sin límite por payload similarity

**429 Response:**
```json
{
  "detail": "Rate limit exceeded: 10000 requests/hour (global)"
}
```

---

## 🔒 Garantías de Seguridad

### 1. Ruido Controlado

**Seed determinista:**
```python
seed_string = f"{case_id}:{api_key}:{day_bucket}"
hash_val = int(hashlib.sha256(seed_string.encode()).hexdigest()[:16], 16)
```

**Propiedades:**
- ✅ Mismo usuario + mismo día = mismo ruido (reproducible)
- ✅ Diferentes usuarios = ruido diferente (NO promediable)
- ✅ Diferentes días = ruido diferente (NO promediable en tiempo)

**Nivel de ruido:**
- Free/Research: ±0.02 (2% del rango)
- Internal: Sin ruido

---

### 2. Cuantización

**Precisión por tier:**
- Free: 0.1 (10 valores posibles: 0.0, 0.1, 0.2, ..., 1.0)
- Research: 0.1 (igual que free)
- Internal: Sin cuantización (precisión completa)

**Función:**
```python
def quantize(score: float, precision: int = 1) -> float:
    return round(score * 10 ** precision) / 10 ** precision
```

---

### 3. Filtrado por Tier

**Dimension scores:**
- Free: `dimension_scores = {}` (vacío)
- Research: `dimension_scores = {...}` (cuantizado)
- Internal: `dimension_scores = {...}` (sin cuantizar)

**Razón:** Reducir superficie de ataque para inferencia

---

### 4. Rate Limiting

**Niveles de protección:**

| Límite | Free | Research | Internal |
|--------|------|----------|----------|
| Global (req/hora) | 100 | 1,000 | 10,000 |
| Por case_id (req/hora) | 10 | 50 | ∞ |
| Payload similarity (req/hora) | 20 | 100 | ∞ |

**Implementación:**
```python
rate_limiter.check_rate_limit(
    client_id=api_key_info["email"],
    case_id=request.case_id,
    payload_hash=hash_payload(request.dict()),
    limits={...}
)
```

---

### 5. Timing Jitter

**Delay aleatorio:** 5-20ms por request

**Objetivo:** Prevenir timing side-channel attacks

**Implementación:**
```python
import time
import random
time.sleep(random.uniform(0.005, 0.020))
```

---

## 📈 Reproducibilidad

### Garantía

**Mismo usuario + mismo caso + mismo día = mismo score**

**Evidencia (Test P0-C):**
```
Request 1: score = 0.0000
Request 2: score = 0.0000
Request 3: score = 0.0000
Request 4: score = 0.0000
Request 5: score = 0.0000

✅ PASS: Scores idénticos
```

### Ventana Temporal

**Bucket diario:** `YYYY-MM-DD`

**Cambio de día:**
- Scores cambian a las 00:00 UTC
- Ruido se regenera con nuevo day_bucket
- Reproducibilidad se mantiene dentro del nuevo día

---

## 🛡️ Resistencia a Ataques

### Multi-Key Averaging Attack

**Test ejecutado:** 20 API keys diferentes atacando mismo caso

**Resultados:**
```
Media:           0.0950
Desv. estándar:  0.0135
Mínimo:          0.0801
Máximo:          0.1173
Rango:           0.0372
Scores únicos:   20/20

✅ Varianza suficiente (std >= 0.01)
✅ Rango suficiente (range >= 0.03)
✅ Promediado NO reduce incertidumbre
```

**Conclusión:** Sistema resistente a multi-key averaging attack

---

### Probing Sistemático

**Protección:** Rate limiting por case_id

**Test ejecutado:** 15 requests con misma key al mismo caso

**Resultado:**
```
Requests 1-10: ✅ 200 OK
Request 11:    🚫 429 Rate Limited

✅ Bloqueado después de 10 requests/hora
```

**Conclusión:** Probing sistemático mitigado

---

### Timing Side-Channel

**Protección:** Jitter aleatorio 5-20ms

**Test ejecutado:** 100 requests midiendo tiempo de respuesta

**Resultado:**
```
Tiempo medio:    127ms
Desv. estándar:  8ms
Rango:           95-165ms

✅ Varianza suficiente para prevenir timing attacks
```

---

## ⚠️ Limitaciones Conocidas

### 1. Evaluador Rígido

**Problema:** Evaluador genera scores en rango estrecho (~0.08-0.12)

**Impacto:** Hardening solo validado en zona baja de scores

**Mitigación:** Documentado en `P1D_EVALUATOR_RIGIDITY_ISSUE.md`

**Estado:** NO bloqueante para beta controlada, SÍ para producción pública

---

### 2. Zona Media de Scores

**Test P1-D:** Zona media (0.5-0.7) falla criterio de varianza

**Causa:** Evaluador no genera scores en ese rango

**Impacto:** No se puede validar hardening en zona media/alta

**Mitigación:** Aceptar limitación y documentar

---

## 🎯 Veredicto de Seguridad

### 🟢 GO para Beta Controlada

**Aprobado para:**
- Staging interno
- Dev externo controlado (pocas keys)
- Evaluación manual supervisada

**Protecciones validadas:**
- ✅ Dev keys bloqueadas en prod
- ✅ Rate limiting por api_key
- ✅ Reproducibilidad dentro del día
- ✅ Multi-key averaging mitigado (zona baja)
- ✅ 429 genérico en free tier
- ✅ /docs cerrado en producción

---

### 🟡 NO-GO para Producción Pública

**Razón:** Hardening solo validado en zona baja de scores

**Acción requerida:**
- Ajustar evaluador para generar scores continuos (0.2-1.0)
- Re-ejecutar TEST-7 en 3 zonas
- Validar hardening en todo el rango

**O alternativamente:**
- Documentar limitación explícitamente
- Aprobar con disclaimer de "beta"

---

## 📚 Referencias

- `P0_P1_CHECKLIST_STATUS.md` - Estado checklist pre-producción
- `P1D_EVALUATOR_RIGIDITY_ISSUE.md` - Problema evaluador rígido
- `SECURITY_AUDIT_REPORT.md` - Auditoría de seguridad completa
- `tests/test_p0_checklist.py` - Tests P0-A/B/C
- `tests/test_multikey_attack.py` - TEST-7 original
- `tests/test_multikey_zones.py` - TEST-7 en 3 zonas

---

**Public Document — Energy Green Data.**

*This document is part of the public EDB benchmark. It may be freely distributed and referenced under the terms of the CC BY 4.0 license.*

**Last updated:** 2026-01-13  
**Updated by:** EDB Security Team  
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
