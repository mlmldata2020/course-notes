## MS 263  - Data Analysis Techniques In Marine Science
### Homework 4

Due: Tuesday, February 27 (before class)

#### HW2 revisions

Revise Homework 2 for credit. Update your HW2 repository on GitHub, and close the "issue" containing the feedback.

#### Project ideas

Start brainstorming possible ideas for your final project. The goal is to analyze real data that has already been collected and is available to you. Feel free to be overly ambitious at this point - the scope can be reduced to a manageable size as we progress through the semester. We will set aside time in class to briefly discuss these ideas individually.

#### Linear regression and correlation

These questions use data from the [wcoa_cruise](wcoa_cruise) directory (used in class and also included in this repository). Feel free to use any functions in `pandas`,`numpy` or `scipy.stats` that you find useful.

1. In the Jupyter notebook [wcoa_analysis_hw4](wcoa_analysis_hw4.ipynb), make a scatter plot between all nitrate and phosphate samples deeper than 500 dbar and draw a Type I regression line. 

2. In the file called [regress.py](regress.py), create a function called `slope_ci` that calculates confidence intervals for the slope of the regression line, given the data values and confidence level (default 95%). 

3. In the file called [regress.py](regress.py), create a function called `rcrit` that calculates the critical correlation coefficient r for statistical significance, given the degrees of freedom and significance level alpha.

4. In the file called [regress.py](regress.py), create a function called `type2regress` that calculates the slope and y-intercept of the geometric mean (Type II) regression line, given two arrays of numbers. This is the line that bisects the regression of y on x, and the regression of x on y. See Glover Jenkins and Doney pp. 60-62 (on Moodle) for additional information.

5. In the Jupyter notebook [wcoa_analysis_hw4](wcoa_analysis_hw4.ipynb), draw the Type II regression line on the plot made in #1. Comment on:

  * the strength and significance of the correlation in #1
  * the applicability of a Type I or Type II linear regression model
  * your oceanographic interpretation

__Submission format:__ Upload all modified files to your homework 4 Github repository. Include any files that are necessary to run the code (including cruise data files).

__Grading criteria:__ Code runs without errors, functions can be effectively used later with other data sets, code gives correct output, good coding style (documentation, descriptive variable names, not repeating yourself), clear graphics (axis labels and units), and statistical interpretation.
