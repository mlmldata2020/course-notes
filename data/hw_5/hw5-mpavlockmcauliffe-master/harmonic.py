import numpy as np
from matplotlib import pyplot as plt

def seasonal_fit(t,y,tannual):
    '''
    Fits a seasonal cycle and trend to a time series of data.
    
    Inputs:
    y - array of data values
    t - array of time values 
    tannual - The annual period 
            (e.g. 365.25 if the time is in units of days)
            (e.g. 12 if the time is in units of months)

    
    Output:
    c - an array of 4 coefficients
    
    To compute the modeled fit:
    
    y_fit = c[0] + 
        c[1]*t + 
        c[2]*np.sin(2*np.pi*t/t_annual) + 
        c[3]*np.cos(2*np.pi*t/t_annual)
    '''
    #Create Design Matrix according to modeled fit
    A = np.empty([len(y),4])
    A[:,0] = 1 #first term of model
    A[:,1] = t #second term
    A[:,2] = np.sin((2*np.pi*t)/tannual) #third term
    A[:,3] = np.cos((2*np.pi*t)/tannual) #fourth term

    #Solve for coefficients
    c_all = np.linalg.lstsq(A,y)
    c=c_all[0] #get coefficients out of c_all
    
    #stderr = c[1] #this gives an array of sums of residuals but we don't need it
    
    return c


if __name__ =='__main__':
    
    #test func with example data from inclass
    t = np.arange(1,25)
    SST = np.array([7.6, 7.4, 8.2, 9.2, 10.2, 11.5, 12.4, 13.4, 13.7, 11.8,         10.1,9.0, 8.9, 9.5, 10.6, 11.4, 12.9, 12.7, 13.9, 14.2, 13.5, 11.4, 10.9, 8.1])
    
    t_annual = 12 #length of year in units of months
    c = seasonal_fit(t,SST,t_annual)
   
    y_fit = c[0] + c[1]*t + c[2]*np.sin(2*np.pi*t/t_annual) +   c[3]*np.cos(2*np.pi*t/t_annual)
    
    #test with a plot
    plt.plot(t,SST,'o')
    plt.plot(t,y_fit,'--')
