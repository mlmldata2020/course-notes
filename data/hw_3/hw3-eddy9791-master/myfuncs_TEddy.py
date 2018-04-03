import numpy as np
from scipy import stats

def cumulativesum(data, units):
    '''
    This function converts a list or array of daily averages (a rate in units 
    of [volume or distance]/second) to an array of the cumulative sum (in units 
    of volume). For the input (data, units); data can be a list or array, and 
    units are the volume units of the input data. 

    The data set must be a DAILY average with a rate in terms of SECONDS, 
    because the funciton multiplies the input by the number of seconds in a day 
    to get the final cumulative sum.
    
    The output will be given as ([array], units of the array) where the array 
    is the cumulative sum of the input list/array, and the units are the units 
    given in the input.
    '''
    
    result=[] ## creates a blank array
    cumsum = 0 ## starts the cumulative sum at 0
    for i in data:
        cumsum = (i*(24*3600)) + cumsum ## for each value of the input data set, multiply by the number of seconds in a day, and add the cumulative sum (starting at zero). Saves to the cumulative sum, so the next value is added to the other values already added. 
        result = np.append(result, cumsum) ## adds the result from cumsum to the blank "results" array. Each value is added, and it doesn't replace the previous value. 
    
    return (result, units) ## returns the final array once the function has gone through all the values in "data", and addes the units 

def anova_oneway(data):
    '''
    This function performs a one-way anova for an array with groups (in columns)
    and samples in each group (in rows). Data must have equal sample sizes. 
    
    The function returns the F statistic and p-value (F,p)
    '''

    grand_mean = np.mean(data) #calculates grand mean
    group_mean = np.mean(data, axis = 0) # calculates the group mean
    replicates = np.shape(data)[0] #calculates the number of replicates in each group (this assumes equal sample sizes in each group)
    dof_group = len(group_mean)-1 # calculates the degress of freedom of the groups (number of groups -1)
    dof_within = len(group_mean)*replicates - len(group_mean) #calculates the degrees of freedom within (number of total samples - number of groups)
    ssbetween = sum(replicates*((group_mean-grand_mean)**2)) #calculates the sum of squares between
    sstotal = sum(sum((data-grand_mean)**2)) #calculates the total sum of squares 
    sswithin = sstotal - ssbetween #based on the total sum of squares and sum of squares between, we can figure out the sum of squares within without writing a long equation
    msb = ssbetween/dof_group #calculates the mean square error between
    msw = sswithin/dof_within # calculates the mean square error within
    F = msb/msw #calculates the f statistic
    
    p = 1-stats.f.cdf(F,dof_group,dof_within)     #calculates the p value based on the f statistic and the degrees of freedom between and within
    

    return (F, p)

