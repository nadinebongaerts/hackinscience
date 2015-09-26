# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:49:38 2015

@author: xavierduportet
"""

station = {
    'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
    'number': 31705,
    'latitude': 48.8645278209514,
    'name': 'CHAMPEAUX (BAGNOLET)',
    'longitude': 2.416170724425901
}

keyorder = ['latitude', 'longitude', 'number', 'name', 'address']
for i in sorted(station.items(), key=lambda i: keyorder.index(i[0])):
    print(i[0], i[1])
