#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 07:58:11 2020

@author: sg24x7
"""
import sys
def collatz(number):
    if number!=1:
        if number % 2 == 0:
            number = number // 2
            print(number)
            collatz(number)
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
            collatz(number)
    else:
        sys.exit()        
print('Enter number:')
num = input()
number = int(num)
collatz(number)