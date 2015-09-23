# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:04:33 2015

@author: xavierduportet
"""

result = []

abc = "abcdefghijklmnopqrstuvwxyz"

for x in abc:
    for y in abc:
        if x != y:
            result.append(x+y)

for i in result:
    print(i)
