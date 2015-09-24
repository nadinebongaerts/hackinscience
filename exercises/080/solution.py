# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:04:33 2015

@author: xavierduportet
"""

import itertools

result = itertools.combinations('abcdefghijklmnopqrstuwvyz', 2)

for i in result:
    print(i)
