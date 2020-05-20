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
	def testcrossover_individuals(self):
		""" crossover_individuals should fail if parent_b doesn't have the same size as self.chromosone"""
		      with self.assertRaises(IncompatibleChromosome):
				Individual.crossover_individuals(self,self.chromosone+[0])
	def testevaluate_fitness(self):
		""" evaluate_fitness should fail if mu is negative """ 
		setofintegers=txttoarray('small.txt')
		with self.assertRaises(OutOfRangeError):
			Individual.evaluate_fitness(self,-1,setofintegers)

class Testpopulation(unittest.TestCase):
	def testpopulationsizeinteger(self):
	   """Population.__init__ should fail with non-integer input"""
	   with self.assertRaises(NotIntegerError):
			Population(0.5,1)
	def testpopulationsizepositive(self):
	   """Population.__init__ should fail with negative input"""
	   with self.assertRaises(OutOfRangeError):
			Population(-1,1)

class Testgenerations(unittest.TestCase):
	def testgenrationsnumberinteger(self):
	   """Generations.__init__ should fail with non-integer input"""
	   with self.assertRaises(NotIntegerError):
			Generations(0.8,1,10)
	def testgenerationsnumberpositive(self):
	   """Generations.__init__ should fail with negative input"""
	   with self.assertRaises(OutOfRangeError):
			Generations(-1,1,10)


if __name__ == "__main__":
	unittest.main()
