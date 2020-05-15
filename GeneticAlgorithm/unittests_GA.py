# -*- coding: utf-8 -*-

import unittest
import GA
from GA import *


class Testindividual(unittest.TestCase):
	def testchromosomesizeinteger(self):
	   """Individual.__init__ should fail with non-integer input"""
	   with self.assertRaises(NotIntegerError):
			Individual(0.5)
	def testchromosomesizepositive(self):
	   """Individual.__init__ should fail with negative input"""
	   with self.assertRaises(OutOfRangeError):
			Individual(-1)

class Testpopulation(unittest.TestCase):
	def testpopulationsizeinteger(self):
	   """Population.__init__ should fail with non-integer input"""
	   with self.assertRaises(NotIntegerError):
			Population(0.5,1)
	def testpopulationsizepositive(self):
	   """Population.__init__ should fail with negative input"""
	   with self.assertRaises(OutOfRangeError):
			Population(-1,1)


if __name__ == "__main__":
	unittest.main()