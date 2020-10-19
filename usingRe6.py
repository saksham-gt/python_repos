#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:33:10 2020

@author: sg24x7
"""
import re

# Using Wildcard character (.), it matches just one character before the dot, and it does not match newline character.
atRegex = re.compile(r'.at')
x = atRegex.findall('The cat in the hat sat on the flat mat.')
print(x)        # it just matches the first element before dot i.e. only 'lat' not 'flat'

atRegex = re.compile(r'.\.gupta')
x = atRegex.findall('This is saksham.gupta')        # to include . in the search use \.
print(x)

# Matching everything with dot-star (.*)
nameReg = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameReg.search('First Name: Al Last Name: Steigwart')
print(mo.groups())

# also dot-star-question mark to do it non greedy way the above concept.
nongr = re.compile(r'<.*?>')
x = nongr.search('<To serve man>for dinner.>')
print(x.group())            # non greedy
nongr = re.compile(r'<.*>')
x = nongr.search('<To serve man>for dinner.>')  # greedy
print(x.group())

# Matching newlines with the dot character
# we have to use re.DOTALL in the second argument of re.compile()

noNewlineRe = re.compile('.*')
mo = noNewlineRe.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)

NewlineRe = re.compile('.*', re.DOTALL)
mo = NewlineRe.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)