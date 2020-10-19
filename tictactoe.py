#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:04:33 2020

@author: sg24x7
"""

theBoard = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
            'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
            'bot-L' : ' ', 'bot-M' : ' ', 'bot-R' : ' '}

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

printboard(theBoard)
for i in range(1, 10):
    print('What\'s your move? : ', end = '')
    move = input()
    if i%2 == 1:
        theBoard[move] = 'X'
    else:
        theBoard[move] = 'O'
    printboard(theBoard)
    