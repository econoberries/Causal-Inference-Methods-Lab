# RAPSEM replication track (R)

The initial task is to **reproduce the authors' work**, not write a speculative new estimator.

1. Clone https://github.com/PsychometricsMZ/RAPSEM alongside this repository.
2. Read the upstream README and install the \`rapsem\` R package in the recommended reproducible environment.
3. Run \`emperical_example/run_all.sh\` from the upstream root (upstream spelling).
4. Start with a single simulation setting before running the full Monte Carlo study.
5. Save reproducibility notes using [our experiment log template](../../docs/research/experiment_log_template.md).

## Discussion questions
- Why does the treatment need to be randomized in the reference design?
- Under what conditions can treatment–covariate interactions serve as identifying variation?
- What does no unobserved effect modification mean?
- How do latent factor scores introduce measurement error?
- What is the role of the method-of-moments correction?
- How do weak interaction instruments or model violations affect results?
- Under what assumptions can mediation effects be interpreted causally?

The upstream project includes its own code, simulation studies and empirical illustration. **We reference rather than vendor it**; cite the authors for any replicated results.
