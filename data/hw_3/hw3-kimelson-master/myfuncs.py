import numpy as np
from scipy import stats

def cumulativesum(data):
    '''This function returns the cumulative sum of a 1D array in the form of an array.'''

    import numpy as np
    
    cumsum=0
    result = [] # empty array to add cumulative sums into
    for val in data:  # for each value in the data set:
        cumsum = cumsum + val  # add each value to the cumulative sum
        result = np.append(result,cumsum)  # appending the cumulative sum into the new array

    return result

def anova_oneway(data):
    '''This function performs a one-way analysis of variance on an array with J groups (in columns) and N samples in each group (in rows).  N should be the same for each group.
    It returns the F-statistic and the p-value as (F,p)'''

    import numpy as np
    from scipy import stats

    grandmean = np.mean(data)
    eachmean = np.mean(data,axis=0)
    NJ = np.shape(data)
    J = NJ[1]  # number of groups/columns
    N = NJ[0]  # number of samples in each group (ie number of rows)
    
    #sum of squares within groups (SSW):
    var=np.var(data,axis=0,ddof=1)
    sqsumw=var*(N-1)
    
    SSW = sum(sqsumw)
            
    #mean square within (MSW):
    dfd = N*J-J  #degrees of freedom for denominator
    MSW = SSW/dfd
    
    #sum of squares among (SSA)    
    SSA = sum((N*(eachmean-grandmean)**2))
    
    #mean square among (MSA):
    dfn = J-1  #degrees of freedom for numerator
    MSA = SSA/dfn
    
    # Test=statistic: Fisher's F:
    F=MSA/MSW

    #for P-value:
    fdist = stats.f.cdf(F,dfn,dfd) #cumulative f-distribution
    p = 1-fdist

    return F, p


if __name__ == '__main__':
    # do the following stuff if myfuncs.py is run as a script

    print('running as a script')
    
#    cumulativesum(data) example
#    January 2017 daily upwelling index in m^3/s/100m coastline
    upwelling_index=[88., 11., -164.,-16., 82., -53., -321., -257., 1., -43., 21., 67., 45., 54., 41., 12., 1., -134., -9., -6., -122., -94., 22., -6., 8., 10., -7., -3., 14., 5.]

#    cumulative upwelling index in m^3/100m coastline:
    cui = cumulativesum(upwelling_index)  #m^3/s/100m coastline
    cui2 = cui*86400  #86400 s/day
    print ('January 2017 cumulative upwelling index in m^3/100m coastline =',cui2)
#    
    
#    anova_oneway(data) example- 3 groups, each with a sample size of 4:
    
    data = [7.,8.,10.,11.],[4.,5.,7.,8.],[1.,2.,4.,5.]
    data = np.array(data)
    data = data.T
    
    ANOVA=anova_oneway(data)
    print('(F-statistic, p-value) =',ANOVA)
    
    
