# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:49:11 2015

@author: xavierduportet
"""

import sys
import operator
sys.argv
if len(sys.argv == 2):
    print(operator.add(int(sys.argv[1]), int(sys.argv[2])))
else:
    print('usage: python3 solution.py OP1 OP2')
