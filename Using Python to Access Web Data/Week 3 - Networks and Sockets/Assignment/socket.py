# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 01:29:43 2019

@author: Bharat Agrawal
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.orgcmd', 80))
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print (data);

mysock.close()