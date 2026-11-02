# Study 01 — BLSM 2013 and household economic welfare (IFLS4–IFLS5)

**Status:** Audit initiated; data not yet inspected; no model fitted.

**Code and private data workspace:** the owner's separate IFLS project (the RStudio \`IFLS_Project.Rproj\`). Data must stay local. The audit scripts there live in \`02_scripts/10_blsm_2013/\`, with \`03_notebooks/02_blsm_2013_ifls4_ifls5_audit.Rmd\`.

## 1. Target question and estimands

Did receiving **2013 BLSM** affect later household economic welfare among actual beneficiaries, compared to the counterfactual in which they did not receive it?

- Treatment \`D=1\`: verified household receipt of the **2013** BLSM program. IFLS5 Book 1 KSR3TYPE column C records BLSM, KSR17 records receipt, KSR18 the first receipt date, and KSR22 the last receipt date. Program and date coding need auditing.
- Outcome: change in **real monthly household consumption per capita**, based on harmonized IFLS4 (2007–08) and IFLS5 (2014–15) expenditure aggregates. This is a *longer-run* effect, not the immediate effect during 2013.
- ATT at follow-up: \`E[Y_5(1)-Y_5(0)|D=1]\` for a carefully defined population of beneficiary households (or anchored baseline members).
- Subgroup ATT: \`E[Y_5(1)-Y_5(0)|D=1,G=g]\` for a **baseline-defined** subgroup \`G\`. It is not the population CATE \`E[Y(1)-Y(0)|X=x]\`.
- Potential subgroups: baseline welfare quintiles; 2007 urban/rural status; baseline household composition. Use “poor/near-poor” only when tied to a defensible region-year poverty threshold.

We must choose what the unit and treatment mean if a 2007 household divides into several 2014 households. The first sample could be stable-household pairs; report the selection consequence and estimate a person-anchored sensitivity analysis if feasible.

## 2. Chronology / contamination

- IFLS4: fielded 2007–08 (pre-2013).
- BLSM 2013: launched after the June 22 fuel subsidy change. SMERU reports disbursements June/July and September/October 2013.
- IFLS5: fielded 2014–15; another cash-transfer round started in November 2014, overlapping fieldwork for some respondents.
- Treatment should be linked to first/last receipt dates and interview dates, with explicit ambiguous/late-exposure categories.
- Older BLT programs and concurrent PKH/BSM/Raskin may affect baseline welfare, selection into BLSM, and subsequent welfare. Specify whether the estimand is the effect of BLSM *as delivered with other programs*, or a restrictive isolated exposure regime; do not indiscriminately condition on post-treatment assistance.

## 3. Audit before identification

| Gate | Required evidence |
|---|---|
| Transfer | Verified BLSM vs BLT/PKH KSR3TYPE code, KSR17 yes/no, first/last payment dates, unknown status, program-record coverage |
| Panel | PTRACK14/HTRACK14 linkage counts and split-offs; household versus person-anchor definition; actual matched sample |
| Outcome | Documented KS1 weekly food, KS2 monthly nonfood, KS3 yearly nonfood, KS0 and housing/education; consistent period conversion and inclusion rules; no double counts |
| Price comparability | Interview dates, time-specific CPI, spatial price differences, household-size adjustment, nominal-to-real deflation |
| Pretreatment X | 2007 welfare, assets, family size, education, work, residence, baseline assistance; missingness and timing |
| Treatment selection | Treated-control descriptive balance, overlap, empirical propensity distributions, effective sample size |
| Attrition | Household loss, tracking movement, missing outcome, reinterview/weight diagnostics |
| Additional programs | Prior BLT and PKH/BSM/Raskin; timing and possible effect modification |
| Sample size | Recipients and controls with fully observed baseline, follow-up and subgroup membership |

## 4. Candidate identification and estimator

A two-wave **doubly robust panel Difference-in-Differences ATT** (Python: current `DoubleMLDID` or `differences`) is a sensible *candidate*, not an automatic solution.

Let \`ΔY=Y_5-Y_4\`. Identification for the eligible treated population requires an **observed-covariate conditional parallel trends assumption**:

\`E[ΔY(0)|D=1,X] = E[ΔY(0)|D=0,X]\`.

Also assess no anticipation, consistency, positivity, no interference, missing-outcome assumptions, and meaningful comparability of the consumption measures.

Initial estimator order:
1. Descriptive change by treatment group, baseline balance and overlap; not yet causal.
2. Covariate-adjusted panel DiD.
3. Doubly robust DiD ATT (e.g. R \`DRDID\`), with justified uncertainty and sampling/cluster design.
4. Prespecified subgroup ATT, with multiple-testing and small-cell awareness.
5. More flexible nuisance learning and cross-fitting if support/sample size allow; compare with simpler specifications.

Only two waves means **parallel trends cannot be directly examined with multiple pre-2013 measures**. IFLS3 may be used later for compatible welfare items as a design extension, but does not solve all selection problems by itself. Fuel-price shock heterogeneity and nonrandom welfare targeting remain threats.

**LATE is not a default extension.** Social Protection Card possession or a propensity score is not an automatically valid instrument. A credible administrative rule, exclusion, relevance, monotonicity and assignment population would need to be demonstrated separately.

## 5. Why RAPSEM is a separate phase

RAPSEM estimates **controlled direct and mediator effects of a latent mediator**. It does not estimate an ATT by default. If the total-effect ATT study is credible, a mediation extension would still require:

1. A defensible treatment assignment/ignorability model (or new observational identifying argument).
2. A mediator *after BLSM, before the later welfare outcome*, measured with valid latent indicators. Two waves may not suffice.
3. Baseline \`X\` and at least one relevant treatment-by-\`X\` interaction which affects the mediator but not the outcome directly under the structural model; the exclusion restriction cannot be certified by an F-test.
4. No unobserved effect modification as required by the RAPSEM framework, plus correct measurement model and measurement-error correction.
5. A validated estimator for observational settings with proper uncertainty quantification, not simply feeding DML propensity scores into \`rapsem::med_est\`.

**Household consumption per capita is a constructed welfare index**, not automatically a reflective latent factor. If we use RAPSEM, a suitable multi-indicator *mediator* may be latent; the welfare outcome could remain observed only if the method and measurement implementation support that specification. A separate time-resolved mediator is the limiting data requirement.

## 6. Decisions after first local audit

- Report exact count of 2013 recipients, unknown/2014 statuses, and observed support.
- Choose household-lineage or person-anchored analysis population.
- Choose and document the harmonized real welfare aggregate and price base.
- Check whether treatment and outcome data are sufficient for ATT and baseline subgroup ATT.
- If any key gate fails, revise design instead of forcing a treatment-effect model.
- Open a separate methodological issue for observational RAPSEM only after an intermediate mediator and structural identification route are established.

## Primary sources

- [RAND IFLS5 Household Questionnaire, Book 1 KSR](https://www.rand.org/content/dam/rand/pubs/working_papers/WR1100/WR1143z3/RAND_WR1143z3.pdf)
- [RAND IFLS5 User's Guide](https://www.rand.org/well-being/social-and-behavioral-policy/data/FLS/IFLS/ifls5.html)
- [SMERU, BLSM 2013 implementation](https://www.smeru.or.id/en/publication/use-social-protection-card-kps-and-implementation-2013-unconditional-cash-transfer)
- [Morelli, Faleh & Brandt, RAPSEM](https://arxiv.org/abs/2509.23935)

## Python-first workflow (added November 2026)

The IFLS project's [Python study audit](https://github.com/econoberries/IFLS-Socio-Economic-Data-Analysis-Project/tree/main/02_scripts/10_blsm_2013/python) now covers original Stata code/label reading, BLSM payment-year checks, roster/tracking inspection, welfare variable inventories, and interview-date metadata. It saves only aggregate tables locally. [Python notebook](https://github.com/econoberries/IFLS-Socio-Economic-Data-Analysis-Project/blob/main/03_notebooks/02_blsm_2013_ifls4_ifls5_audit_py.ipynb).

**Not yet built:** verified welfare aggregate, full household panel with sample rules, DR DiD ATT and subgroup ATT estimation. **RAPSEM** remains implemented in R by its authors; an eventual Python implementation or interface needs validation, especially for observational assignment.
