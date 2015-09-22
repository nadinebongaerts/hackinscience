# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:40:55 2015

@author: xavierduportet
"""

import datetime
today = datetime.date.today()
now = datetime.datetime.now().strftime("%H:%M:%S")
print('This is', today, 'and it is', now)
