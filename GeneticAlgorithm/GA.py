# -*- coding: utf-8 -*-
import numpy as np
import random

#Define exceptions
class GeneticsError(Exception): pass
class OutOfRangeError(GeneticsError): pass
class NotIntegerError(GeneticsError): pass

class Individual:
	def __init__(self,size):#give the size of the solution (it's suposed to be the same as the size of the set of integers)
		if size<0:
			raise OutOfRangeError, "chromosomesize can't be a negative number"
		elif not size == int(size):
			raise NotIntegerError, "chromosomesize can't be a decimal number"
		self.size=size

	def setrandom_individuals(self): #initialises the value of chromosome with 0 and 1 chosen at following a random uniform distribution
		self.chromosome=np.random.randint(2, self.size)

	def mutate_individuals(self): #randomly invert one of the allele of the chromosome
		p=1/self.size
		for i in range(1,self.size+1):
			if random.uniform(0,1)<=p:
				self.chromosome[i]=abs(self.chromosome[i]-1)

	def evaluate_fitness(self,mu):#the fitness function is designed to maximise the number of integers chosen and minimise the value of their sum. mu is a parameter between 0 and 1 that's meant to give a strong advanage to a solution whose sum is actually 0.
		n=np.dot(self.chromosome,np.ones((self.size,1)))
		sigma=abs(np.dot(self.chromosome,setofintegers))
		self.fitnessscore=n/(sigma+mu)

class Population:
	def __init__(self,populationsize,chromosomesize):#intialise the population of a generation by stocking it in an array of individuals.
		if populationsize<0:
			raise OutOfRangeError, "populationsize can't be a negative number"
		elif not populationsize == int(populationsize):
			raise NotIntegerError, "populationsize can't be a decimal number"
		self.size=populationsize
		self.generation=np.array(populationsize,dtype=numpy.object)
		for i in range(1,populationsize+1):
			self.generation[i]=Individual(chromosomesize)