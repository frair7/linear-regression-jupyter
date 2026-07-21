# Prompts Used to Generate This Solution

Major prompts used with Cursor AI to produce the files in this folder. These are condensed to the essential instructions needed to reproduce the workflow.

---

## Prompt 1: Initial project setup

> Create all required files only inside the ai folder. Do not read, modify, move, rename, or delete any files outside the ai folder, and do not perform any Git operations without permission. Do not look at the manual folder or other folders.
>
> Create an `environment.yml` file for this project. Then create a Jupyter notebook in both Python and R that analyze the dataset `regression_data.csv`. Each notebook should load the data, create a scatter plot, fit a simple linear regression model, overlay the regression line, evaluate the model, and include Markdown explaining each step. Export both notebooks as HTML files.
>
> Create standalone Python and R scripts that read the dataset, fit a linear regression model, and generate/save the regression plot as a PNG file. Place all generated notebooks, scripts, HTML files, and output images inside the ai folder and verify that everything runs successfully.

---

## Prompt 2: Separate regression plots per script

> There should be a regression plot for both the AI scripts (Python and R). Each script should save its own PNG output file.

---

## Prompt 3: Documentation

> Without looking at any of the other folders: Create a short README inside the ai folder describing the AI-generated notebooks and scripts. Mention that all files were generated without modifying the manual implementation. Create PROMPTS.md summarizing the most important prompts used to generate this AI-assisted solution.

---

## Prompt 4: Full regression analysis update

> Using this folder and only this folder, update the Python script, Python notebook, R script, and R notebook.
>
> Read `regression_data.csv` using `YearsExperience` as the independent variable and `Salary` as the dependent variable. Fit a linear regression model and report the slope, intercept, regression equation, R-squared, and predicted salary for 6 years of experience.
>
> Create a polished landscape regression graph with observed data points, the fitted line, clear title and axis labels, a legend, the regression equation, R-squared, a highlighted prediction point at 6 years, and an annotation showing the predicted salary.
>
> Run both scripts and both notebooks after making the changes. Save the graph images as `linear_regression_python_output.png` and `linear_regression_r_output.png`. Export the completed notebooks as HTML in the ai folder. Update the existing files in place without creating extra versions.

---

## Prompt 5: Update documentation

> Update the PROMPTS.md and README.md files to reflect the current project structure, outputs, and run instructions.
