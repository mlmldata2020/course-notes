import numpy as np

def seasonal_fit(t,y,tannual):
    '''
    Fits a seasonal cycle and trend to a time series of data.
    
    Inputs:
    y - array of data values
    t - array of time values 
    tannual - The annual period 
            (e.g. 365.25 if the time is in units of days)
    
    Output:
    c - an array of 4 coefficients
    
    To compute the modeled fit:
    
    y_fit = c[0] + 
        c[1]*t + 
        c[2]*np.sin(2*np.pi*t/t_annual) + 
        c[3]*np.cos(2*np.pi*t/t_annual)
    '''
    
    # Insert code here
    
    return c