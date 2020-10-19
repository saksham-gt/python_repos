#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:27:02 2020

@author: sg24x7
"""

def spam():
    global eggs
    eggs = 'spam' #this is global
    
def bacon():
    eggs = 'bacon' #this is local
    
def ham():
    print(eggs)

eggs = 42 #this is global
spam() 
print(eggs)   