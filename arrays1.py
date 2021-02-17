# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:33:51 2020

@author: kilic
"""

import numpy as np

myArray = np.arange(1, 16)
myArray.resize(3,5)
print(myArray)

### a => row 2
print("a)\n",myArray[2])

### b => column 5
print("b)\n",myArray[:,4])

### c => rows 0&1
print("c)\n",myArray[0:2, :])

### d => columns 2-4
print("d)\n",myArray[:, 2:5])

### e => element 1x4
print("e)\n",myArray[1, 4])

### f => elements row 1-2, column 0,2,4
print("f)\n",myArray[1:3, 0:5:2])