# -*- coding: utf-8 -*-

import unittest
import VideoGames
from VideoGames import *

racing = Racing("fantasy",2,"+3")



class Testspe(unittest.TestCase):
	def testtrack(self):
		self.assertEqual(racing.spe("Sunshine Airport"), "Sunshine Airport", "Should be Sunshine Airport")
	def testexistingtrack(self):
	   """spe should fail with tracks not part of the game"""
	   with self.assertRaises(UnknownTrackError):
			racing.spe("Baby Circuit")

class TestEngineCylinder(unittest.TestCase):
	def testCCpositive(self):
	   """EngineCylinder should fail with negative input"""
	   with self.assertRaises(OutOfRangeError):
			racing.EngineCylinder(-1)

	def testCCinteger(self):
	   """EngineCylinder should fail with non-integer input"""
	   with self.assertRaises(NotIntegerError):
			racing.EngineCylinder(0.5)

if __name__ == "__main__":
	unittest.main()
