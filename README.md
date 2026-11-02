# Causal Inference Methods Lab

**From assumptions and estimands to reproducible applied analyses.**

An evolving learning and research repository focused on applied **causal inference**, **Double/Debiased Machine Learning (DML)**, and **Rank-Preserving Structural Equation Modeling (RAPSEM)**. The goal is not merely to run software, but to understand why an estimator works, when its assumptions are plausible, and what happens when they fail.

> **Guiding principle:** Identification comes before estimation. A sophisticated estimator cannot make an observational association causal by itself.

## Study modules

| Module | Question | Start here |
|---|---|---|
| 01 — Causal foundations | What is a causal estimand, and how does confounding arise? | [Foundations](docs/methods/01_foundations.md) |
| 02 — Double Machine Learning | How do orthogonal scores and cross-fitting reduce nuisance-estimation bias? | [DML](docs/methods/02_double_machine_learning.md) |
| 03 — RAPSEM | When can causal latent mediation be identified despite unobserved mediator–outcome confounding? | [RAPSEM](docs/methods/03_rapsem.md) |

## Quick start (Python 3.10+)

```bash
git clone https://github.com/econoberries/Causal-Inference-Methods-Lab.git
cd Causal-Inference-Methods-Lab

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[test]'

python examples/01_foundations/01_confounding.py
python examples/02_double_ml/01_plr_from_scratch.py
pytest -q
```

The core tutorial compares a naive, confounded regression with a cross-fitted partially linear estimator on synthetic data with a known treatment effect. The optional official DoubleML examples need additional packages; see their headers.

**RAPSEM is an R-based replication track.** Follow [the RAPSEM exercise guide](examples/03_rapsem/README.md) and the authors' own [R package](https://github.com/PsychometricsMZ/RAPSEM).

## Structure

```text
Causal-Inference-Methods-Lab/
├── docs/
│   ├── methods/                  # Theory, notation, assumptions, exercises
│   ├── research/                 # Applied case ideas and experiment logs
│   ├── method_comparison.md
│   └── roadmap.md
├── examples/
│   ├── 01_foundations/
│   ├── 02_double_ml/
│   └── 03_rapsem/
├── src/causal_methods_lab/       # Small original teaching implementations
├── tests/                        # Sanity tests for synthetic examples
└── data/                         # Data policy; no restricted datasets
```

## Workflow for every method

1. State the causal question, units, estimand, and target population.
2. Draw a DAG or write the identifying assumptions.
3. Derive or explain the moment condition and estimator.
4. Run a simulation where the causal truth is known.
5. Reproduce an official implementation or published result.
6. Investigate failure modes (bias, coverage, weak instruments, measurement error).
7. Apply the method only to a defensible empirical design.
8. Record the code, seed, settings, diagnostics, and limitations.

See the [roadmap](docs/roadmap.md) for the proposed growth path.

## Reference repositories (not copied into this repository)

- [econoberries/DoubleMLReplicationCode](https://github.com/econoberries/DoubleMLReplicationCode) — R replication simulations by Bach et al.
- [econoberries/doubleml-pipeline](https://github.com/econoberries/doubleml-pipeline) — Google's automated DML workflow.
- [econoberries/EconML](https://github.com/econoberries/EconML) — heterogeneous-effect estimation.
- [econoberries/example-causal-datasets](https://github.com/econoberries/example-causal-datasets) — possible benchmark datasets.
- [econoberries/EWMEncouragementRules-IFLS](https://github.com/econoberries/EWMEncouragementRules-IFLS) — IV-based policy-learning example with IFLS.
- [DoubleML (Python)](https://github.com/DoubleML/doubleml-for-py) and [DoubleML (R)](https://github.com/DoubleML/doubleml-for-r).
- [PsychometricsMZ/RAPSEM](https://github.com/PsychometricsMZ/RAPSEM) — authors' R package, empirical application, and simulations.

## Main readings

- Chernozhukov et al. (2018), *Double/debiased machine learning for treatment and structural parameters*. https://doi.org/10.1111/ectj.12097
- [A Guide to Double Machine Learning](https://dmlguide.github.io/)
- Bach et al. (2022), *DoubleML—An Object-Oriented Implementation of Double Machine Learning in Python*. https://jmlr.org/papers/v23/21-0862.html
- Morelli, Faleh & Brandt (2025), *Identifying Latent Mediators Without Sequential Ignorability via a Rank-Preserving Structural Equation Model*. https://arxiv.org/abs/2509.23935

## Important research boundaries

**DML is not a solution to unobserved confounding.** The introductory PLR lab assumes sufficient observed pre-treatment covariates and a partially linear structural model. **RAPSEM is not a plug-and-play mediation method for observational treatment.** Its reference identification strategy relies on randomized treatment and additional structural, interaction, and measurement assumptions. See each module before applying either estimator.

Do not upload restricted microdata (including IFLS files), individual identifiers, credentials, or licensed paper PDFs. Keep simulations separate from real research data and cite upstream authors when replicating their work.

**Status:** v0.1 starter. Original educational code; upstream software is referenced, not vendored. Python tests run automatically in GitHub Actions.
