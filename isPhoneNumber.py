#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 02:06:57 2020

@author: sg24x7
"""


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi Moshi a phone number?')
print(isPhoneNumber('Moshi Moshi'))

message = 'Call me at 425-555-4242 tomorrow. 425-555-4242 is my offie number.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number Found : ' + chunk)
print('Done')
    