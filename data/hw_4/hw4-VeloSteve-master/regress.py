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
    # Use stats library linear regression to get values needed below.
    regression = stats.linregress(x, y)
    dof = len(x) - 2
    t = stats.t.ppf(1-alpha/2, dof)
    stderr = regression.stderr
    mean = regression.slope
    return [mean - t*stderr, mean + t*stderr]


# NOTE: I changed the default to match the input definition.
def rcrit(nu,alpha=0.05):
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

    # From class, we can calculate t from abs(r) * sqrt(N-2) / sqrt(1-r**2)
    # If r is positive this simplifies to (letting d = sqrt(N-2))
    # t**2 = (dr)**2 / (1-r**2)
    # and can be arranged as
    # r = sqrt(t**2/(d**2 + t**2))
    
    # To use the equation above, we just need to get t
    # Not that d = sqrt(N-2) and nu = N-2, so d**2 is nu
    t= stats.t.ppf(1-alpha/2, nu)
    rcrit = (t**2 / (nu + t**2))**0.5

    return rcrit

def type2regress(x,y):
    """
    Type II Linear regression.  This version assumes that all points in each 
    variable have equal uncertainties.
    
    INPUTS:
    x,y - two different variables
    
    OUTPUT:
    slope, intercept
    
    """

    # Use the fact from Glover, Jenkins, and Doney that the Type II slope
    # can be calculated from the geometric mean of the Type I slopes of the 
    # data taken in either order.
    myx = stats.linregress(x, y).slope
    mxy = stats.linregress(y, x).slope
    slope =(myx/mxy)**0.5
    # Calculate the intercept as intercept = y - slope * x.
    # In GJD the x and y values are weighted by their uncertainties, but
    # lacking that information assume equal weighting for all points.
    intercept = np.mean(y) - slope * np.mean(x)
    return slope,intercept


if __name__ == '__main__':
    print('Quick sample runs.')
    x = [5, 10, 20, 30, 40]
    y = [10, 21, 39, 61, 79]
    print('Test data x:', x)
    print('Test data y:', y)
    regression = stats.linregress(x, y)
    print('Slope according to scipy:', regression.slope)
    print('The slope confidence interval for x and y is', slope_ci(x, y, 0.05))
    print()
    print('Critical r for dof=50 and significance 0.95 is', rcrit(50, 0.05))
    print('Critical r for dof=50 and significance 0.99 is', rcrit(50, 0.01))
    print('Critical r for dof=3 and significance 0.95 is', rcrit(3, 0.05))
    print('Critical r for dof=3 and significance 0.99 is', rcrit(3, 0.01))
    print()
    [s, i] = type2regress(x, y)
    print('Type II regression of Y vs. X gives slope', s, 'and intercept', i ) 
    [s2, i2] = type2regress(y, x)
    print('Type II regression of Y vs. X gives slope', s2, 'and intercept', i2 )
    print('Compare the inverse of the first slope:', (1/s))