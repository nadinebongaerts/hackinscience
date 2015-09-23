# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:29:45 2015

@author: xavierduportet
"""

keywords = []
abc = "abcdefghijklmnopqrstuvwxyz"
abcd = list(abc)
for x in abcd:
    for y in abcd:
            keywords.append(x+y)
for i in keywords:
    print(i)
