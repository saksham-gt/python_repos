#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:55:57 2020

@author: sg24x7
"""
from matplotlib import pyplot as plt
mention = [500, 505]
years = [2013, 2014]
plt.bar([2013, 2014], mention, 0.8)
plt.xticks(years)
plt.ylabel("# of times I eard someone say 'data science'")

plt.ticklabel_format(useOffset=False)

plt.axis([2012.5, 2014.5, 0, 550])
plt.title("Look at the huge increase!")
plt.show()

