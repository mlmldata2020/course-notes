import numpy as np
from scipy import stats

def cumulativesum(data):
    '''Return the seqential sums of values in the argument.
    
       Accepts an array or list and returns a numpy.array of
       the same length and data type.  The nth value in the
       output array is the sum of the first n values in the input.
    '''
    import numpy as np

    # Initialize the output to zeros, which should be faster
    # than append.  'zeros_like' attempts to match the data type.
    cum_array = np.zeros_like(data)
    cumsum = 0
    # Go through all the input values, using their index i to
    # place the cumulative sum into the output array.
    for i, val in enumerate(data):
        cumsum = cumsum + val 
        cum_array[i] = cumsum

    return cum_array

def anova_oneway(data):
    '''Take balanced sets of data and perform one-way ANOVA.
    
    The data must be formatted with J columns representing J groups 
    and N rows containing one sample for each group.  The F statistic and
    p-value for a one-way ANOVA are returned.
    '''
    from scipy import stats

    n_obs = len(data) # number of rows = number of observations
    n_group = len(data[0])  # number of columns = number of groups
    
    # Take the average of each column, i.e. average across rows, axis = 0.
    group_mean = np.mean(data, axis=0)

    # For ANOVA, we need to ratio of variance between groups to variance
    # within, so do each part separately and then divide.

    # First get the denominator, based on variance within groups
    # Sum the variances for each group.
    group_variance = np.zeros(n_group)
    for gp in range(n_group):
        group_variance[gp] = sum((data[:, gp]-group_mean[gp])**2)

    # The sum of squares within groups
    SSW = sum(group_variance)
    # Degrees of freedom within (denominator):
    dfd = n_obs*n_group - n_group
    # Mean square within
    MSW = SSW / dfd

    # Now get the numerator, based on variance between groups.
    grand_mean = np.mean(data)
    SSA = 0
    for gp in range(n_group):
        SSA = SSA + n_obs * (group_mean[gp] - grand_mean)**2

    # Degrees of freedom among (numerator):
    dfn = n_group - 1
    # Mean square among groups
    MSA = SSA/dfn

    # The ratio of mean squares is the F value
    F = MSA/MSW

    # Now compute the area included to the left of F
    cdf = stats.f.cdf(F, dfn, dfd)
    # The p-value is the area to the right
    p = 1 - cdf

    return F, p
