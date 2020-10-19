#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:29:27 2020

@author: sg24x7
"""

spam = []

while(True):
    name = input()
    if name == '':
        break
    spam = spam + [name]
op = ''
x = 0
if len(spam)>0:
    x = len(spam) - 1
    for i in range(x):
        op += spam[i] + ', '
    op = ' and ' + spam[i+1]
else:
    op = ''

print(op)
