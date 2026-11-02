# Module 01 — Foundations of causal inference

## Learning target
Given a research question, define the causal estimand, draw the DAG, state the assumptions that identify it and choose an estimator **only after** those steps.

## Basic notation
- D: treatment/exposure; Y: outcome; X: measured pretreatment covariates.
- Y(1), Y(0): potential outcomes under binary treatment.
- ATE = E[Y(1) - Y(0)].
- ATT = E[Y(1) - Y(0) | D = 1].
- Consistency: observed Y equals the potential outcome under received D.
- Conditional exchangeability: (Y(0), Y(1)) ⟂ D | X.
- Positivity: comparison groups exist at every relevant value of X.

## Practice
1. Draw a DAG with X -> D, X -> Y and D -> Y.
2. Run \`python examples/01_foundations/01_confounding.py\`.
3. Explain why naive OLS is confounded in this simulation.
4. Compare linear adjustment with the nonlinear synthetic data-generating process.
5. Suggest a post-treatment variable and explain why controlling for it can harm interpretation of a total effect.

## Extensions
Randomized trials, selection on observables, matching, inverse propensity weighting, instrumental variables, regression discontinuity, DiD, staggered treatment, mediation and interference are future modules.
