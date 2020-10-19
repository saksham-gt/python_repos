#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 04:30:16 2020

@author: sg24x7
"""

def eggs(someParameter):
    someParameter.append('Hello')
    
spam = [1, 2, 3]
eggs(spam)
print(spam)