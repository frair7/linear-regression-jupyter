# AI-Assisted Linear Regression (Assignment 3)

This folder contains the AI-generated solution for the linear regression portion of Assignment 3. All files here were created with AI assistance and **without modifying the manual implementation** in other folders.

## Contents

| File | Description |
|------|-------------|
| `environment.yml` | Conda environment with Python, Jupyter, R, and analysis dependencies |
| `regression_data.csv` | Dataset with `YearsExperience` and `Salary` |
| `regression_plot.py` | Standalone Python script: fit model, report results, save plot |
| `regression_plot.R` | Standalone R script with the same workflow |
| `regression_analysis_python.ipynb` | Python notebook with step-by-step analysis and graph |
| `regression_analysis_r.ipynb` | R notebook with the same workflow |
| `regression_analysis_python.html` | Executed HTML export of the Python notebook |
| `regression_analysis_r.html` | Executed HTML export of the R notebook |
| `linear_regression_python_output.png` | Regression plot from the Python script |
| `linear_regression_r_output.png` | Regression plot from the R script |

## Dataset

Both notebooks and scripts read `regression_data.csv` in this folder, using `YearsExperience` as the independent variable and `Salary` as the dependent variable.

## Analysis Output

Both Python and R produce the same results:

| Metric | Value |
|--------|-------|
| Slope | 8285.2921 |
| Intercept | 29203.5227 |
| Regression equation | `Salary = 29203.5227 + 8285.2921 * YearsExperience` |
| R-squared | 0.7852 |
| Predicted salary at 6 years | 78915.28 |

Each regression graph includes observed data points, the fitted line, the regression equation, R-squared, a legend, and a highlighted prediction at 6 years of experience.

## Running on Ascend

Load the required modules, then run either script from this folder:

```bash
module load python/3.12
python3 regression_plot.py
```

```bash
module load gcc/12.3.0 R/4.5.2
Rscript regression_plot.R
```

Each script prints the regression statistics and saves its plot as a PNG file in this folder.

To execute the notebooks and export HTML:

```bash
module load python/3.12
jupyter nbconvert --to notebook --execute regression_analysis_python.ipynb --output regression_analysis_python.ipynb
jupyter nbconvert --to html regression_analysis_python.ipynb --output regression_analysis_python.html
```

```bash
module load python/3.12 gcc/12.3.0 R/4.5.2
jupyter nbconvert --to notebook --execute regression_analysis_r.ipynb --output regression_analysis_r.ipynb --ExecutePreprocessor.kernel_name=ir
jupyter nbconvert --to html regression_analysis_r.ipynb --output regression_analysis_r.html
```

## Environment Setup

```bash
conda env create -f environment.yml
conda activate ai_v2_regression
```

On Ascend, the `python/3.12` and `gcc/12.3.0` + `R/4.5.2` modules provide the needed packages without a conda environment.
