# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:05:26 2021

@author: kilic
"""

def conversion(C):
    Fahrenheit = (9 / 5) * C + 32
    return Fahrenheit
print("Celcius\t\tFahrenheit")
for aNumber in range (101):
    print("%d\t\t%.1f" % (aNumber, conversion(aNumber)))