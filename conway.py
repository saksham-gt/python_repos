#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 05:39:41 2020

@author: sg24x7
"""

#Conway's Game of Life
# '#' for living cell and ' ' for empty cell

import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] #Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') #adding a living cell
        else:
            column.append(' ') #add a dead cell
    nextCells.append(column)
    
while True: #main program loop
    print('\n\n\n\n\n')        #separate each steps with newlines
    currentCells = copy.deepcopy(nextCells)
    
    #Print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end=' ')   #print the # or space
        print()                                 #printing the newline at the end of the row
        
    #Calculate the next step's cell based on current step cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbouring coordinates
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH-1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT
            
            # Count number of iving Neighbours
            numNeighbours = 0
            if currentCells[leftCoord][rightCoord]=='#':
                numNeighbours+=1                # Top left neighbour is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbours+=1                # Top neighbour is alive.
                
            