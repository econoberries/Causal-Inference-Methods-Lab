# Module 03 — RAPSEM: Latent causal mediation

**Paper:** Morelli, S., Faleh, R. & Brandt, H. (2025), *Identifying Latent Mediators Without Sequential Ignorability via a Rank-Preserving Structural Equation Model*. https://arxiv.org/abs/2509.23935

**Reference implementation:** https://github.com/PsychometricsMZ/RAPSEM

## Motivation
Conventional mediation models often need sequential ignorability, including no unmeasured confounding between the mediator and outcome after conditioning on baseline variables and treatment. That can be implausible. With *latent* mediators, measurement error creates additional challenges.

## Broad idea
The authors combine factor-score estimation, G-estimation, treatment-by-covariate interactions and a method-of-moments correction for measurement error. The interactions can identify effects under a rank-preserving structural model **if** the relevant restrictions hold.

The published approach relies on **randomized treatment**, no unobserved effect modification and instrument-like treatment–covariate interaction assumptions. It is not a general cure for unobserved mediator–outcome confounding.

## Applied learning sequence
1. Read the paper's estimands and the identifying restrictions.
2. Inspect the authors' R package and analysis scripts.
3. Reproduce the official empirical example with pinned software versions.
4. Reproduce one simulation cell without mediator–outcome confounding and one with confounding.
5. Compare standard SEM, uncorrected factor-score regression and RAPSEM.
6. Vary treatment-by-covariate interaction strength, sample size, mediator reliability and model violations.
7. Report bias, RMSE, confidence interval coverage, power and convergence.
8. Discuss whether a proposed real-world study meets the required design assumptions.

## Important applicability boundary
Observational school-track choice (e.g., SMK vs SMA in IFLS) is **not randomized**. We cannot simply apply the reference RAPSEM estimator as if it were. A new application needs credible exogenous treatment assignment or a justified extension of the theory, alongside valid interaction restrictions.

## Illustrative authors' API (R; after installing their package)
\`\`\`r
model <- "
  cov =~ x1 + x2 + x3
  med =~ m1 + m2 + m3
  out =~ y1 + y2 + y3
  med ~ treat + cov + treat:cov
  out ~ treat + med + cov
"
fit <- rapsem::med_est(model, data, treat_names = "treat")
fit$summary$gestimation
fit$summary$standard
\`\`\`

See [our RAPSEM replication guide](../../examples/03_rapsem/README.md). The official repository contains \`rapsem/\`, \`simulation_study/\`, and \`emperical_example/\` (upstream spelling). Prefer its documented Nix/R environment for exact reproducibility.
