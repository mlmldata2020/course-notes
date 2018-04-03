import numpy as np

def seasonal_fit(t,y,tannual):
    '''
    This function fits a seaonal cylcle and trend to a time series of data given y(data values) and t(time values) and giving coefficients
    #Fits a seasonal cycle and trend to a time series of data.
    #Inputs:
    #y - array of data values
    #t - array of time values 
    #tannual - The annual period 
           # (e.g. 365.25 if the time is in units of days)
           #for inclass data set tannual would be 12 for units in months
    #Output:
    #c - an array of 4 coefficients
    #To compute the modeled fit:
    '''
    data_shape = np.array(np.shape(y))  #finding the shape of the data
    data_int=np.int(data_shape)  #converting the array to an interger to work later on
    matrix = np.ones([data_int,4])  #creating a matrix of ones using the shape of the data and            4 beacuse thats the number of coefficients needed
    
    column2 = t      #replacing the columns of ones with the equation 
    column3 = np.array(np.sin(2*np.pi*t/tannual))
    column4 = np.array(np.cos(2*np.pi*t/tannual))
    
    matrix[:,1]=column2    #taking all the rows in column two and replaing with what I called column 2
    matrix[:,2]=column3   #taking all the rows in column three and replaing with what I called column 3
    matrix[:,3]=column4  #taking all the rows in column four and replaing with what I called column 4
    #do not have to replace column one because it is one an dthe array already has ones
    
    coefficient=np.linalg.lstsq(matrix,y)   #finding the coefficients
    c=coefficient[0]   #taking the first values from the above equation
    
#y_fit = (c[0] +       #y values after finding coefficients
   # c[1]*t + 
   # c[2]*np.sin(2*np.pi*t/tannual) + 
   # c[3]*np.cos(2*np.pi*t/tannual))
    
    # Insert code here
    return c


#testing the function

import numpy as np

from matplotlib import pyplot as plt

t = np.arange(1,25)
SST = np.array([7.6, 7.4, 8.2, 9.2, 10.2, 11.5, 12.4, 13.4, 13.7, 11.8, 10.1, 9.0,                8.9, 9.5, 10.6, 11.4, 12.9, 12.7, 13.9, 14.2, 13.5, 11.4, 10.9, 8.1])
    
    
    
coefficients=seasonal_fit(t,SST,12)
print(coefficients)    
