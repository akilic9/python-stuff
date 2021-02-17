# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:27:27 2020

@author: kilic
"""

"""
FIRST SCENARIO
Filter operation calls its lambda argument 10 times.
Map function calls its lambda argument 5 times.

SECOND SCENARIO
Filter operation calls its lambda argument 10 times.
Map function calls its lambda argument 10 times.
"""

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def squared(x):
    print("Function squared called for number", x)
    x = x ** 2
    return x

def odd(x):
    print("Function even called for number", x)
    return x % 2 != 0

newList = list(map(squared,
         filter(odd, numbers)))
print(newList)

newnewList = list(filter(odd,
                         map(squared, numbers)))
print(newnewList)