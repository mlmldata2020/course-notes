import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import pandas as pd

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
    #first - ignore the nans in x and y and reassign variables
    jj = (np.isfinite(x) & np.isfinite(y)) 
    x = np.array(x[jj]) #make into array because pd series is weird (?)
    y = np.array(y[jj])
    
    #calculate the slope of the type I regression line for comparison later
    result = stats.linregress(x,y)
    a = result.slope
    b = result.intercept
    yhat = a*x + b #y values as a result of model
    
    #find means and degrees of freedom
    meanx = np.mean(x)
    meany = np.mean(y)
    dfree = (len(x)+len(y))/2 - 2 #this function should assume the same number of     samples in each variable, but what if there is a diff number of nans?? 
    
    #calculate regression slope of fit (ahat)
    ahat = (sum((x-meanx)*(y-meany))/(sum((x-meanx)**2)))
    
    #find critical t value
    tcrit = stats.t.ppf(1-alpha,df=dfree)
        

    #find std error (Se)
    SSE = sum((y-yhat)**2)
    Se = np.sqrt(SSE/dfree)
    
    #define lower and upper confidence 
    slope_lower = ahat - tcrit*(np.sqrt((Se**2)/(sum(x+meanx))))
    slope_upper = ahat + tcrit*(np.sqrt((Se**2)/(sum(x+meanx))))

    return slope_lower, slope_upper


#%%
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
    #find means and degrees of freedom
    meanx = np.mean(x)
    meany = np.mean(y)
    
    #find std deviations & covariance
    sx = np.std(x,ddof=1)
    sy = np.std(y,ddof=1)
    Sxy2 = (1/(nu+1)*sum((x-meanx)*(y-meany)))

    #calculate critical r
    rcrit = Sxy2/(sx*sy) #compare this to table for significance of correlation
    
    return rcrit

def type2regress(x,y):
    """
    Type II Linear regression.
    
    INPUTS:
    x,y - two different variables
    
    OUTPUT:
    slope, intercept
    
    """
    #use linregress to get slope of y from x
    resultyx = stats.linregress(x,y)
    m_yx = resultyx.slope
   
    #use linregress to get slope of x from y and calculate geometric mean
    resultxy = stats.linregress(y,x)
    m_xy = resultxy.slope
    
    #Type II slope (aka the geometric mean)
    slope = np.sqrt(m_yx/m_xy) 
    
    #Type II intercept
    intercept = np.mean(y) - np.mean(x)*slope

    return slope,intercept



#%% 
#Do the following only if this file is run as a script
if __name__ =='__main__':
    #load in some data for testing
    #MOVE TO THIS DIRECTORY: C:\Users\Miya\Documents\aaClasses\DataAnalySpr18\hw4-mpavlockmcauliffe-master)
     filename = 'wcoa_cruise/WCOA2013_hy1.csv'
     df = pd.read_csv(filename, header=31,na_values=-999, parse_dates=[[8,9]])
     
     #make variables easier and make an index to ignore the nans
     x = df['NITRAT'] 
     y= df['PHSPHT'] 
     
     ii, = np.where(df['CTDPRS']>500)
     
     #Messy indexing...but OK for test.
     x1 = x[ii]
     y1 = y[ii]
     
     jj = (np.isfinite(x1) & np.isfinite(y1))
     x2 = x1[jj]
     y2 = y1[jj]
     
     x = x2
     y = y2
     
     #calculate linregress
     result = stats.linregress(x2,y2)
     a = result.slope
     b = result.intercept
     regline = a*x+b
     
     #check func
     slope_lower, slope_upper = slope_ci(x,y,alpha=.05)
     confupper = slope_upper*x + b
     conflower = slope_lower*x + b
     
     #plot nitrate vs. phosphate at index ii where pressure > 500db
     plt.figure()
     plt.plot(x[jj],y[jj],'co',label='Samples')
     plt.title('Phosphate vs. Nitrate at Pressure > 500 db')
     plt.xlabel('Nitrate $[\mu M / kg]$')
     plt.ylabel('Phosphate $[\mu M / kg]$')
     
     plt.plot(x,regline,'b-',label='LinRegress')
     
     plt.plot(x[jj], confupper,'--r',label='Conf Upper')
     plt.plot(x[jj], conflower,'g--',label='Conf Lower')
     
     plt.legend()
    
     #test rcrit function
     output_test = rcrit(nu,alpha=0.95)
     print('Part 3: r-critical value: ',output_test)
     
     #test type2regress(x,y)     
     slope,intercept = type2regress(x,y)
     print('Part 4: ')
     print('Type II slope = ',slope)
     print('Type II intercept = ',intercept)
    
        
    
    