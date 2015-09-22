# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:49:58 2015

@author: xavierduportet
"""
even = list()
for i in range(0, 101):
    if(i % 2) == 0:
        even.append(i)
print(sum(even))
