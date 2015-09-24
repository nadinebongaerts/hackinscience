# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:04:33 2015

@author: xavierduportet
"""

import itertools

for i in itertools.combinations('abcdefghijklmnopqrstuvwxyz', 2):
    print(i[0]+i[1])
