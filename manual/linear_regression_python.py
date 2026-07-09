import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

filename = sys.argv[1]
x_column = sys.argv[2]
y_column = sys.argv[3]

dataset = pd.read_csv(filename)

plt.scatter(dataset[x_column], dataset[y_column], color="red")

model = LinearRegression()
model.fit(dataset[[x_column]], dataset[[y_column]])
plt.plot(dataset[x_column], model.predict(dataset[[x_column]]), color="blue")
plt.title(f"{y_column} vs {x_column}")
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.savefig("linear_regression_python_output.png")
print("R-squared:", model.score(dataset[[x_column]], dataset[[y_column]]))  # R-squared