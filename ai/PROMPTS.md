# Prompts Used to Generate This Solution

Major prompts used with Cursor AI to produce the files in this folder. These are condensed to the essential instructions needed to reproduce the workflow.

---

## Prompt 1: Initial project setup

> Create all required files only inside the ai_v2 folder. Do not read, modify, move, rename, or delete any files outside the ai_v2 folder, and do not perform any Git operations without permission. Do not look at the ai folder or the manual folder.
>
> Create an `environment.yml` file for this project. Then create a Jupyter notebook in both Python and R that analyze the dataset `../regression_data.csv`. Each notebook should load the data, create a scatter plot, fit a simple linear regression model, overlay the regression line, evaluate the model, and include Markdown explaining each step. Export both notebooks as HTML files.
>
> Create standalone scripts that replace specific column names with generic `x_column`, `y_column`, and `file name` arguments. The scripts should run on the Ascend command line as `<filename> <x_column> <y_column>` and generate/save the regression plot as a PNG file. Place all generated notebooks, scripts, HTML files, and output images inside the ai_v2 folder and verify that everything runs successfully.

---

## Prompt 2: Separate regression plots per script

> There should be a regression plot for both the AI scripts (Python and R). Each script should save its own PNG output file.

---

## Prompt 3: Documentation

> Without looking at any of the other folders: Create a short README inside the ai_v2_0 folder describing the AI-generated notebooks and scripts. Mention that all files were generated without modifying the manual implementation. Create PROMPTS.md summarizing the most important prompts used to generate this AI-assisted solution.
