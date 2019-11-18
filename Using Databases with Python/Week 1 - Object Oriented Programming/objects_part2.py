# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:29:47 2019

@author: bharat
"""

class PartyAnimal:

    x = 0 
    
    def __init__(self):
        print("I am constructed")
        
    def party(self):
        self.x = self.x + 1
        print('so far', self.x)
        
    def __del__(self):
        print("I am destructed")
        
    if __name__ == '__main__':
        an = PartyAnimal()
        an.party()
        an.party()
        an = 42
        print("an contains",an)
        
        