#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 07:25:44 2020

@author: sg24x7
"""

import time, sys
indent = 0                      #how many spaces to indent
indentIncreasing = True         #Whether the indent is increasing or not
try:
    while True:
        print(' '*indent + '********')
        #print(str(indent))
        time.sleep(0.1)         #pause for 1/10th second
        
        if indentIncreasing:
            #increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                indentIncreasing = False
                
        else:
            #decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()