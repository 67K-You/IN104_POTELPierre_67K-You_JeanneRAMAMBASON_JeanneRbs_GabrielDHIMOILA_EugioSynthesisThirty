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
		for i in range(0,self.size):
			if random.uniform(0,1)<=p:
				self.chromosome[i]=abs(self.chromosome[i]-1)
				
	def crossover_individuals(self,parent_b):
		n=self.size
		m=np.size(parent_b)
		if m!=n :
			raise IncompatibleChromosome, "size of parent_b and self.chromosone must agree"
		i=rand.randint(0,n-1)
		j=rand.randint(0,n-1)
		enfant=np.zeros(n)
		s=random()
		if i>j:
			temp=i
			i=j
			j=temp
		if s<0.5:
			if i!=j:
				enfant[0:i]=self.chrosomone[0:i]
				enfant[i+1:j]=parent_b[i+1:j]
				if j<n:
					enfant[j+1:n-1]=self.chromosone[j+1:n-1]
			else:
				enfant[0:i]=self.chrosomone[0:i]
				enfant[i+1:n-1]=parent_b[i+1:n-1]
		else:
			if i!=j:
				enfant[0:i]=parent_b[0:i]
				enfant[i+1:j]=self.chrosomone[i+1:j]
				if j<n:
					enfant[j+1:n-1]=parent_b[j+1:n-1]
			else:
				enfant[0:i]=parent_b[0:i]
				enfant[i+1:n-1]=self.chrosomone[i+1:n-1]		
		return enfant


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
		for i in range(0,populationsize):
			self.generation[i]=Individual(chromosomesize)

	
		def choice_crossover(self):
			total=0
			for i in range(self.size):
				total+=self.generation[i].fitnessscore
			n=random()
			i=0
			s=self.generation[0].fitnessscore/total
			while i<self.size and s<n:
				i+=1
				s+=self.generation[i].fitnessscore/total
			return i 

class Generations:
	def __init__(self,generationsnumber,populationsize):
		if generationsnumber<0:
			raise OutOfRangeError, "generationsnumber must be a positive number"
		elif not generationsnumber == int(generationsnumber):
			raise NotIntegerError, "generationsnumber must be an integer"
		self.size=generationsnumber
		self.generations=np.array(generationsnumber,populationsize,dtype=numpy.object)
		for i in range(0,generationsnumber):
			for j in range(0,populationsize):
				self.generations[i,j]=Individual(chromosomesize)
	
	
	
