#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    
    x=np.array(x)
    y=np.array(y)
    
    slope,intercept,rvalue,pvalue,stderr = stats.linregress(x,y)  #Type I linear regression of x and y to get the model
    N=(len(x))
    yi=(slope*x+intercept)  #y-value from model (regression line formula)
    SSE=sum((y-yi)**2)  #sum of squared errors
    Se=((SSE/(N-2))**0.5)  #standard error
    t=stats.t.ppf((1-alpha/2),(N-2))  #critical t-value
    sqdevmeanx=(x-np.mean(x))**2  #squared deviations from the mean for x
    tbound=(t*(Se**2/sum(sqdevmeanx)**0.5))  #mean +/- this value is the condifence interval

    slope_lower=slope-tbound
    slope_upper=slope+tbound

    return slope_lower,slope_upper


def rcrit(nu,alpha=0.05):
    '''
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
    '''

    #calculated r from test statistic equation: t=r* (N-2)^1/2/(1-r^2)^1/2
    t=stats.t.ppf(1-alpha/2,nu)
    rcrit=(1/((nu/(t**2))+1))**0.5

    return rcrit

def type2regress(x,y):
    '''
    Type II Linear regression.
    
    INPUTS:
    x,y - two different variables
    
    OUTPUT:
    slope, intercept
    
    '''

    x=np.array(x)
    y=np.array(y)
    
    myx,intercept1,rvalue,pvalue,stderr = stats.linregress(x,y)
    mxy,intercept2,rvalue,pvalue,stderr = stats.linregress(y,x)
    
    slope=(myx/mxy)**0.5

    mx=np.mean(x)
    my=np.mean(y)
    
    intercept=my-slope*mx

    return slope,intercept


if __name__ == '__main__':

    print('running as a script')
    
    x=[1,2,3,4,5,6]
    y=[3,6,8,12,15,17]
    
    confint=slope_ci(x,y,alpha=0.05)
    critr=rcrit(4,alpha=0.05)
    slope,yintercept=type2regress(x,y)
    
    print('The confidence intervals for the regression line is:',confint)
    print('The critical r-value is:',critr)
    print('Type II Linear Regression: slope =',slope,'y-intercept =',yintercept)