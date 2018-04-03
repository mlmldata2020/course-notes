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
    
    y = np.array(y)
    t = np.array(t)
   
    A=np.nan*np.ones([len(y),4])  #create the design matrix

    col2=t
    col3=np.sin(2*np.pi*t/t_annual)
    col4=np.cos(2*np.pi*t/t_annual)
    A[:,0]=1
    A[:,1]=col2
    A[:,2]=col3
    A[:,3]=col4

    c = np.linalg.lstsq(A,y)
    c = c[0]
    
    return c

if __name__ == '__main__':
    # do the following stuff if harmonic.py is run as a script
    print('running as a script')
    
    #Example:
    t=([1,2,3,4,5,6,7,8,9,10,11,12])   #random time series - monthly for a year
    y=([10,13,24,3,12,16,6,8,11,10,4,4])  #random data values
    t_annual=12  #time is in months
    
    c=seasonal_fit(t,y,t_annual)
    
    print(c)
    
    print('Modelled Fit Equation:')
    print(c[0],'+',c[1],'* t +',c[2],'* sin(2*pi*t/',t_annual,') +',c[3],'* cos(2*pi*t/',t_annual,'))')
