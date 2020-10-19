#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:29:54 2020

@author: sg24x7
"""

import random, sys
print('ROCK, PAPER, SCISSORS')
print('0 Wins, 0 Losses, 0 Ties')
wins = 0
losses = 0
ties = 0
unum = 0

while True:
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True:
        print('Enter your move (r)ock (p)aper (s)cissors or (q)uit')
        move = input()
        if move == 'q':
            sys.exit()
        elif move == 'p' or move == 's' or move == 'r':
            break
        print('Type one of p,r s, q.')
        
    #display what is player's move
    if move == 'p':
        print('PAPER versus...')
        unum = 1
    elif move == 's':
        print('SCISSORS versus...')
        unum = 2
    elif move == 'r':
        print('ROCK versus...')
        unum = 3
        
    #Display what is computer's move
    num = random.randint(1,3)
    comMove = num
    if num == 1:
        cMove = 'p'
        print('PAPER')
    elif num == 2:
        cMove == 's'
        print('SCISSORS')
    elif num == 3:
        cMove == 'r'
        print('ROCK')
        
    if unum == comMove:
        print('It is a tie!')
        ties = ties + 1
    elif unum == 1 and comMove == 2:
        print('You lose!')
        losses = losses + 1
    elif unum == 1 and comMove == 3:
        print('You win!')
        wins = wins + 1
    elif unum == 2 and comMove == 3:
        print('You lose!')
        losses = losses + 1
    elif unum == 2 and comMove == 1:
        print('Your win!')
        wins = wins + 1
    elif unum == 3 and comMove == 2:
        print('You win!')
        wins = wins + 1
    elif unum == 3 and comMove == 1:
        print('You win!')
        wins = wins + 1
    
    