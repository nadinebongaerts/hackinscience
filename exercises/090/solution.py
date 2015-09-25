# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:49:39 2015

@author: xavierduportet
"""

import sys


def order(l):
    return list(enumerate(l))

l = sys.argv
order(l)

for i in order(l):
    print(i[0], i[1])
