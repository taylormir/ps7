# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:03:37 2020

@author: taylo
"""
import matplotlib.pyplot as py
from numpy.polynomial.polynomial import polyfit
import numpy as np

# ts-tp vs tp


#times adjusted to be relative to 23:36
tp= np.array([54.65,57.34,60.49,61.8,61.9,62.25,63.10,63.5,66.08,67.07,68.32,71.12,71.50,77.80]) #seconds
ts= np.array([57.90,62.15,67.55,70.0,70.10,70.70,72.00,72.80,78.30,79.79,81.40,86.40,86.20,97.70]) #seconds


y= ts-tp   # set y-value as difference in times
x= tp

b, m= polyfit(x,y,1)  #create an equation for the best fit line, the slope of which is vpvs ratio.
py.plot(x, b+m*x,1)   # y=mx+b where m is the slope of the best fit line
print (m)

def bestfit (x,y):   #define a function for the bestfit line I am extrapolating
    x= (y-b)/m       # solve equation for best fit line for x  
    return x
t0= bestfit(x,0)    #solve for x when the difference in arriaval times (ts-tp) or "y" is equal to zero
print (t0)

py.scatter(x,y)    # plot ts-tp vs tp 
py.xlabel('tp (seconds after 23:26)')
py.ylabel('ts-tp (seconds after 23:26)')
py.title('Wadati Diagram')
py.show()

