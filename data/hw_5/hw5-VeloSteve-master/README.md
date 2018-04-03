## MS 263  - Data Analysis Techniques In Marine Science
### Homework 5

Due: Tuesday, March 6 (before class)

#### HW3 revisions

Revise Homework 3 for credit. Update your HW3 repository on GitHub, and close the "issue" containing the feedback.

#### Wrap up in class problems

Turn in solutions to questions 3 and 4 of the [in-class problems](https://github.com/mlmldata2018/week04_inclass_problems)

_Grading criteria:_ Correct results and clear figures.

_Submission format_ Create a Jupyter Notebook and upload to your HW5 Github repository.

#### Harmonic analysis: function

Write a function called `seasonal_fit` in the file [harmonic.py](harmonic.py) that takes time series data as input and returns four least-squares coefficients for describing the linear trend and annual cycle. See the doc-string for details on required input and output.

_Grading criteria:_ Correct results, input and output match what is specified in doc-string, robust: works for example in class and homework problem below. Clear variable names and commenting.

_Submission format:_ Edit the [harmonic.py](harmonic.py) file and upload to your GitHub repository.

#### Harmonic analysis: Monterey Wharf

The `data_files` directory in this repository contains a csv file with hourly data from the Monterey Wharf shore station operated by MLML. 

* Use your harmonic analysis function to calculate the trend and seasonal cycle. 
* Plot the residual (difference between annual fit and data) as function of time.
* Comment on how well the model matches the data, and how the estimate of the seasonal cycle could be improved.

Note that there is a variable called 'unix_time'. This is the number of seconds
since 1970-01-01 00:00 http://www.unixtimestamp.com/

_Grading criteria:_ Correct results, uses function from a different file, clear plot, clear answers to questions.

_Submission format:_ Edit the [Monterey_Wharf2_analysis](Monterey_Wharf2_analysis.ipynb) Jupyter Notebook and upload to your GitHub repository.
