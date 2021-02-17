# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:10:34 2020

@author: kilic
"""

s1 = {'red', 'green', 'blue'}
s2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

print(s1 == s2)
print(s1 != s2)
print(s1 < s2)
print(s1 > s2)
print(s1 <= s2)
print(s1 >= s2)

print(s1|s2)
print(s1.union(s2))