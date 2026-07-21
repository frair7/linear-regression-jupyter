library(ggplot2)

args <- commandArgs(trailingOnly = TRUE)

filename <- args[1]
x_column <- args[2]
y_column <- args[3]

dataset <- read.csv(filename)

model <- lm(
  as.formula(paste(y_column, "~", x_column)),
  data = dataset
)

# Predicted values for regression line
predictions <- predict(
  model,
  newdata = dataset
)

# Regression statistics
slope <- coef(model)[2]
intercept <- coef(model)[1]
r_squared <- summary(model)$r.squared

# Predict salary at 6 years
years_to_predict <- 6

prediction_input <- data.frame(years_to_predict)
names(prediction_input) <- x_column

predicted_salary <- predict(
  model,
  newdata = prediction_input
)[1]

# Data frame for predicted point
prediction_data <- data.frame(
  x = years_to_predict,
  y = predicted_salary
)

p <- ggplot() +

  # Observed data
  geom_point(
    aes(
      x = dataset[[x_column]],
      y = dataset[[y_column]],
      colour = "Observed Data"
    ),
    size = 2.5
  ) +

  # Regression line
  geom_line(
    aes(
      x = dataset[[x_column]],
      y = predictions,
      colour = "Linear Regression"
    ),
    linewidth = 1
  ) +

  # Predicted salary point
  geom_point(
    data = prediction_data,
    aes(
      x = x,
      y = y,
      colour = "Predicted Salary at 6Y"
    ),
    shape = 8,
    size = 4,
    inherit.aes = FALSE
  ) +

  # Predicted salary text shifted left
  annotate(
    "text",
    x = years_to_predict - 0.25,
    y = predicted_salary + 2500,
    label = paste0(
      "$",
      format(
        round(predicted_salary, 2),
        big.mark = ",",
        nsmall = 2
      )
    ),
    colour = "green",
    hjust = 1
  ) +

  # Regression equation
  annotate(
    "text",
    x = 1,
    y = 70000,
    label = paste0(
      "y = ",
      round(slope, 2),
      "x + ",
      round(intercept, 2),
      "\nR² = ",
      round(r_squared, 2)
    ),
    hjust = 0
  ) +

  # Legend colors and labels
  scale_colour_manual(
    name = "",
    values = c(
      "Observed Data" = "red",
      "Linear Regression" = "blue",
      "Predicted Salary at 6Y" = "green"
    )
  ) +

  ggtitle(paste(y_column, "vs", x_column)) +
  xlab(x_column) +
  ylab(y_column)

# Save as an 8 × 6 inch plot
ggsave(
  "linear_regression_r_output.png",
  plot = p,
  width = 8,
  height = 6,
  units = "in"
)

print(summary(model))

cat(
  "R-squared:",
  round(r_squared, 3),
  "\n"
)

cat(
  "Predicted salary for",
  years_to_predict,
  "years of experience: $",
  format(
    round(predicted_salary, 2),
    big.mark = ",",
    nsmall = 2
  ),
  "\n"
)