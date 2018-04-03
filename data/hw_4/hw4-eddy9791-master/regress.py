import numpy as np
from scipy import stats

def slope_ci(x,y,alpha=0.05):
    ''' Compute the confidence intervals for the slope of the 
    Type I regression between x and y.
    
    INPUTS:
    x - independent variable values
    y - dependent variable values (must be same length as x)
    alpha - significance level (default 0.05 for 95% confidence)
    
    OUTPUT:
    slope_lower,slope_upper - bounds of confidence interval
    '''
    
    # Insert code here

    return slope_lower,slope_upper

def rcrit(nu,alpha=0.95):
    """
    Critical r (correlation coefficient), given significance level
    and degrees of freedom.
    
    INPUTS:
    nu - degrees of freedom (N-2)        
    alpha - significance level (default 0.05 for 95% confidence)
    
    OUTPUT:
    rcrit - critical r value
    
    Values for 0.05 and 0.01 correspond with Appendix E in
    Emery and Thomson (2004) Data Analysis Methods in Physical 
    Oceanography
    """

    # Insert code here.

    return rcrit

def type2regress(x,y):
    """
    Type II Linear regression.
    
    INPUTS:
    x,y - two different variables
    
    OUTPUT:
    slope, intercept
    
    """

    # Insert code here.

    return slope,intercept