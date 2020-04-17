# -*- coding: utf-8 -*-
#!/usr/bin/env python

import VideoGames
import unittest
from VideoGames import *

SmashBros = Fighting("fantasy",2,13)


class BadInputFighting(unittest.TestCase):
   def testnameofplayer1knownnames(self):
      """nameofplayer1 should dail with name not in the list"""
      with self.assertRaises(UnknownPlayerError):
         SmashBros.nameofplayer1('Jeanne')

   def testequipweapon(self):
      """equiweapon should fail with name of weapons not in the list"""
      with self.assertRaises(UnknownWeaponError):
         SmashBros.equipweapon('Timer')

   def testtimefightoolong(self):
   	"""timefight should fail with time out of range"""
   	with self.assertRaises(OutOfRangeError):
         SmashBros.timefight(9)

   def testZero(self):
      """timefight should fail with zero input"""
      with self.assertRaises(OutOfRangeError):
         SmashBros.timefight(0)

   def testNegative(self):
      """timefight should fail with negative input"""
      with self.assertRaises(OutOfRangeError):
         SmashBros.timefight(-3)

   def testNonInteger(self):
      """timefight should fail with non-interger input"""
      with self.assertRaises(NotIntegerError):
         SmashBros.timefight(0.5)
		
if __name__ == "__main__":
   unittest.main()
