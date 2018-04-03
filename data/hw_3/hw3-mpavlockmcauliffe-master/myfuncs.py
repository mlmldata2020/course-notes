import numpy as np
from scipy import stats


#%%
def cumulativesum(data):
    '''This function calculates the cumulative sum of an array or list of numbers and stores the result in another array.'''

#make sure data is an array
    data=np.array(data)
    cumsum = 0
    result = ([])
    for val in data:
        cumsum = val + cumsum
        result = np.append(result, cumsum)
        
    return result



#%%
def anova_oneway(data):
    '''This function performs a one-way analysis of variance for an array with J groups (in columns) and N samples in each group (in rows), assuming each data set has the same number of observations.'''
    
    #first define number of groups and samples
    N, J = np.shape(data) #N=samples, #J = groups
    
    #find means & define total number of samples    
    Gmean = np.mean(data) #grand mean
    GroupMean = np.mean(data,axis=0) #mean of each group (columns)
    totsamp = N*J #total number of samples
    
    #first find differences of each sample from it's own group mean
    tosum_SSW =([])
    for i,n in enumerate(data.T):
        dif = sum((n-GroupMean[i])**2)
        tosum_SSW = np.append(tosum_SSW, dif)
   
    MSW = sum(tosum_SSW)/(totsamp-J) #mean squares within
    dfd = totsamp-J

    #next find the sum of squares of each group mean from grand mean
    SSA = sum(N*((GroupMean-Gmean)**2))
    MSA = SSA/(J-1) #mean squares among
    dfn = J-1 #deg freedom numerator

    #F-Statistic
    F = MSA/MSW
    #find p-value
    p = 1 - stats.f.cdf(F,dfn,dfd)

    return F, p




#%% 
#Do the following only if this file is run as a script
if __name__ =='__main__':
    
    #THESE CHECKS ONLY WORK WITH THESE DATASETS
    
    #check cumulative sum function
    upwelling_index = [88., 11., -164.,-16., 82., -53., -321., -257., 1., -43.,            21., 67., 45., 54., 41., 12., 1., -134., -9., -6., -122., -94., 22., -6., 8., 10., -7., -3., 14., 5.]
    
    print('Running as a script to check funcs:')
    check = cumulativesum(upwelling_index)
    #print('Cumsum with my func: ', check)
    #print('Cumsum with np: ', np.cumsum(upwelling_index))
    print('Are my cumsum values equal to np.cumsum values? :',      check==np.cumsum(upwelling_index))
    
    
    #check anova_oneway function
    data = np.genfromtxt('MgO_Maine.csv',skip_header=1,delimiter=',')
    
    # use the anova_oneway function in myfuncs.py 
    F,p = anova_oneway(data)
    statsF, statsp = stats.f_oneway(data[:,0], data[:,1], data[:,2])
    print('Check if my F and p is equal to stats.f.oneway: ')
    print('F from my function: ', F)
    print('F from stats.f_oneway: ', statsF)
    print('p from my function: ', p)
    print('p from stats.f_oneway: ', statsp)
    
    
    
    
    
    
    
    
    
    
    
    
