# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:02:29 2020

@author: kilic
"""

import random
import string

myList = []
for x in range(20):
    a = random.choice(string.ascii_lowercase[:6])
    myList.append(a)

myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)

def unique(myList):
    uList = []
    
    for x in myList:
        if x not in uList:
            uList.append(x)
    return uList

uniqueList = unique(myList)
uniqueList.sort()
print(uniqueList)