#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:19:48 2020

@author: sg24x7
"""


from matplotlib import pyplot as plt 

movies = ["Annie Hall", "Ben-Hur", "Gandhi", "Casablanca", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8, so we'll add 0.1 to left co-ordinate
# so that each bar is centered
xs = [i+0.1 for i, _ in enumerate(movies)]

# plot bars with left x- coordinate
plt.bar(xs, num_oscars, color = "green")

plt.ylabel("# of Academy Awards")
plt.xlabel("Movies")
plt.title("My Favourite Movies")

#label x-axis with movie names at bar centers
plt.xticks([i+0.15 for i, _ in enumerate(movies)], movies)

plt.show() 