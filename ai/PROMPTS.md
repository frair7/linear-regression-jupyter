# Prompts Used to Generate the AI-Assisted Solution

This file records the major prompts used to produce the contents of the `ai/` folder. Only the essential prompts are included so the workflow can be reproduced.

---

## Prompt 1: Generate the AI-Assisted Assignment

```
I am working on the AI-assisted portion of Assignment 2. Please create all required files only inside the ai folder. Do not modify, move, rename, or delete any files outside the ai folder, and do not perform any Git operations (no commits, pushes, branch changes, or modifications to my repository) without my permission.

Create an environment.yml file for this project. Then create a Jupyter notebook in both Python and R that analyze the dataset ../regression_data.csv. Each notebook should load the data, create a scatter plot, fit a simple linear regression model, overlay the regression line, evaluate the model, and include Markdown explaining each step. Export both notebooks as HTML files.

Then we need the stand alone scripts that would replace the salary and years experience and file name inside the script with more generic x_column y_column and file name. Then we need to be able to run these scripts on ascend command-line for <filename> <x_column> <y_column>. it should generate and save the regression plot as a png file. Place all generated notebooks scipts and HTML files and output images inside the ai. folder and verify that everything runs successfull without modifying anything outside that folder.
```

**Expected deliverables:**
- `environment.yml`
- `regression_python.ipynb` and `regression_r.ipynb`
- `regression_python.html` and `regression_r.html`
- `linear_regression_python.py` and `linear_regression_r.R`
- PNG regression plot outputs from the scripts
- Verification that all files run successfully on Ascend

---

## Prompt 2: Add Project Documentation

```
Create a short README inside the ai/ folder describing the AI-generated notebooks and scripts. Mention that all files were generated without modifying the manual implementation.
```

**Expected deliverable:**
- `README.md` describing the AI-generated files and noting that the `manual/` implementation was left unchanged

---

## Prompt 3: Document the AI Workflow

```
Create PROMPTS.md inside the ai/ folder summarizing the most important prompts used to generate this AI-assisted solution. Do not include unnecessary conversation—only the major prompts that would allow someone else to reproduce the AI workflow.
```

**Expected deliverable:**
- `PROMPTS.md` (this file)
