# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 22:12:34 2019

@author: bharat
"""

class PartyAnimal:
    x = 0
    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)
        
b = PartyAnimal()

print("Type ", type(b))
print("Dir ", dir(b))