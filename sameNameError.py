#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:31:42 2020

@author: sg24x7
"""

def spam():
    print(eggs)             #ERROR!
    eggs = 'spam local'
    
eggs = 'global'
spam()