# Module 02 — Double/Debiased Machine Learning

## Key readings
- Chernozhukov et al. (2018), *The Econometrics Journal* 21, C1–C68: https://doi.org/10.1111/ectj.12097
- Bach et al. (2022), *JMLR* 23(53): https://jmlr.org/papers/v23/21-0862.html
- Official DoubleML documentation: https://docs.doubleml.org/
- Applied DML guide: https://dmlguide.github.io/

## First example: partially linear regression (PLR)

We begin with:

\`\`\`text
Y = theta_0 * D + g_0(X) + epsilon;   E[epsilon | D, X] = 0
D = m_0(X) + V;                      E[V | X] = 0
\`\`\`

Fit the *nuisance functions* l_0(X) = E[Y|X] and m_0(X) = E[D|X]. Note that l_0(X) is not g_0(X). The orthogonal moment equation uses:

\`\`\`text
psi(W; theta, eta) = (D - m(X)) * [Y - l(X) - theta*(D - m(X))]
\`\`\`

At the true nuisance functions, the moment is insensitive to small first-order nuisance estimation errors (Neyman orthogonality), under regularity conditions. **Cross-fitting** trains the nuisance models on other observations and predicts on held-out folds.

## Practical exercises
1. Generate a dataset with true theta = 2.
2. Estimate naive OLS (Y on D) and explain the confounding.
3. Fit nuisance ML models using 5-fold cross-fitting.
4. Compute held-out residuals for Y and D.
5. Solve for theta using the ratio of residual products to residualized-treatment sum of squares.
6. Calculate the iid orthogonal-score plug-in standard error.
7. Compare with the official DoubleMLPLR Python or R implementation.
8. Change sample size, nuisance learner, fold count and data-generating process; assess bias and coverage.

## Key caveats
- DML does not itself identify a causal effect; **unobserved confounding remains** under this PLR setup.
- PLR imposes a partially linear constant effect. Binary treatments with heterogeneous effects call for separate IRM/AIPW designs.
- The teaching implementation provides a single-split iid plug-in SE, not cluster-robust or panel-data inference.
- Good prediction of nuisance functions does not replace overlap and causal design checks.

## Next
IRM, PLIV, repeated cross-fitting, effect heterogeneity, formal sensitivity analyses, and the Bach et al. R simulation replications.
