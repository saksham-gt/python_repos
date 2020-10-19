#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:54:29 2020

@author: sg24x7
"""

# Using pipe to search for any of the given arguments
import re
batRegex = re.compile(r'Tina Fey|Batman')
mo1 = batRegex.search('Batman and Tina Fey')            # if both found then stores in group which comes first
print(mo1.group())
mo1 = batRegex.search('Tina Fey and Batman')
print(mo1.group())

# If strings hare a common part
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())
print(mo.group(1))

# Optional matching with ?
batRegex = re.compile(r'Bat(wo)?man')               # (wo)? is the regular expression means the pattern 'wo' is optional search
mo1 = batRegex.search('The adventures of Batman.')
mo2 = batRegex.search('The adventures of Batwoman')
print(mo1.group())
print(mo2.group())

phn = re.compile(r'(\d\d\d-)(\d\d\d-)?\d\d\d\d')
mo = phn.search('My number is 425-555-4242')
print(mo.group())
mo = phn.search('My number is 555-4242')
print(mo.group())
mo = phn.search('My number is 425-4242')
print(mo.group())