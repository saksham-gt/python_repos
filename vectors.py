#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:31:46 2020

@author: sg24x7
"""
def vector_add(v, w):
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]
def bector_subtract(v, w):
    return [v_i - w_i 
            for v_i, w_i in zip(v, w)]
def vector_sum(vectors):
    result = [vectors[0]]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result
def scalar_multiply(c, v):
    return [c*v_i for v_i in v]
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

v1 = [1, 2, 1]
v2 = [3, -5, 2]
h = vector_sum(v2)
print(h)