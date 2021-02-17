# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:44:54 2020

@author: kilic
"""
tlds = {'Canada':'ca', 'United States':'us', 'Mexico':'mx'}

### a & b
if str(input('Enter search key: ')) in tlds:
    print('Dictionary contains this key.\n')
else:
    print("The dictionary doesn't contain this key.\n")
    
### c
for  key, value in tlds.items():
    print(f'{key}: \t {value}')

### d
print('\nBefore adding the new pair:', tlds)
tlds['Sweden'] = 'sw'
print('After:', tlds)

### e
tlds.update(Sweden='se')
print('After update:', tlds)

### f & g
reverse_tlds = {value:key.upper() for key, value in tlds.items()}
print('Reverse and uppercase:', reverse_tlds)