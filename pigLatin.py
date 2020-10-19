#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 00:17:26 2020

@author: sg24x7
"""

# English to Pig Latin 
print("Enter the English message to translate into Pig Latin : ")
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []       # A list of words in Pig Latin
for word in message.split():
    # Separate the non-letters at the start of the word
    prefixNonLetters = ''  
    
    while len(word)>0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
        
    if len(word)==0:
        pigLatin.append(prefixNonLetters)
        continue
    
    # Separate the non letters at the end of this word.
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
        
    # Remember if the word is in uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()
        
    word = word.lower()     # making the word in lowercase
        
    # Separate the consonant at the start of the word
    prefixConsonats = ''
    while len(word)>0 and not word[0] in VOWELS:
        prefixConsonats += word[0]
        word = word[1:]
    
    # Add the pig latin ending to the word:
    if prefixConsonats != '':
        print("Prefix Consonants : " + prefixConsonats)
        word += prefixConsonats + 'ay'
    else:
        word += 'yay'
   
    # Set the word back to uppercase ot title if it was
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # Add the non letter back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single stirng:
print(' '.join(pigLatin))