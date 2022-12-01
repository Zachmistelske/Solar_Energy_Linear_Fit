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
u=h['Year']
r=h['Avg_Solar']
t=r.astype(float)
v=np.zeros(len(t))
for i in range(len(t)):
    v[i]=np.log(t[i])
q1=h['StdDev']
q2=q1.astype(float)
q=np.zeros(len(q1))
for i in range(len(q1)):
    q[i]=math.log(q2[i])
# make a linear point plot of data set displaying errors to each y-value 
plt.scatter(u,v,color='red')
plt.errorbar(u,v,q,color='red',fmt='o',label='data set')
# calculate constant 'a' in the linear equation y=a*x that best represents data first by breaking up formula's sums into arrays for each data value
# us=x^2/sigma^2
us=np.zeros(len(u))
for i in range(len(u)):
    us[i]=((u[i])**2)/((q[i])**2)
# uv=x*y/sigma^2
uv=np.zeros(len(u))
for i in range(len(u)):
    uv[i]=((u[i])*(v[i]))/((q[i])**2)
# divide sums to obtain a
a=(sum(uv))/(sum(us))
# multiply each data value x by calculated a to obtain yfit values and plot linear function
yfit=np.zeros(len(u))
for i in range(len(u)):
    yfit[i]=a*u[i]
plt.plot(u,yfit,color='green',label='fitted linear function')
# calculate chi-squared to evaluate between data and yfit
chi=np.zeros(len(v))
for i in range(len(v)):
    chi[i]=((yfit[i]-v[i])/(q[i]))**2
chis=sum(chi)
# calculate the error in determining the constant a
ae=np.zeros(len(u))
for i in range(len(u)):
    ae[i]=(((u[i])**2)/((q[i])**2))
aerror=math.sqrt((1)/(sum(ae)))
# display results
print('Best-fit value of a:',a)
print('uncertainty in a:',aerror)
print('chi-squared:',chis)
plt.xlabel('Year')
plt.ylabel('Avg_Solar_Consumption')
plt.legend()
plt.show()