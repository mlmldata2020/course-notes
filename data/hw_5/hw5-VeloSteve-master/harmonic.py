import numpy as np

def seasonal_fit(t,y,t_annual):
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
    # We need a matrix (A) of the non-coefficient parts of the terms in y_fit
    # Initialize with nan values
    A = np.ones((len(t),4))*np.nan
    # This could be done in one line, but 4 seems more readable.
    A[:, 0] = 1
    A[:, 1] = t
    A[:, 2] = [np.sin(2*np.pi*x/t_annual) for x in t]
    A[:, 3] = [np.cos(2*np.pi*x/t_annual) for x in t]
    
    # library function lstsq returns coefficients in c[0], std err in c[1]
    c = np.linalg.lstsq(A, y)

    return c[0]


# NOTE: I tried this as a possible improvement, but the results actually got
# worse.  The function below is not used in the Jupyter notebook.
def seasonal_fit_asymmetric(t,y,t_annual):
    '''
    Fits a seasonal cycle and trend to a time series of data.
    
    Inputs:
    y - array of data values
    t - array of time values 
    tannual - The annual period 
            (e.g. 365.25 if the time is in units of days)
    
    Output:
    c - an array of 6 coefficients
    
    To compute the modeled fit:
    
    y_fit = c[0] + 
        c[1]*t + 
        c[2]*np.sin(2*np.pi*t/t_annual) + 
        c[3]*np.cos(2*np.pi*t/t_annual)
        c[4]*np.sin(2*np.pi*(t+t_annual/4)/t_annual) + 
        c[5]*np.cos(2*np.pi*(t+t_annual/4)/t_annual)
    '''
    # We need a matrix (A) of the non-coefficient parts of the terms in y_fit
    # Initialize with nan values
    k = 2*np.pi/t_annual
    A = np.ones((len(t),6))*np.nan
    A[:, 0] = 1
    A[:, 1] = t
    A[:, 2] = [np.sin(k*x) for x in t]
    A[:, 3] = [np.cos(k*x) for x in t]
    # Offset these by 3 months (1/4 of a year) to see if the combination can
    # capture the asymmetry of seasonal swings.
    dt = t_annual/4
    A[:, 4] = [np.sin(k*(x-dt)) for x in t]
    A[:, 5] = [np.cos(k*(x-dt)) for x in t]
    
    # library function lstsq returns coefficients in c[0], std err in c[1]
    c = np.linalg.lstsq(A, y)
    
    return c[0]
