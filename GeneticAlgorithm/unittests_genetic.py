# -*- coding: utf-8 -*-

import unittest
import genetic
from genetic import *

class Testindividual(unittest.TestCase):
	def testmutate(self):
		"""mutate should fail if not (0<=rate<=1)"""
		with self.assertRaises(OutOfRangeError):
			Individual.mutate(self,-1)
        
class Testpopulation(unittest.TestCase):
	def testpopulationsizeinteger(self):
		"""Population.__init__ should fail with non-integer input"""
		with self.assertRaises(NotIntegerError):
			Population(0.5,[1,2])
	
	def testpopulationsizepositive(self):
		"""Population.__init__ should fail with negative input"""
		with self.assertRaises(OutOfRangeError):
			Population(-1,[1,2])
	
	
	def testliste(self):
		"""Population.__init__ should fail if liste is not a type 'list'"""
		with self.assertRaises(NotListError):
			Population(3,2)
      
class Testget_sub_list(unittest.TestCase):
	def testlist(self):
		""" get_sub_list should fail if len(liste)=0"""
		with self.assertRaises(OutOfRangeError):
			get_sub_list([])
		
	def testpositiveiteration(self):
		""" get_sub_list should fail if iteration<=0"""
		with self.assertRaises(OutOfRangeError):
			get_sub_list([1,2],10,-1)
				
	def testintegeriteration(self):
		"""get_sub_list should fail if iteration is non-integer"""
		with self.assertRaises(NotIntegerError):
			get_sub_list([1,2],10,0.5)
				
if __name__ == "__main__":
	unittest.main()
