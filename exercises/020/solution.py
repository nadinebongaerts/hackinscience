# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:24:36 2015

@author: xavierduportet
"""

import sys
import operator
sys.argv
if len(sys.argv) == 3:
    print(operator.sub(int(sys.argv[1]), int(sys.argv[2])))
else:
    print('usage: python3 solution.py OP1 OP2')
