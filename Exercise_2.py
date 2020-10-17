# -*- coding: utf-8 -*-
# Exercise two
# Name: Eduardo R Rodrigues de Brito Junior
# Course: Applications of Accelerators

import numpy as np
import math
e = 1.602E-19
u = 1.661E-27
# We will consider C-12 ions, so 12 nucleons and charge 6
m = 12.0 * u 
q = 6.0 * e
# Voltage will be 1000 V and phase pi/4 rad and size of bedroom 2 m and 20 drift tubes
U = 1000.0
ph = math.pi/4.0
sz = 2.0
ndf = 20
# Calculating the constant sqrt(q*U*sin(pi/4)/2*m)
k = math.sqrt(q*U*math.sin(ph)/(2.0*m))
# Creating the vector with sqrt(i)
df = np.arange(1,ndf+1)
vc = np.vectorize(math.sqrt)
df = vc(df)
# Calculating the sum of sqrt(i) to determine the frequency to fit in bedroom
tot_sum = sum(df)
# Calculating the frequency f = k*sum(sqrt(i))/sz
f = k*tot_sum/sz
df = (k/f)*df
# Printing the solutions
print('\n*****Solution for the problem is*****')
print('\nInput Data\n')
print('Ion is C-12')
print('Charge = %0.4e C' %q)
print('Mass = %0.4e kg' %m)
print('Voltage = %0.1f V' %U)
print('Phase = %0.4f rad'%ph)
print('Size of the accelarator = %0.1f m' %sz)
print('Number of drift tubes = %d' %ndf)
print('\nCalculated Data\n')
print('Frequency =  %0.4e Hz ' %f)
print('Size of each drif tubes',end='')
for ik in range(ndf):
    print('\nDrift tube %d = %0.4f m'%(ik,df[ik]),end='')
print('\n*****End of the solution*****')