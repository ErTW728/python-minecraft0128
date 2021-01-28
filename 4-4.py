# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:36:51 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
myID =mc.getPlayerEntityId("Er_ic28")
mc.postToTitle(myID,"hello")
