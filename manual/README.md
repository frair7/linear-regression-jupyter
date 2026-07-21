# Assignment3_Updated_LinearRegression
OSU BSGP Assignment 3: Linear regression with jupyter and updating previously generated scripts

## Overview

This assignment had two lesson themes. 
The first was to further expand the classes understanding of GitHub.
The second was to explore the code and scripts made in the previous week and determine how they could be modified or improved. 
All of the files that were generated inside of the manual folder were created by hand. 

## Objective
- Clone your respository from assignment2 to a local folder.
- Create a branch on your GitHub repository from assignment2.
- Connect the folder to the assignment3 branch.
- Modify the scripts manually.
- Modify the Jupyter Notebooks manually.
- Commit the scripts and understand the differences.
- In seperate parts of this assignment we will then submit the differnt commit branches to learn how they are snapshots in history. Pull the request, tag, and merge main branch. 

## Dataset
We used the same dataset from assignment 2 that compared years experience to salary. 

## Repository Structure
- I modified the folder structure from assignment 2 to remove the two different versions of the AI folders as 1 was really all that was needed.

```
Assignment3/
|
├── regression_data.csv
├── environment.yml
├── requirements.txt
├── setup_env.sh
├── README.md
├── REFLECTION.md
│
├── manual/
|   ├── archived <--- Keeping these here to show the differences in outcomes.  
|   |   ├── regression_python.ipynb
|   |   ├── regression_r.html
|   |   ├── regression_python.html
|   ├── README.md
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
│   ├── regression_data.csv <--- The cursor needed this so that everything else could remain self contained. 
│   ├── regression_python.ipynb
│   ├── regression_python.html
│   ├── linear_regression_python.py
│   ├── linear_regression_python_output.png
│   ├── regression_r.ipynb
│   ├── regression_r.html
│   ├── linear_regression_r.R
│   ├── linear_regression_r_output.png
│   └── PROMPTS.md
```


## Software and Libraries

### Python
- Python 3.10
- Pandas
- matplotlib
- scikit-learn
- Jupyter Nobeook

### R

- R
- ggplot2
- IRkernel
- Jupyter Notebook

## Changes made to the script
- Chagnes include more detailed code that taught me how and where some of these function can modify a graph.
- Added a prediction model.

## Manual Assignment Components:
Part A, Manual (20 pts)

No AI tools. Type it in. Same content as before, no changes.

Clone your Assignment 2 repo, create an assignment3 branch, enhance your regression analysis with detailed diagnostics and annotated plots, and demonstrate GitHub workflow proficiency through pull requests and tagging.

Complete in both Python and R using:

    Jupyter Notebooks (.ipynb)
    Standalone Scripts (.py, .R)

Required directory structure (see the “Using Git with Improved Notebooks and Scripts” help page for the full tree).

Submit (Part A):

    Original main-branch commit URL before merging assignment3.
    assignment3 branch URL.
    Tagged main-branch URL after the merge (e.g., assignment3-final).

Include a README.md describing your repository, written by you, by hand.
