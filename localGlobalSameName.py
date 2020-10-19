#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:15:01 2020

@author: sg24x7
"""

def spam():
    eggs = 'spam local'
    print(eggs)             #print 'spam local'
    
def bacon():
    eggs = 'bacon local'
    print(eggs)             #print 'bacon local'
    spam()
    print(eggs)             #print 'bacon local' as the local variable in sam is destroyed as spam() returned its value
    
eggs = 'global'
bacon()
print(eggs)                 #print 'global'