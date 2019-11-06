# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:41:33 2019

@author: bharatagrawal
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from xml.etree import ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
counts=0
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx)

tree = ET.parse(html)

comments = tree.findall('comments/comment')

for comment in comments:
    counts = counts+int(comment.find('count').text)
print(counts)