#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:01:10 2020

@author: sg24x7
"""


from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color="green", marker='o', linestyle="solid")

# adding a title
plt.title("Nominal GDP")

# add a label to y-axis and x-axis         
plt.ylabel("Billions of $")
plt.xlabel("Years")

# to display
plt.show()

# to save the figure
plt.savefig("ajsdd")