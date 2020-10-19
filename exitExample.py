#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:00:57 2020

@author: sg24x7
"""

import sys
while True:
    print('Type Exit to exit')
    response = input()
    if response == 'Exit':
        sys.exit()
    print('You typed' +response+ '.')