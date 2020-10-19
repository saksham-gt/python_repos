#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 06:13:43 2020

@author: sg24x7
"""

birthdays = {'Papa' : 'Jun 14', 'Mother' : 'Sept 14', 'Phalguni Di' : 'Mar 2'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name==' ':
        break
    
    if name in birthdays:
        print(birthdays[name]+ ' is the birthday of ' +name)
    else:
        print('I do now have birthday information for '+name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Brithday database updated.')
        
    print(birthdays)
        
        
