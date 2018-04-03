## Homework 6
Due: Before class, March 13

### Multivariate regression - aragonite saturation state

Using data from the West Coast Ocean Acidification (WCOA) cruise, create two multiple linear regression models to calculate aragonite saturation state (OmegaA) as a function of more commonly observed variables.
1. Temperature, salinity, pressure, dissolved oxygen and nitrate (same as class):
OmegaA = c0 + c1 x T + c2 x S + c3 x P + c5 x O + c6 x N

2. Dissolved oxygen, and the interaction between oxygen and temperature (subtracting reference values):
OmegaA = c0 + c1 x (O - Oref) + c2 x (O - Oref)*(T - Tref)

For each regression:
* Plot the modeled fit vs. the data points

* Plot the modeled fit vs. the residuals

* Use `statsmodels` to print a summary of the regression results and statistical tests. Here, `y` is the array containing the response variable and `A` is the design matrix containing the predictor variables.
```
import statsmodels.api as sm
res = sm.OLS(y, A).fit()
print(res.summary())
```

Compare the two regressions in words, commenting on:
  * Statistical significance
  * Multiple co-linearity
  * Applicability of the model equations
  * The potential for numerical errors

_Submission format_: Jupyter Notebook in HW6 GitHub repository.

_Grading criteria_: Correct results, clear code and comments, completeness of statistical interpretation.

### Discussion Reading

Read this article on "good enough" strategies for managing code and data.

https://swcarpentry.github.io/good-enough-practices-in-scientific-computing/

We will discuss these strategies, and any questions about them, in the next class.

### Preliminary independent data analysis

Create at least one figure that is clear and well-labeled, using a data set that you might be interested in working with for your project. You can use whatever file type you wish (.py file, Jupyter Notebook). Just make sure there is a README file that describes what you did in this preliminary analysis, and a potential question you are interested in addressing for your project.

Check out the Matplotlib gallery for plotting ideas:
* https://matplotlib.org/gallery.html

Also, check out the Seaborn package, which builds off of Matplotlib:
* https://seaborn.pydata.org/examples/index.html


_Submission format_: Upload data and files to GitHub (you can create a new project repository if you are git-savvy - if not, we will start the process of setting one up next class). Include a README file.

_Grading criteria_:
* Code uses data file as input, and creates figure
* Code runs
* Code is well-documented
* Preliminary project goals stated
* Figure has title and axis labels, and a legend if necessary

### HW4 revisions

Revise and update on GitHub.
