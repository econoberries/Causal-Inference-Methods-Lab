# Growing research roadmap

This repository grows by methodological modules, with theory, exercises, simulations, replication and applications kept together.

## v0.1 — Initial working starter (included)
- [x] Repository philosophy and references
- [x] Confounding illustration with a known treatment effect
- [x] Cross-fitted partially linear DML implemented from scratch (Python)
- [x] Official DoubleML examples in Python and R
- [x] RAPSEM reproduction instructions and assumptions
- [x] Automated sanity tests for the teaching implementation

## v0.2 — Identification and causal foundations
- [ ] Potential outcomes, DAGs, SWIGs and counterfactual notation
- [ ] Exchangeability, positivity, interference and consistency
- [ ] Propensity score, IPW, standardization and doubly robust AIPW
- [ ] Selection bias, bad controls and post-treatment conditioning

## v0.3 — Double Machine Learning lab
- [ ] IRM for binary treatment: ATE and ATT
- [ ] PLIV and identification with instruments
- [ ] Reproduce selected Bach et al. simulations from the existing R fork
- [ ] Compare ML learners, repeated splits and Monte Carlo coverage
- [ ] Treatment-effect heterogeneity and sensitivity analysis

## v0.4 — RAPSEM reproduction
- [ ] Pin software to authors' reference environment
- [ ] Reproduce published simulation and empirical results
- [ ] Vary mediator–outcome confounding and measurement reliability
- [ ] Vary instrument strength and structural assumptions
- [ ] Compare bias, RMSE, coverage, power and convergence

## Future methods (order deliberately open)
- [ ] Difference-in-differences, staggered adoption and event studies
- [ ] Regression discontinuity, IV and synthetic controls
- [ ] Causal forests, meta-learners, policy learning
- [ ] Mediation analysis, latent-variable causal modeling
- [ ] Well-identified empirical case studies (no restricted data uploaded)

Open an issue before starting a new method or research question. Record decisions and experiments as the repo evolves.
