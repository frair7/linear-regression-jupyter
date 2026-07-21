#!/usr/bin/env Rscript
# Linear regression analysis of salary versus years of experience.

script_dir <- if (sys.nframe() == 0) {
  dirname(normalizePath(sub("--file=", "", commandArgs(trailingOnly = FALSE)[grep("--file=", commandArgs(trailingOnly = FALSE))][1])))
} else {
  "."
}

data_file <- file.path(script_dir, "regression_data.csv")
output_file <- file.path(script_dir, "linear_regression_r_output.png")

x_column <- "YearsExperience"
y_column <- "Salary"
predict_years <- 6

format_currency <- function(value) {
  paste0("$", format(round(value), big.mark = ",", scientific = FALSE, trim = TRUE))
}

if (!file.exists(data_file)) {
  cat(sprintf("Error: file not found: %s\n", data_file))
  quit(status = 1)
}

data <- read.csv(data_file, stringsAsFactors = FALSE)

if (!(x_column %in% names(data)) || !(y_column %in% names(data))) {
  cat(sprintf("Error: required columns not found in %s\n", basename(data_file)))
  cat(sprintf("Available columns: %s\n", paste(names(data), collapse = ", ")))
  quit(status = 1)
}

formula <- as.formula(paste(y_column, "~", x_column))
model <- lm(formula, data = data)

coefs <- coef(model)
intercept <- unname(coefs[1])
slope <- unname(coefs[2])
r2 <- summary(model)$r.squared
predicted_salary <- as.numeric(predict(model, newdata = data.frame(YearsExperience = predict_years)))
equation <- sprintf("Salary = %.4f + %.4f * YearsExperience", intercept, slope)

cat("Linear Regression Results\n")
cat(paste(rep("-", 40), collapse = ""), "\n", sep = "")
cat(sprintf("Slope: %.4f\n", slope))
cat(sprintf("Intercept: %.4f\n", intercept))
cat(sprintf("Regression equation: %s\n", equation))
cat(sprintf("R-squared: %.4f\n", r2))
cat(sprintf(
  "Predicted salary at %g years of experience: %.2f\n",
  predict_years,
  predicted_salary
))

x_vals <- data[[x_column]]
y_vals <- data[[y_column]]
x_line <- seq(min(x_vals), max(x_vals), length.out = 100)
y_line <- intercept + slope * x_line

png(output_file, width = 1200, height = 600, res = 150)
par(
  mar = c(5, 5, 4, 2),
  bg = "#FAFAFA",
  fg = "#2C3E50",
  col.axis = "#2C3E50",
  col.lab = "#2C3E50",
  col.main = "#2C3E50",
  font.lab = 2,
  font.main = 2,
  las = 1
)

plot(
  x_vals,
  y_vals,
  pch = 19,
  cex = 1.35,
  col = adjustcolor("#2E86AB", alpha.f = 0.85),
  xlab = "Years of Experience",
  ylab = "Salary ($)",
  main = "Linear Regression: Salary vs Years of Experience",
  panel.first = grid(col = "#D5D8DC", lty = "dashed")
)

lines(x_line, y_line, col = "#C0392B", lwd = 2.5)
points(
  predict_years,
  predicted_salary,
  pch = 21,
  bg = "#F39C12",
  col = "#2C3E50",
  cex = 2.2,
  lwd = 1.5
)

text(
  predict_years + 0.35,
  predicted_salary + 3500,
  labels = paste0("Predicted salary: ", format_currency(predicted_salary)),
  pos = 4,
  font = 2,
  cex = 0.95,
  col = "#2C3E50"
)

stats_label <- paste0(
  sprintf("Salary = %s + %s × YearsExperience", format(intercept, big.mark = ",", nsmall = 2), format(slope, big.mark = ",", nsmall = 2)),
  sprintf("\nR² = %.4f", r2)
)
legend(
  "bottomright",
  legend = c("Observed data", "Fitted regression line", sprintf("Prediction at %g years", predict_years)),
  col = c("#2E86AB", "#C0392B", "#F39C12"),
  pch = c(19, NA, 21),
  lty = c(NA, 1, NA),
  lwd = c(NA, 2.5, NA),
  pt.bg = c(NA, NA, "#F39C12"),
  pt.cex = c(1.2, NA, 1.6),
  bty = "n",
  cex = 0.95
)
rect(
  grconvertX(0.02, "npc"),
  grconvertY(0.98, "npc"),
  grconvertX(0.46, "npc"),
  grconvertY(0.84, "npc"),
  col = adjustcolor("white", alpha.f = 0.95),
  border = "#CCCCCC"
)
text(
  grconvertX(0.03, "npc"),
  grconvertY(0.965, "npc"),
  labels = stats_label,
  adj = c(0, 1),
  cex = 0.95
)

dev.off()

cat(sprintf("Saved regression plot to %s\n", basename(output_file)))
