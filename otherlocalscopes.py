#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:07:37 2020

@author: sg24x7
"""

def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham = 101
    eggs = 0    
    
    #since both eggs variables are the local variables of two different functions therefore they both are different 
    #when bacon() returns it also destroys the local varible eggs in bacon and hence it remains the same as in spam()
    
spam()
