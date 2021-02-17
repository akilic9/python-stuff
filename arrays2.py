# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:24:26 2020

@author: kilic
"""
import numpy as np

array1 = np.array([[0,1],[2,3]])
array2 = np.array([[4,5],[6,7]])

### a
array3 = np.vstack((array1, array2))
print("a)\n", array3)

### b
array4 = np.hstack((array1, array2))
print("b)\n", array4)

### c
a1 = array4.view()
a2 = array4.view()
array5 = np.vstack((a1, a2))
print("c)\n", array5)

## d
a3 = array3.copy()
a4 = array3.copy()
array6 = np.hstack((a3, a4))
print("d)\n", array6)