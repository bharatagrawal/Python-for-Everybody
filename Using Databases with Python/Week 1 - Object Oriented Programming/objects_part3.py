# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:05:20 2019

@author: bharat
"""

class PartyAnimal:
    x = 0 
    name = ''
    
    def __init__(self,z):
        self.name = z
        print(self.name, " constructed")
        
    def party(self):
        self.x = self.x  + 1
        print(self.name, "pary count", self.x)
        
a = PartyAnimal('sally')
a.party()

b = PartyAnimal('jim')
b.party()
a.party()
        