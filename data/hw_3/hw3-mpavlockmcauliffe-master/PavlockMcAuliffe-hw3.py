# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:53:56 2018

@author: Miya

Homework #3
"""
import numpy as np
import myfuncs
from scipy import stats
from statsmodels.stats import power



#%% Part 1: Cumulative upwelling index calculations
print()
print('HW3 Part1 ')
#Values in units of (m^3/s)/100m coastline
upwelling_index = [88., 11., -164.,-16., 82., -53., -321.,
                   -257., 1., -43., 21., 67., 45., 54., 41.,
                   12., 1., -134., -9., -6., -122., -94., 22.,
                   -6., 8., 10., -7., -3., 14., 5.]

# use the cumulativesum function in myfuncs.py - but first, convert units because my cumulativesum function is for an arbitrary array. 

#convert units to (m^3/day)/100m coastline
upwelling_index_day = np.array(upwelling_index)*86400 

#use function to calculate cumulative upwelling index for data
cui = myfuncs.cumulativesum(upwelling_index_day)

#display results here
print('Cumulative sum of Jan, 2017 upwelling index [(m^3/day)/100m coastline]: ')
print(cui)
print()



#%% Part 2: One way ANOVA function
print('HW3 Part 2:')
#get data from txt file
data = np.genfromtxt('MgO_Maine.csv',skip_header=1,delimiter=',')

#define dfd & dfn to compare with critical F later
N, J = np.shape(data) #N=samples, #J = groups
dfd = N*J-J
dfn = J-1

# use the anova_oneway function in myfuncs.py 
F,p = myfuncs.anova_oneway(data)

#find F critical values for 95% and 99% confidence
Fcrit95 = stats.f.ppf(.95, dfn, dfd)
Fcrit99 = stats.f.ppf(.99, dfn, dfd)

#Run tests and print results and interpretations
print('For 95% confidence, alpha = .05: ')
print('p value for data = ', p)
print('Critical F = ', Fcrit95)
print('F value for data = ', F)

if p>.05 and F<Fcrit95: #the only time you would accept null
    print('Accept null hypothesis, all groups are statistically the same')
else: #any other scenario results in rejecting the null
    print('Reject null hypothesis, at least one group is statistically different')

print() 

print('For 99% confidence, alpha = .01: ')
print('p value for data = ', p)
print('Critical F = ', Fcrit99)
print('F value for data = ', F)

if p>.01 and F<Fcrit99: #the only time you would accept null
    print('Accept null hypothesis, all groups are statistically the same')
else: #any other scenario results in rejecting the null
    print('Reject null hypothesis, at least one group is statistically different')

#print terms to reject & accept to visually double check alpha to p and F to Fcrit
print()
print('Reminder:')
print('Reject null if p is smaller than alpha.')
print('Reject null if F is larger than F critical.')
print()

#%% Part 3: Short problems
print('HW3 Part 3a:')
#a: Comparing respiration rates
StationA = np.array([0.45, 0.77, 0.71])
StationB = np.array([0.54, 0.43, 0.36])

#test to determine whether there is a significant difference in the mean respiration rate between the two stations.

#compares two independent sets of measurements, compares means, assuming equal variance
tstat, pval = stats.ttest_ind(StationA,StationB,equal_var=True)

#find t lower and upper to compare
tlow = stats.t.ppf(.025,4) #degrees of freedom = (total samples) - (num groups)
thigh = stats.t.ppf(.975,4)

if tlow < tstat < thigh and pval > .05:
    print('T range: ', tlow, '<', tstat, '<', thigh)
    print('With 95% confidence, accept the null, the two groups are not significantly different. Test t value fits within critical t values and p-value is > .05.')
else:
    print('T range: ')
    print(tlow, '/<', tstat, '/<', thigh)
    print('With 95% confidence, the two groups are significantly different.')

print()

#%%
#b: Comparing two years of current meter records
print('HW3 Part 3b:')
station1 = 23 #+/- 3
station2 = 20 #+/- 2
dfree = 60 #sum of all samples - number of groups

difmeans = station1-station2
sx1 = (3**2)/31 
sx2 = (2**2)/31

#conduct t-test assuming equal variance and normal distribution
t_test = (difmeans)/np.sqrt(sx1+sx2) #test t-value

#find lower and upper critical values
tcrit95low = stats.t.ppf(.025,df=60)
tcrit95high = stats.t.ppf(.975,df=60)

print('Test t value for two samples = ', t_test)
print('t(.025) = ', tcrit95low)
print('t(.975) = ', tcrit95high)

if tcrit95low < t_test < tcrit95high:
    print('Accept the null hypothesis, these data are statistically the same.')
else: 
    print('Reject the null hypothesis, these data are statistically different. Test t value does not fall within critical range.')


print()
#%%
#c: Power analysis and experimental design
print('HW3 Part 3c:')
effect_size = power.tt_solve_power(power=.8,alpha=.05,nobs=20)
print('The minimum difference in mean length must be: ',effect_size, 'mm')
print('With a target power of 80%, the probability of not observing a significant effect of this magnitude if there actually is one is 20%. There is a 20% chance of having Type-2 error')







