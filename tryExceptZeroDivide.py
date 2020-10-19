#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:40:43 2020

@author: sg24x7
"""

def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
        