# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:09:16 2020

@author: kilic
"""
import random
import pandas as pd

### a
panda1 = pd.Series([7, 11, 13, 17])
print("a)\n",panda1)

### b
panda2 = pd.Series(random.randrange(0, 101) for x in range (21))
print("\nb)\n", panda2, "\n\n", panda2.describe())

### c
panda3 = pd.Series([98.6, 98.9, 100.2, 97.9], index = ['Julie', 'Charlie', 'Sam', 'Andrea'])
print("\nc)\n", panda3)

###d
dict = {'Julie' : 98.6, 'Charlie' : 98.9, 'Sam' : 100.2, 'Andrea' : 97.9}
panda4 = pd.Series(dict)
print("\nd)\n", panda4)