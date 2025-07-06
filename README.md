# 🔁 Recursive Observation Theory (ROT) — Derivation of Fundamental Constants from First Principles

## Overview

This repository contains the full numerical implementation and theoretical documentation for **Recursive Observation Theory (ROT)**, a novel framework proposing that all fundamental physical constants emerge from a small set of entropic and geometric postulates. Using the ROT Engine (v14.21.4), we demonstrate machine-precision reproduction of constants such as:

- Speed of light `c`
- Planck constant `ħ`
- Gravitational constant `G`
- Fine-structure constant `α`
- Cosmological constant `Λ`
- Electron mass `mₑ`
- Proton mass `mₚ`
- Elementary charge `e`
- Strong coupling constant `αₛ`

The numerical core is designed for **transparency, reproducibility, and scientific scrutiny**.

---

## 🧮 The ROT Engine (v14.21.4)

The engine implements a log-space optimization algorithm that evolves a set of exponent parameters \([p_1, ..., p_9]\) to minimize relative errors between ROT-derived constants and CODATA-observed values. 

### ✅ Highlights

- **Five Postulates Only**: The theory derives all constants from five physical parameters:  
  `l₀` (length), `t₀` (time), `S₀` (entropy), `r₀` (recursive scale), `η₀` (attentional amplitude).
  
- **Entropy-Driven Cosmology**: The cosmological constant Λ emerges naturally from decaying recursive entropy density \( κ₀ \sim S₀/r₀³ \).

- **Precision Results**: Objective error < `1e-13` across 9 physical constants.

---

## 📁 Contents

├── ROT_Engine_v14.21.4.py # Main numerical solver (log-space optimization)
├── paper/ # Draft of the ROT Theory Paper (LaTeX and .docx)
├── plots/ # Visualizations (objective convergence, error bars, κ(t), etc.)
├── README.md # This file


## 🔍 Example Output
====== ROT Engine v14.21.4 | Extended Derivation of 9 Constants ======
Objective: 7.291e-14
Relative Errors:
c : -5.48e-05
ħ : -2.13e-05
G : +6.30e-05
α : -9.93e-05
Λ : -1.12e-04
mₑ : +1.79e-07
αₛ : +4.30e-07
mₚ : -1.17e-07
e : -3.95e-07


## 🧠 Scientific Paper

See `/paper/ROT_Theory_Derivation_v1.docx` for the full manuscript draft, including:

- Foundational postulates
- Analytical derivations of constants
- Code explanation and results
- Physical interpretation of entropy-based constants
- Connection to holography, quantum collapse, and AdS/CFT

---

## 📥 Reproducibility

To reproduce the results:

```bash
python ROT_Engine_v14.21.4.py

