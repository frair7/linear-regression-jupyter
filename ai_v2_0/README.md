# AI-Assisted Linear Regression (Assignment 2)

This folder contains the AI-generated solution for the linear regression portion of Assignment 2. All files here were created with AI assistance and **without modifying the manual implementation** in other folders.

## Contents

| File | Description |
|------|-------------|
| `environment.yml` | Conda environment with Python, Jupyter, R, and analysis dependencies |
| `regression_analysis_python.ipynb` | Python notebook: load data, scatter plot, fit model, overlay line, evaluate |
| `regression_analysis_r.ipynb` | R notebook with the same workflow |
| `regression_analysis_python.html` | Executed HTML export of the Python notebook |
| `regression_analysis_r.html` | Executed HTML export of the R notebook |
| `regression_plot.py` | Standalone Python script (command-line arguments) |
| `regression_plot.R` | Standalone R script (command-line arguments) |
| `regression_data_regression_plot_python.png` | Regression plot from the Python script |
| `regression_data_regression_plot_r.png` | Regression plot from the R script |

## Dataset

Both notebooks and scripts analyze `../regression_data.csv`, using `YearsExperience` as the predictor and `Salary` as the response.

## Running on Ascend

Load the required modules, then run either script with `<filename> <x_column> <y_column>`:

```bash
module load python/3.12
python3 regression_plot.py ../regression_data.csv YearsExperience Salary
```

```bash
module load gcc/12.3.0 R/4.5.2
Rscript regression_plot.R ../regression_data.csv YearsExperience Salary
```

Each script saves a PNG regression plot in the current directory.

## Environment Setup

```bash
conda env create -f environment.yml
conda activate ai_v2_regression
```

On Ascend, the `python/3.12` and `gcc/12.3.0` + `R/4.5.2` modules provide the needed packages without a conda environment.
