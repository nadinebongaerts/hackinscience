# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:44:08 2015

@author: xavierduportet
"""

m = list()
for i in range(0, 1000):
    if(i % 3) == 0 or (i % 5) == 0:
        m.append(i)
print(sum(m))
