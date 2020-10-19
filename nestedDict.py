#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:20:22 2020

@author: sg24x7
"""

allGuests = {'Alice' : {'apples' : 5, 'pretzels' : 12}, 
             'Bob' : {'ham sandwiches' : 3, 'apples' : 2}, 
             'Carol' : {'cups': 3, 'apple pies' : 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        print(k, end = ' ')
        print(v)
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought: ')
print(' - Apples              ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups                ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes               ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches      ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies          ' + str(totalBrought(allGuests, 'apple pies')))