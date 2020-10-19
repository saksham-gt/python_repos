#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:13:07 2020

@author: sg24x7
"""

import re
phn = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')         # phn is regex object, also\d for digit character
mo = phn.search('My number is 425-555-4242.')        # we call search() in phn and enter the string to be searched.
print(mo.group())                                   # group() is used to return the string that is matched in from the string passed,

# Also, another and shorter method to declare the regex object if we want to repeat the pattern of string in re.compile()
phn = re.compile('\d{3}-\d{3}-\d{4}') 
mo = phn.search('My number is 425-555-4242.')
print(mo.group())

# We can create groups by adding parenthesis in a parenthesis and the number starts from 1.
phn = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')     # Grp 1 is first 3 digits and grp 2 is rest numbers.
mo = phn.search('My number is 425-555-4242.')
print('Group 1: ' + mo.group(1)+ ', Group 2: ' + mo.group(2) + ', Complete String: ' + mo.group(0))
areaCode, mainNum = mo.groups()                     # note the plural form in 'groups()' which includes all the group
print('Area Code: '+ areaCode + ', Main Number: ' + mainNum)

# Now, parenthesis(), curly brackets{} etc. have an important place in declaring regex object 
# Hence we cannot use this directly in the string to be searched in re.compile()
# So, we use '\' to use this in pattern.
phn = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phn.search('My number is (425) 555-4242')
print(mo.group())
