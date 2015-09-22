# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:35:51 2015

@author: Nadine Bongaerts
"""

phantom_menace = """Turmoil has engulfed the Galactic Republic. The\
 taxation of trade routes to outlying star systems is in\
 dispute. Hoping to resolve the matter with a blockade of deadly\
 battleships, the greedy Trade Federation has stopped all shipping to\
 the small planet of Naboo. While the congress of the Republic\
 endlessly debates this alarming chain of events, the Supreme\
 Chancellor has secretly dispatched two Jedi Knights, the guardians of\
 peace and justice in the galaxy, to settle the conflict"""
# print(phantom_menace.split())
# don't forget the () behind the .split
#Now the string has become a list,so you can count the number of words in the list
print(len(phantom_menace.split()))
