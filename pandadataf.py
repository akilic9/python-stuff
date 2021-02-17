# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:11:13 2020

@author: kilic
"""
import pandas as pd

### a
a_dict = {'Maxine' : [95.7, 96.4, 97.3], 'James' : [98.4, 93.2, 93.4], 'Amanda' : [92.6, 97.7, 92.8]}
temperatures = pd.DataFrame(a_dict)
print("a)\n", temperatures)

### b
temperatures.index = ['Morning', 'Afternoon', 'Evening']
print("\nb)\n" , temperatures)

### c
print("\nc)\n", temperatures['Maxine'])

### d
print("\nd)\n", temperatures.iloc[0])

### e
print("\ne)\n", temperatures.iloc[[0,2]])

### f
print("\nf)\n", temperatures.iloc[:,[0,2]])

### g
print("\ng)\n", temperatures.iloc[[0,1],[0,2]])

### h
print("\nh)\n", temperatures.describe())

### i
print("\ni)\n", temperatures.T)

### j
print("\nj)\n", temperatures.sort_index(axis=1))