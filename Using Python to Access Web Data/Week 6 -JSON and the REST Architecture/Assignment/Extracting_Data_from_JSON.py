# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 02:20:29 2019

@author: Admin
"""

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', 'http://py4e-data.dr-chuck.net/comments_300752.json')

html = urllib.request.urlopen(url)
html = html.read().decode()
print('Retrieved', len(html), 'characters')

sum = 0
count = 0
try:
    js = json.loads(html)
except:
    js = None
	
for item in js['comments']:
	count += 1
	sum += int(item['count'])
	
print('Count:', count)
print('Sum:', sum)