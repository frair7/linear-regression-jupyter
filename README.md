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
│   ├── linear_regression_python.ipynb
│   ├── linear_regression_python.html
│   ├── linear_regression_python.py
│   ├── linear_regression_python_output.png
│   ├── linear_regression_r.ipynb
│   ├── linear_regression_r.html
│   ├── linear_regression_r.R
│   └── linear_regression_r_output.png
│
└── ai/
    ├── linear_regression_python.ipynb
    ├── linear_regression_python.html
    ├── linear_regression_python.py
    ├── linear_regression_python_output.png
    ├── linear_regression_r.ipynb
    ├── linear_regression_r.html
    ├── linear_regression_r.R
    ├── linear_regression_r_output.png
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

## Results

Both implementations successfully modeled the relationship between years of experience and salary using linear regression. The fitted models produced similar regression coefficients and an R² value of approximately **0.785**, indicating that years of experience explains approximately **78.5%** of the variation in salary within this dataset.

## Assignment Components

- **Part A:** Manual implementation completed without AI assistance.
- **Part B:** AI-assisted implementation completed in a separate `ai` folder.
- **Part C:** Reflection comparing the manual and AI-assisted workflows.
