# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:39:20 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import choice
m = [14,15,16,56,73,129]
r = choice(m)
print(r)
myID =mc.getPlayerEntityId("Er_ic28")
x,y,z = mc.entity.getTilePos(myID)
startX =x
list2 = [[12,41,14],[35,73,86]]
for i in list2:
    for j in i:    
        mc.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1