#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:45:54 2020

@author: sg24x7
"""

import random, sys
print('I am thinking of a number between 1 and 20')
ans = random.randint(1, 20)
for i in range(5):
    print('Take a guess')
    guess = int(input())
    if guess==ans:
        break
    elif guess<ans:
        print('Your guess is too low!')
    elif guess>ans:
        print('Your guess is too high.')
if guess==ans:
    print('Congratulations! You guesssed the number in '+str(i+1)+' chances.')
else:
    print('Better luck next time!!')