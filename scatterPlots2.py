#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:27:25 2020

@author: sg24x7
"""


from matplotlib import pyplot as plt
test1_grades = [99, 90, 85, 97, 80]
test2_grades = [100, 85, 60, 90, 70]

plt.scatter(test1_grades, test2_grades)
plt.title("Axes aren't comparable")
plt.xlabel("test 1 grade")
plt.ylabel("test 2 grade")
plt.axis("equal")
plt.show()