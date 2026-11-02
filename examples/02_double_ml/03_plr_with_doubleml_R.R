# Optional R counterpart for the Python PLR teaching example.
# Install: install.packages(c("DoubleML", "mlr3", "mlr3learners", "ranger"))
# Run:     Rscript examples/02_double_ml/03_plr_with_doubleml_R.R
# This is a learning example; real data require a separate identification audit.

library(DoubleML)
library(mlr3)
library(mlr3learners)

set.seed(2026)
n <- 2000
x1 <- rnorm(n)
x2 <- rnorm(n)
x3 <- rnorm(n)
m0 <- 0.9*x1 - 0.8*x2 + 0.7*sin(x3) + 0.4*x1*x2
d <- m0 + rnorm(n)
h0 <- 1.2*x1 - 0.5*x2^2 + 0.8*sin(x3) + 0.4*x1*x2
y <- 2.0*d + h0 + rnorm(n)
dat <- data.frame(y=y, d=d, x1=x1, x2=x2, x3=x3)

data_dml <- DoubleMLData$new(dat, y_col="y", d_cols="d", x_cols=c("x1", "x2", "x3"))
rf <- lrn("regr.ranger", num.trees=200, min.node.size=5)
fit <- DoubleMLPLR$new(data_dml, ml_l=rf, ml_m=rf, n_folds=5)
fit$fit()
print(fit$summary())
cat("True causal effect: 2.0\n")
