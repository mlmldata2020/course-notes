#%matplotlib notebook
import pandas as pd
import numpy as np
from scipy import stats
#from matplotlib import pyplot as plt

filename = 'wcoa_cruise/WCOA2013_hy1.csv'      #opening the data through pandas
df = pd.read_csv(filename, header=31, 
                 na_values=-999, parse_dates=[[8,9]])

filename = 'WCOA2013_hy1.csv'
pd.read_csv(filename,header=31)

df = pd.read_csv(filename,header=31,
                na_values=-999, parse_dates=[[8,9]])  #[] rows 8 and 9 have date information




def slope_ci(x,y,alpha=0.05):
    ''' This function computes the confidence intervals for the slope of the Type I regression between x and y'''
    #INPUTS:
    #x - independent variable values
    #y - dependent variable values (must be same length as x)
    #alpha - significance level (default 0.05 for 95% confidence)
    
    #OUTPUT:
    #slope_lower,slope_upper - bounds of confidence interval
    x_mean=np.mean(x)   #mean of the values in the x array
    y_mean=np.mean(y)  #mean of values in the y array
    x_minus_mean=x-x_mean  #x minus the x mean
    y_minus_mean=y-y_mean  #y minus the y mean
        
    a_hat_numerator=sum(x_minus_mean*y_minus_mean)  #calculating the numerator of a hat
    a_hat_denominator=sum(x_minus_mean**2)  #calculating the denominator of a hat
    a_hat=a_hat_numerator/a_hat_denominator #calculating a hat
    
    #i=(np.isfinite(x) & np.isfinite(y))   #telling it to only give values that have a number value instead of nan
    result = stats.linregress(x,y)   #calculating the linear regression slope and y-intercept
    a=result[0]       #slope
    b=result[1]      #y-intercept
    
    y_hat=(a*x)+b
    
    #b_hat=y_mean-(a_hat*x_mean)
    
    SSE=sum((y-y_hat)**2)
    
    x_total=len(x)   #finding length of x data
    y_total=len(y)   #finding length of y data
    n=(x_total+y_total)/2  #total number of samples in each
    nu=n-2            #degrees of freedom
    se=(SSE/nu)**0.5  #standard error
    
    t_crit=stats.t.ppf(0.95,nu)  #finding t-critical
    #t_lower=stats.t.ppf(0.05,nu)
    
    slope_lower=(a_hat-t_crit*(np.sqrt(((se**2)/(np.abs(sum(x+x_mean))))))) #finding lower slope of interval
    slope_upper=(a_hat+t_crit*(np.sqrt(se**2/(np.abs((sum(x+x_mean)))))))    #finding upper slope of interval
        
    # Insert code here

    return slope_lower,slope_upper




ii,= np.where(df['CTDPRS']>500)  #getting data where pressure is greater than 500 dbars

x=df['NITRAT'][ii]  #nitrate data with index
x=np.array(x)   #turning it into an array
x=x[np.isfinite(x)]  #making sure not to include nans in array
#print(x)

y=df['PHSPHT'][ii]  #phosphate data with index
y=np.array(y)  #turning it inot an array
y=y[np.isfinite(y)]  #not including nans in array
#print(y)

slope_low,slope_high=slope_ci(x,y,0.05)
print('lower interval')
print(slope_low)
print('upper interval')
print(slope_high)



def rcrit(nu,alpha=0.95):
    '''This function calculates the critical r (correlation coefficient), given the significance level and the degrees of freedom''' 
        
   # INPUTS:
    #nu - degrees of freedom (N-2)        
   # alpha - significance level (default 0.05 for 95% confidence)
    
  #  OUTPUT:
   # rcrit - critical r value
    
    #Values for 0.05 and 0.01 correspond with Appendix E in
   # Emery and Thomson (2004) Data Analysis Methods in Physical 
   # Oceanography
    x_mean=np.mean(x)  #finding mean of x
    y_mean=np.mean(y)  #finding mean of y
    x_minus_mean=x-x_mean  #subtracting mean of x from x
    y_minus_mean=y-y_mean  #subtracting mean of y from y
   
    x_total=len(x)   #finding length of x values
    y_total=len(y)   #finding length of y values
    n=(x_total+y_total)/2 #total number of samples
    nu=n-1           #degrees of freedom
    
    s2xy=(1/nu)*(sum((x_minus_mean)*(y_minus_mean)))   #covariance
    sx=np.std(x,ddof=1)   #standard deviation of x
    sy=np.std(y,ddof=1)    #standard deviation of y
    
    rcrit=s2xy/(sx*sy)   
    
    
    # Insert code here.
    
    return rcrit


ii,= np.where(df['CTDPRS']>500)

x=df['NITRAT'][ii]
x=np.array(x)
x=x[np.isfinite(x)]
#print(x)

y=df['PHSPHT'][ii]
y=np.array(y)
y=y[np.isfinite(y)]
#print(y)
x_total=len(x)
y_total=len(y)
n=(x_total*y_total)
nu=n-1  

rcritical=rcrit(nu,0.95)
print('Critical r value')
print(rcritical)    # compare this value to the correlation coefficient table




def type2regress(x,y):
    '''This function calculates the slope and y-intercept of the geometric mean (Type II) regression line, given two arrays''' 
    #Type II Linear regression.
    #INPUTS:
    #x,y - two different variables
    #OUTPUT:
    #slope, intercept
    
    result_yx = stats.linregress(x,y)  #linregress of y from x
    myx=result_yx[0]       #slope of y from x
         
    
    result_xy=stats.linregress(y,x)  #linregress of x from y
    mxy=result_xy[0]       #slope of x from y
     
    slope=np.sqrt(myx/mxy)  #calculating the geometric mean (new slope of type 2)
    
    intercept=np.mean(y)-(slope*np.mean(x))
   
    

    # Insert code here.

    return slope,intercept
    
    
    
    
ii,= np.where(df['CTDPRS']>500)

x=df['NITRAT'][ii]
x=np.array(x)
x=x[np.isfinite(x)]
#print(x)

y=df['PHSPHT'][ii]
y=np.array(y)
y=y[np.isfinite(y)]
#print(y)
x_total=len(x)
y_total=len(y)
n=(x_total*y_total)
nu=n-1  

slope,intercept=type2regress(x,y)
print('slope of type two regression')
print(slope)
print('intercept of type two regression')
print(intercept)
        