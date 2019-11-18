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
        print(self.name, "party count", self.x)



#FootballFan is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal and more.
class FootballFan(PartyAnimal):
    points = 0
    
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points",self.points)


s = PartyAnimal('sally')
s.party()

j = FootballFan('yash')
j.party()
j.touchdown()

        