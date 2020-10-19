#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:21:44 2020

@author: sg24x7
"""

def spam():
    global eggs     #this statement declares 'eggs' as the global variable
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)