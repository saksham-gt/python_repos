#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 04:24:26 2020

@author: sg24x7
"""

import random

messages = ['It is certain', 
            'It is decidedly so', 
            'Yes, definitely', 
            'Reply hazy try again', 
            'Ask again later', 
            'Concentrate and ask again', 
            'My reply is no', 
            'Outlook not so good', 
            'Very doubtful']

print (messages[random.randint(0, len(messages)-1)])