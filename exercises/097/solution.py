# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:58:49 2015

@author: xavierduportet
"""


def love_meet(bob, alice):
    return set(bob) & set(alice)


def affair_meet(bob, alice, silvester):
    l = set(alice) & set(silvester)
    return l - set(bob)
