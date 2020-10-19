#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:46:27 2020

@author: sg24x7
"""

import random
numberOfStreaks = 0
x = []
f = 0
for experiments in range(10000):
    f = 0
    for i in range(100):
        if random.randint(0,1) == 0:
            x.append('H')
        else:
            x.append('T')
    for k in range(100):
        if k+5<100: 
            face = x[k]
            for j in range(k+1, k+6):
                if x[j]==face:
                    f = 1
                    continue
                else:
                    f = 0
                    break
            if f==1:
                numberOfStreaks += 1
        else:
            break
print('Chances of Streak: ' + str(int(numberOfStreaks*100/10000 )))

