# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 19:38:39 2022

@author: zachm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

h = pd.read_csv("C:/Research/data analytics/Research Projects/energy project/linearfitsolar.csv")
h.head()
h.info()
h.hist(bins=100, figsize=(15, 10))
plt.show()

c=h['Year']/h['Avg_Solar']
v=h['Year']
r=h['Avg_Solar']
u=r.astype(float)
q1=h['StdDev']
q=q1.astype(float)
# make a linear point plot of data set displaying errors to each y-value
plt.scatter(u,v,color='green')
plt.errorbar(u,v,q,color='green',fmt='o',label='data set')
# calculate constant 'a' and 'b' in the linear equation y=a+b*x that best represents data first by breaking up formula's sums into arrays for each data value
# uv=x*y/sigma^2
xy=np.zeros(len(u))
for i in range(len(u)):
    xy[i]=(u[i]*v[i])/((q[i])**2)
# us=x^2/sigma^2
xs=np.zeros(len(u))
for i in range(len(u)):
    xs[i]=((u[i])**2)/((q[i])**2)
# nu=x/sigma^2
nx=np.zeros(len(u))
for i in range(len(u)):
    nx[i]=(u[i])/((q[i])**2)
# nv=y/sigma^2
ny=np.zeros(len(v))
for i in range(len(v)):
    ny[i]=(v[i])/((q[i])**2)
# j=1/sigma^2
j=np.zeros(len(q))
for i in range(len(q)):
    j[i]=(1/((q[i])**2))
# calculate determinant of inverse matrix that is used to find a and b
det=(sum(j)*sum(xs))-((sum(nx)))**2
# calculate a by multiplying and subtracting sums then divide by determinant
a=((sum(ny)*sum(xs))-(sum(nx)*sum(xy)))/(det)
# calculate b by multiplying and subtracting sums then divide by determinant
b=((sum(j)*sum(xy))-(sum(nx)*sum(ny)))/(det)
# calculate errors in determining a and b
errora=math.sqrt((sum(xs))/(det))
errorb=math.sqrt((sum(j))/(det))
# calculate yfit values by plugging calculated values a and b into yfit equation yfit=a+b*x
yfit=np.zeros(len(u))
for i in range(len(u)):
    yfit[i]=a+b*(u[i])
# plot yfit function 
plt.plot(u,yfit,color='purple',label='fitted linear function')
# calculate chi-squareed to test agreement between yfit and data
chi=np.zeros(len(v))
for i in range(len(v)):
    chi[i]=((yfit[i]-v[i])/(q[i]))**2
chis=sum(chi)
# display calculated values a,b,their errors, and chi-squared
print('Best-fit value of a:',a)
print('Best-fit value of b:',b)
print('uncertainty in a:',errora)
print('uncertainty in b:',errorb)
print('chi-squared:',chis)

plt.xlabel('Avg Solar Consumption (kWh)')
plt.ylabel('Year')
plt.legend()
plt.show()

