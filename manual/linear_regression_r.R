library(ggplot2)
args <- commandArgs(trailingOnly = TRUE)

filename <- args[1]
x_column <- args[2]
y_column <- args[3]

dataset <- read.csv(filename)

model <- lm(as.formula(paste(y_column, "~", x_column)), data = dataset)

p <- ggplot() +
  geom_point(aes(x = dataset[[x_column]], y = dataset[[y_column]]), colour = "red") +
  geom_line(aes(x = dataset[[x_column]], y = predict(model, newdata = dataset)), colour = 'blue') +
  ggtitle(paste(y_column, "vs", x_column)) +
  xlab(x_column) +
  ylab(y_column)
ggsave("linear_regression_r_output.png", plot = p)

print(summary(model))