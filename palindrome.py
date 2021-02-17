# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:04:41 2021

@author: kilic
"""

aNumber = int (input ("Please enter a number:") )
hold = aNumber
reverse = 0
while (aNumber > 0):
    remainder = aNumber % 10
    reverse = reverse * 10 + remainder
    aNumber = aNumber // 10
if (hold == reverse):
    print ("The number is a palindrome.")
else:
    print ("The number is not a palindrome.")