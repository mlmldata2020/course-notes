# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:46:11 2018

@author: cindy
"""

import numpy as np

from scipy import stats
from scipy import stats
    


def cumulativesum(data):

    '''This function calculates the cumulative sum of an array in meters cubed per 100 meters of coast line'''
    # Insert code here, calculate result

    cumsum=0
    results=[]
    for i in data:
        cumsum=(i*(86400))+cumsum     #adding the cumultive sum to the data
                                        #multiplying the data by how many second in a day to get the correct units 
        #print(cumsum)
        results=np.append(results,cumsum)   #appends the cumulative sum to an empty array
        #print(x)

    return results  #returns all the sumulative sums for all the numbers



def anova_oneway(data):

    '''This function performs a one way ANOVA'''
    s=np.shape(data)  #grabs shape of data array
    allnum=s[0]*s[1]
    ddofd=allnum-s[1]
    ave=np.mean(data) #mean of data set
    ddofn=s[1]-1
    ssw=0
    ssa=0
    
    for i in range(0,s[1]):
        g=data[:,i]  #grabs all data from the first column
        m=np.mean(g)  #mean of the group
        x=(g-m)**2   #subtracting the mean from the array and taking the square
        sm=sum(x)   #sum of squares
        
        ssw=ssw+sm    #adds up all values in the group by replacing ssw with the new sum of the previous numbers
        msw=ssw/ddofd   #finding the mean square within
        
        
    gmean=np.mean(data,axis=0)
    ssa=sum(s[0]*((gmean-ave)**2))
    msa=ssa/ddofn
            
    F=msa/msw
    
    p=1-(stats.f.cdf(F,ddofn,ddofd)) 
   
    
    # Insert code here, calculate F and p
    return F, p