import numpy as np
from scipy import stats

def cumulativesum(data):
    '''This function calculates the cumulative sum of a list or array'''

    data = np.array(data) # Converts input data into an numpy array
    cumsum = 0 # Defines the starting value of cumsum as zero
    results = [] # Creates new array for appended values
    for val in data: # For each value in the array:
        cumsum = ((val*86400) + cumsum) # Cumsum multiplies the value by 86400s/day and adds the value to itself
        results = np.append(results,cumsum) # Appends the cumsum values to array, results
        
    return results # Returns the appended cumulative sum array 

def anova_oneway(data):
    '''This function calculates a one-way ANOVA test'''

    
    # Insert code here, calculate F and p

    return F, p

#loop ssw to read more than 3 columns