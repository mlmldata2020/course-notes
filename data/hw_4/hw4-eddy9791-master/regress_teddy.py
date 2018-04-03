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
    
    regress = stats.linregress(x,y)
    ahat = regress[0]
    stderror = regress[4]
    df = len(x)-2
    xbar = np.mean(x)
    slope_lower = ahat - (stats.t.ppf(1-alpha, df)*np.sqrt((stderror**2)/sum(x+xbar)))
    slope_upper = ahat + (stats.t.ppf(1-alpha, df)*np.sqrt((stderror**2)/sum(x+xbar)))

    return (slope_lower,slope_upper)

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

    tcrit = stats.t.ppf(1-alpha/2, nu)
    rcrit = np.sqrt((tcrit**2)/((tcrit**2)+nu))

    return rcrit

def type2regress(x,y):
    """
    Type II Linear regression.
    
    INPUTS:
    x,y - two different variables
    
    OUTPUT:
    slope, intercept
    
    """

    regressxy = stats.linregress(x,y)
    mxy = regressxy[0]
    
    regressyx = stats.linregress(y,x)
    myx = regressyx[0]
    
    slope = np.sqrt(mxy/myx)
    intercept = np.mean(y)-slope*np.mean(x)
    
    
    return slope,intercept