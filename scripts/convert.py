#!/usr/bin/env python3

'''class demonstration'''

def temp_f2c(f):
	''' This function converts Fahrenheit to Celcius
	Input: temperature in degrees F
	Output: Celcius
	'''
	c = (f - 32.0)*(5.0/9.0)
	return(c)
	
def temp_c2f(c):
	''' This function converts C to F
	Input: temperature in degrees C
	Output: F
	'''
	f = c*(9/5) + 32
	return(f)
	
if __name__ == '__main__':
	print('do this stuff if run as script')
	print('32 degrees F:',temp_f2c(32),'C')