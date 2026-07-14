# Assignment2_linear-regression-jupyter
OSU BSGP 7030 Assignment 2: Linear Regression with Jupyter

## Overview

This assignment demonstrates how to perform a simple linear regression analysis in both Python and R using Jupyter Notebooks and then convert the notebook workflows into standalone command-line scripts. The goal is to understand the differences between interactive notebook development and reusable scripting while comparing equivalent implementations in Python and R.

## Objectives

- Load a CSV dataset into Python and R.
- Visualize the relationship between years of experience and salary.
- Fit a simple linear regression model.
- Overlay the regression line on a scatter plot.
- Evaluate model performance.
- Export notebooks as HTML documents.
- Convert notebook analyses into standalone command-line scripts.

## Dataset

The project uses the provided dataset:

- `regression_data.csv`

The dataset contains two variables:

- **YearsExperience** – Years of professional experience
- **Salary** – Annual salary

## Repository Structure

```
Assignment2/
│
├── regression_data.csv
├── environment.yml
├── requirements.txt
├── setup_env.sh
├── README.md
├── REFLECTION.md
│
├── manual/
│   ├── regression_python.ipynb
│   ├── regression_python.html
│   ├── linear_regression_python.py
│   ├── linear_regression_python_output.png
│   ├── regression_r.ipynb
│   ├── regression_r.html
│   ├── linear_regression_r.R
│   └── linear_regression_r_output.png
│
├── ai/
│   ├── regression_python.ipynb
│   ├── regression_python.html
│   ├── linear_regression_python.py
│   ├── linear_regression_python_output.png
│   ├── regression_r.ipynb
│   ├── regression_r.html
│   ├── linear_regression_r.R
│   ├── linear_regression_r_output.png
│   └── PROMPTS.md
│
└── ai_v2_0/
    ├── regression_analysis_python.ipynb
    ├── regression_analysis_python.html
    ├── regression_analysis_r.ipynb
    ├── regression_analysis_r.html
    ├── regression_plot.py
    ├── regression_plot.R
    ├── regression_data_regression_plot_python.png
    ├── regression_data_regression_plot_r.png
    ├── environment.yml
    ├── README.md
    └── PROMPTS.md
```

## Software and Libraries

### Python

- Python 3.10
- pandas
- matplotlib
- scikit-learn
- Jupyter Notebook

### R

- R
- ggplot2
- IRkernel
- Jupyter Notebook

## Analysis Workflow

Both the Python and R implementations perform the following steps:

1. Read the dataset.
2. Create a scatter plot of Years of Experience versus Salary.
3. Fit a simple linear regression model.
4. Overlay the regression line on the scatter plot.
5. Evaluate the model using standard regression metrics.
6. Save the notebook as an HTML document.
7. Convert the notebook into a standalone command-line script.

## AI-Assisted Version 2.0

After comparing the initial AI-assisted files with the manual files, I found that the original AI scripts were nearly identical to the manual implementations. Because Cursor was operating within the same project workspace, it may have referenced the existing files in the `manual/` folder while generating the first AI version.

To create a more independent comparison, I regenerated the AI-assisted implementation in the separate `ai_v2_0/` folder. During this second attempt, I explicitly instructed the AI not to inspect, copy, or use the code in the `manual/` or original `ai/` folders. The prompts used for this process are documented in `ai_v2_0/PROMPTS.md`.

The version 2.0 implementation performs the same required linear-regression analysis but differs substantially from the manual version in its organization, validation, plotting methods, and model evaluation.

### Python Version 2.0

The Python command-line script:

* Uses a `main()` function and a Python execution guard.
* Verifies that exactly three command-line arguments were supplied.
* Checks that the requested CSV file exists.
* Confirms that the selected x and y columns are present in the dataset.
* Uses pandas to read the data.
* Uses scikit-learn to fit a linear regression model.
* Calculates both R-squared and root mean squared error.
* Creates an evenly spaced set of x-values for drawing a smooth regression line.
* Adds a legend and a text box containing the model metrics.
* Saves the completed plot as a PNG image.

The Python notebook contains the corresponding interactive analysis and was also exported as an HTML file.

### R Version 2.0

The R command-line script:

* Uses `commandArgs(trailingOnly = TRUE)` to accept the filename and column names.
* Checks that exactly three command-line arguments were supplied.
* Verifies that the requested file exists.
* Confirms that the requested columns are present.
* Uses `lm()` to fit the linear regression model.
* Calculates both R-squared and root mean squared error.
* Uses base R graphics rather than `ggplot2`.
* Adds the fitted regression line with `abline()`.
* Adds a legend and displays the model metrics above the plot.
* Saves the completed plot as a PNG image.

The R notebook contains the corresponding interactive analysis and was also exported as an HTML file.

### Structural Differences from the Manual Version

The manual scripts use a direct, sequential structure with minimal input checking. The version 2.0 AI scripts include more defensive programming, such as argument validation, file checks, column checks, clear error messages, and controlled exit statuses.

The manual Python script reports R-squared, while the version 2.0 Python script reports both R-squared and RMSE. The manual R script uses `ggplot2`, while the version 2.0 R script uses base R plotting functions. The AI-generated Python script also organizes the work into functions, while the manual script executes each step directly at the top level.

These differences made the version 2.0 files more robust, although they were also longer and more complex than the manual implementations.

## Results

Both implementations successfully modeled the relationship between years of experience and salary using linear regression. The fitted models produced similar regression coefficients and an R² value of approximately **0.785**, indicating that years of experience explains approximately **78.5%** of the variation in salary within this dataset.

## Assignment Components

* **Part A:** Manual implementation completed without AI assistance in the `manual/` folder.
* **Part B:** Initial AI-assisted implementation completed in the `ai/` folder.
* **Independent AI comparison:** A second AI-assisted implementation was completed in `ai_v2_0/` after discovering that the initial AI version was nearly identical to the manual version.
* **Part C:** `REFLECTION.md` compares the manual, initial AI-assisted, and independently regenerated AI-assisted workflows.