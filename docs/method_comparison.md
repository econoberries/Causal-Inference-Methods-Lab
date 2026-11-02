# Estimators versus identification assumptions

| Method | Typical setting | Core identifying assumptions | Learning application |
|---|---|---|---|
| Backdoor adjustment | Observational treatment | Conditional exchangeability, consistency and positivity | Simulate confounding |
| DML: PLR | Observational partially linear model | Exogeneity conditional on X; structural PLR model; nuisance-rate requirements | Recover known constant effect |
| DML: IRM / AIPW | Binary treatment | Conditional exchangeability, overlap, valid orthogonal scores | Later: ATE and ATT |
| DML: PLIV | Instrumental-variable setting | Relevance, exclusion and exogeneity of instruments (and model restrictions) | Later: endogenous treatment |
| RAPSEM | Randomized treatment, latent mediator | Randomization; rank-preserving structural restrictions; no unobserved effect modification; valid treatment-covariate interaction restrictions; measurement assumptions | Latent mediation despite mediator–outcome confounding |

This is an orientation table, not a sufficient checklist for applying a method.
**Can a model be fit?** is not the same question as **does the estimand identify the desired causal effect?**

The DML and RAPSEM modules should be compared in terms of what they identify, what assumptions differ, and which empirical designs support them. Neither method automatically makes observational data causal.
