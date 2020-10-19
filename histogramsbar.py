#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:58:41 2020

@author: sg24x7
"""


from matplotlib import pyplot as plt
from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade//10*10
histogram = Counter(decile(grade) for grade in grades)

print(histogram.keys(), histogram.values())

plt.bar([x for x in histogram.keys()], histogram.values(), 8, color = "green")

plt.axis([0, 105, 0, 5])           # x-axis from -5 to 105, y-axis from 0 to 5

plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of students")
plt.title("Distribution of Exam 1 grades")
plt.show()