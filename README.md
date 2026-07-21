# BSGP 7030 – Assignment 3
## Branching, Pull Requests, Merging, Tagging, and Regression Analysis

### Overview

This repository contains the completed work for Assignment 3 of BSGP 7030. The objective of this assignment was to continue development of the linear regression project from Assignment 2 while learning and applying a collaborative Git workflow using feature branches, pull requests, merges, and version tags.

The project contains both a manually developed implementation and an AI-assisted implementation in Python and R.

---
## Repository Structure

```text
Assignment3/
├── ai/
│   ├── environment.yml
│   ├── PROMPTS.md
│   ├── README.md
│   ├── regression_data.csv
│   ├── regression_plot.py
│   ├── regression_plot.R
│   ├── regression_analysis_python.ipynb
│   ├── regression_analysis_python.html
│   ├── regression_analysis_r.ipynb
│   ├── regression_analysis_r.html
│   ├── linear_regression_python_output.png
│   └── linear_regression_r_output.png
│
├── manual/
│   ├── archive/
│   ├── linear_regression_python.py
│   ├── linear_regression_r.R
│   ├── regression_python_v2.ipynb
│   ├── regression_python_V2.html
│   ├── regression_r.ipynb
│   ├── regression_r_v2.html
│   ├── linear_regression_python_output.png
│   └── linear_regression_r_output.png
│
├── environment.yml
├── regression_data.csv
├── requirements.txt
├── setup_env.sh
└── README.md
```

---

## Objectives

The project demonstrates:

- Linear regression in both Python and R
- Command-line scripts
- Interactive Jupyter notebooks
- Regression visualization
- Git feature branch workflow
- Pull requests
- Branch merging
- Version tagging

---

## Project Improvements

Compared to Assignment 2, both the manual and AI-assisted implementations were enhanced to include:

- Linear regression model fitting
- Regression equation displayed on plots
- R² calculation and annotation
- Prediction of salary at **6 years of experience**
- Highlighted prediction point
- Improved plot formatting
- Legends
- Better axis labels and titles
- Cleaner notebook organization
- Exported HTML versions of notebooks

---

## Manual Implementation

The manual implementation was developed directly by the author using:

- Python
- scikit-learn
- matplotlib
- pandas

and

- R
- ggplot2
- lm()

The notebooks walk through:

1. Loading the data
2. Exploring the dataset
3. Fitting a regression model
4. Making predictions
5. Visualizing the results

---

## AI-Assisted Implementation

The AI-assisted implementation was generated using Cursor with carefully constrained prompts.

The AI was instructed to:

- Work only within the AI folder
- Avoid referencing the manual implementation
- Improve visualization
- Add regression equations
- Add R²
- Predict salary at six years of experience
- Export notebooks as HTML
- Generate publication-quality figures

The resulting code was reviewed, tested, and validated before being committed.

---

## Running the Scripts

### Python

```
python linear_regression_python.py regression_data.csv YearsExperience Salary
```

### R

```
Rscript linear_regression_r.R regression_data.csv YearsExperience Salary
```

---

## Outputs

Successful execution produces:

- Regression statistics
- Predicted salary at 6 years
- Publication-quality regression plots
- HTML notebook exports

---

## Git Workflow

This assignment was completed using a Git feature branch.

Workflow:

1. Clone repository
2. Create `assignment3` branch
3. Develop changes on the feature branch
4. Commit changes
5. Push feature branch to GitHub
6. Open Pull Request
7. Merge into `main`
8. Create a version tag

This demonstrates a collaborative software development workflow while preserving the project history.

---

## Software

Python packages:

- pandas
- matplotlib
- scikit-learn

R packages:

- ggplot2

---

# Assignment Summary

This repository contains the completed work for **BSGP 7030 – Assignment 3: Git and Improvements to Assignment 2**.

## Part A – Manual Implementation

The manual implementation was completed without the use of AI and includes:

- Enhanced Python and R regression scripts
- Enhanced Python and R Jupyter notebooks
- Improved regression visualizations with:
  - Regression line
  - Regression equation
  - R² annotation
  - Prediction of salary at 6 years of experience
  - Highlighted prediction point
  - Legends and improved formatting
- HTML exports of both notebooks
- PNG images generated from both scripts
- Git workflow completed using a dedicated `assignment3` feature branch

---

## Part B – AI-Assisted Implementation

A separate AI implementation is included in the `ai/` directory.

The AI-assisted work includes:

- Enhanced Python and R regression scripts
- Enhanced Python and R Jupyter notebooks
- HTML notebook exports
- Generated regression figures
- AI prompt log (`PROMPTS.md`)
- AI-generated repository documentation (`README_AI.md`)
- AI code review (`CODE_REVIEW.md`)

The AI implementation was developed independently of the manual implementation and subsequently reviewed and tested before being committed.

---

## Part C – Reflection

The repository also includes **REFLECTION.md**, which discusses:

- Comparison of manual and AI-generated commit messages
- Evaluation of the AI code review
- Comparison of the manual README and AI-generated README
- Lessons learned and future workflow improvements

---

## Git Workflow Demonstrated

This assignment demonstrates the use of Git and GitHub through:

- Feature branch development (`assignment3`)
- Multiple commits documenting project progress
- Pull request creation
- Branch merging into `main`
- Version tagging of the final merged release

---

## Repository Contents

This repository contains:

- Manual implementation (`manual/`)
- AI-assisted implementation (`ai/`)
- Regression dataset
- Environment and setup files
- Project documentation
- Reflection
- Git history demonstrating the complete development workflow
