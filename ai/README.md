# AI-Assisted Linear Regression (Assignment 2)

This folder contains the AI-generated portion of Assignment 2. All files were created independently inside `ai/` without modifying, moving, or renaming anything in the `manual/` implementation.

## Contents

| File | Description |
|------|-------------|
| `environment.yml` | Conda environment specification for Python and R dependencies |
| `regression_python.ipynb` | Python Jupyter notebook analyzing `../regression_data.csv` |
| `regression_r.ipynb` | R Jupyter notebook analyzing `../regression_data.csv` |
| `regression_python.html` | HTML export of the Python notebook |
| `regression_r.html` | HTML export of the R notebook |
| `linear_regression_python.py` | Standalone Python script with generic CLI arguments |
| `linear_regression_r.R` | Standalone R script with generic CLI arguments |

Each notebook loads the data, creates a scatter plot, fits a simple linear regression model, overlays the regression line, evaluates the model, and includes Markdown explaining each step.

## Running the Scripts on Ascend

From this directory:

```bash
module load miniconda3/24.1.2-py310
conda activate 7030_class_2

python linear_regression_python.py <filename> <x_column> <y_column>
Rscript linear_regression_r.R <filename> <x_column> <y_column>
```

Example:

```bash
python linear_regression_python.py ../regression_data.csv YearsExperience Salary
Rscript linear_regression_r.R ../regression_data.csv YearsExperience Salary
```

Each script saves a regression plot as a PNG file in this folder (`linear_regression_python_output.png` or `linear_regression_r_output.png`).

## Environment Setup

To create the conda environment from scratch:

```bash
conda env create -f environment.yml
conda activate 7030_class_2
```
