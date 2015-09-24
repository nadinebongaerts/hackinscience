# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:53:03 2015

@author: xavierduportet
"""

import operator


def sort_by_name(my_class):
    name = operator.itemgetter(1)
    return sorted(my_class, key=name)
