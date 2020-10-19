#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:42:54 2020

@author: sg24x7
"""
name = 'Joe'
print('Who are you?')
det = input()
while det!=name:
    print('Who are you?')
    det = input()  
print('Hello, Joe. What is your password?(It is a fish)')
pwd = 'swordfish'
pas = input()
dft = 'xyz'
i = 1
for i in range(1, 100) :  
    if pas == pwd:
        print('Access Granted')
        break
    while dft!=name:
        print('Who are you?')
        dft = input()
    print('Hello, Joe. What is your password?(It is a fish)')
    pas = input()
    dft = 'xyz'
    
