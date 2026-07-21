import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

filename = sys.argv[1]
x_column = sys.argv[2]
y_column = sys.argv[3]

dataset = pd.read_csv(filename)

model = LinearRegression()
model.fit(dataset[[x_column]], dataset[[y_column]])

slope = np.ravel(model.coef_)[0]
intercept = np.ravel(model.intercept_)[0]

predictions = model.predict(dataset[[x_column]])
r2 = r2_score(dataset[y_column], predictions)

years_to_predict = 6
prediction_input = pd.DataFrame(
    {x_column: [years_to_predict]}
)

predicted_salary = model.predict(prediction_input)[0][0]

plt.scatter(dataset["YearsExperience"], dataset["Salary"], color=(1, 0, 0, 0.5), edgecolors="k")
plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.grid(True, color="gray", linestyle="--", linewidth=0.5, alpha=0.7, zorder=0)
plt.gca().set_facecolor(("gray", 0.1))
plt.title("Salary vs Experience", fontsize=16)
plt.xlabel("Years of Experience", fontsize=12)
plt.ylabel("Salary", fontsize=12)
plt.text(
    1.1,
    70000,
    f"y = {slope:.2f}x + {intercept:.2f}\n"
    f"$R^2$ = {r2:.2f}\n", 
    fontsize=11
)

plt.scatter(
    years_to_predict,
    predicted_salary,
    color="green",
    s=100,
    marker="*",
    label="Predicted Salary at 6Y"
)
plt.text(
    5.3,
    75000,
    f"${predicted_salary:,.2f}",
    fontsize=11,
    color="green"
)
plt.legend()
plt.savefig(f"manual/{y_column}_vs_{x_column}.png", dpi=300)
plt.show()

print("R-squared:", model.score(dataset[[x_column]], dataset[[y_column]]))  # R-squared
print(f"Predicted salary for {years_to_predict} years of experience: ${predicted_salary:,.2f}")