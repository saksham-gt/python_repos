#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 02:42:15 2020

@author: sg24x7
"""


import re

# to match case insensitive tring
# add re.IGNORECASE or re.I to the second argument of re.compile()

regex1 = re.compile(r'RoboCop', re.I)
print(regex1.search('RObOcOp is part man, part machine, and all cop.').group())

# now to substitute a particular part of string using sub()
namesRegex = re.compile(r'Agent \w+')        
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# We want to show the first letters of the names of the agents and rest of the letters to be replaced by '*'
agentsReg = re.compile(r'Agent (\w)(\w)\w*')
print(agentsReg.sub(r'\1****', 'Agent Aliceland told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
print(agentsReg.sub(r'\2****', 'Agent Aliceland told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))   # r'\1 (\2 or \3)***' meaning that enter the text of group 1, 2, 3 and so on , in the substitution

phoneReg = re.compile(r'((\d{3}|\(\d{3}\)))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5}?)') 
# the upper expression looks fucking messy
# it can be re-written as 
phoneReg = re.compile(r'''(
    (\d{3}|\(\d{3}\))               # area code can either be in normal 3 digits \d{3} or in brackets (123) i.e. \( \d{3} \)
     (\s|-|\.)                      # can be separated by either space or - or .
     \d{3}                          # first 3 digits 
     (\s|-|\.)                      # separator as above
     \d{4}
     (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
    )''', re.VERBOSE)
print(phoneReg.search('My number is 425-555-4242.'))
# now it is readable.
# managing complex patterns by re.VERBOSE to ignore whitespace and comments

