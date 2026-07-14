#!/usr/bin/env Rscript
# Fit a simple linear regression and save a scatter plot with regression line.

args <- commandArgs(trailingOnly = TRUE)

if (length(args) != 3) {
  cat("Usage: Rscript regression_plot.R <filename> <x_column> <y_column>\n")
  quit(status = 1)
}

filename <- args[1]
x_column <- args[2]
y_column <- args[3]

if (!file.exists(filename)) {
  cat(sprintf("Error: file not found: %s\n", filename))
  quit(status = 1)
}

data <- read.csv(filename, stringsAsFactors = FALSE)

if (!(x_column %in% names(data)) || !(y_column %in% names(data))) {
  cat(sprintf("Error: columns must exist in %s\n", filename))
  cat(sprintf("Available columns: %s\n", paste(names(data), collapse = ", ")))
  quit(status = 1)
}

formula <- as.formula(paste(y_column, "~", x_column))
model <- lm(formula, data = data)

r2 <- summary(model)$r.squared
rmse <- sqrt(mean(residuals(model)^2))

x_vals <- data[[x_column]]
y_vals <- data[[y_column]]

output_name <- sprintf("%s_regression_plot_r.png", tools::file_path_sans_ext(basename(filename)))

png(output_name, width = 800, height = 600, res = 150)
plot(
  x_vals,
  y_vals,
  xlab = x_column,
  ylab = y_column,
  main = sprintf("Linear Regression: %s vs %s", y_column, x_column),
  pch = 19,
  col = adjustcolor("steelblue", alpha.f = 0.7)
)
abline(model, col = "red", lwd = 2)
legend(
  "topleft",
  legend = c("Observations", "Regression line"),
  col = c("steelblue", "red"),
  pch = c(19, NA),
  lty = c(NA, 1),
  lwd = c(NA, 2),
  bty = "n"
)
mtext(sprintf("R² = %.4f | RMSE = %.4f", r2, rmse), side = 3, line = 0.2, adj = 0)
dev.off()

cat(sprintf("Saved regression plot to %s\n", output_name))
cat(sprintf("R-squared: %.4f\n", r2))
cat(sprintf("RMSE: %.4f\n", rmse))
