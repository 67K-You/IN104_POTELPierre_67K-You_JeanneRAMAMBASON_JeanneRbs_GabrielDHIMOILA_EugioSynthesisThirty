# -*- coding: utf-8 -*-
#!/usr/bin/env python

#from videogames import *
import videogames
import unittest
from videogames import *

SmashBros = Fighting("fantasy",2,13)import VideoGames



class BadInputFighting(unittest.TestCase):
	def testnameofplayersknownnames(self):
		self.assertRaises(VideoGames.UnknownPlayerError, VideoGames.Fighting.nameofplayers, 'Jeanne')

   	def testequipweapon(self):
   		self.assertRaises(VideoGames.UnknownWeaponError, VideoGames.Fighting.equipweapon, 'Timer')

   	def testtimefightoolong(self):
   		"""in minute"""
   		self.assertRaises(VideoGames.OutOfRangeError, VideoGames.Fighting.timefight, 8)

   	def testZero(self):
   		self.assertRaises(VideoGames.OutOfRangeError, VideoGames.Fighting.timefight, 0)

   	def testNegative(self):
   		self.assertRaises(VideoGames.OutOfRangeError, VideoGames.Fighting.timefight, -3)

   	def testNonInteger(self):
   		self.assertRaises(VideoGames.NotIntergerError, VideoGames.Fighting.timefight, 0.5)
		
if __name__ == "__main__":
   unittest.main()
