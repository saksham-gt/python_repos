#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:06:57 2020

@author: sg24x7
"""
import random
print('I am thinking of a number between 1 and 20')
num = random.randint(1,20)
print('Take a guess.')
guess = input()
for i in range(1,6):
    if int(guess) == num:
        break
    elif int(guess)<num:
        print('Your guess is too low.')
        print('Take a guess.')
        guess = input()
    else:
        print('Your guess is too high.')
        print('Take a guess.')
        guess = input()
if int(guess)==num:
    print('Good job! You guessed the number in '+str(i)+' guesses.')
else:
    print('The number I was thinking of was '+str(num)+'.')
