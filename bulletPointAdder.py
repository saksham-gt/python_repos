# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 23:36:02 2020

@author: sg24x7
"""

#!/usr/bin/env python3
# bulletPointAdder.py - adds wikipedia bullet points to the start.
# to each line of the text on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO : separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):             # loop through all the strings in the "lines" list
    lines[i] = '* ' + lines[i]          # started the lines with '* ' 

# but now the final list we want that as a single string not a list of string (as in lines)
# hence now we join the string if lines.

text = '\n'.join(lines) 
pyperclip.copy(text)

 
