# -*- coding: utf-8 -*-
import numpy as np
import random

#Define exceptions
class GeneticsError(Exception): pass
class OutOfRangeError(GeneticsError): pass
class NotIntegerError(GeneticsError): pass
class IncompatibleChromosome(GeneticsError):pass

def txttoarray(file):#convert the txt input to an array
	setofintegers=np.loadtxt(file,skiprows=1,delimiter=', ')
	return setofintegers

def factor_partial(N):
	for R in xrange(int(np.sqrt(N)),1,-1):
		if N%R == 0 and np.gcd(R,N/R) == 1:
			return N/R, R

class Individual:
	def __init__(self,size):#give the size of the solution (it's suposed to be the same as the size of the set of integers)
		if size<=0:
			raise OutOfRangeError, "chromosomesize can't be a negative number"
		elif not size == int(size):
			raise NotIntegerError, "chromosomesize can't be a decimal number"
		self.size=size

	def setrandom_individuals(self,setofintegers): #initialises the value of chromosome with 0 and 1 chosen at following a random uniform distribution
		self.chromosome=np.zeros(self.size)
		for i in range (self.size):
			n=random.random()
			if (n>0.2 and setofintegers[i]>=0) or (n>0.995 and setofintegers[i]<0):
				self.chromosome[i]=1

	def mutate_individuals(self): #randomly invert one of the allele of the chromosome
		p=1/self.size
		for i in range(0,self.size):
			if random.uniform(0,1)<=p:
				self.chromosome[i]=abs(self.chromosome[i]-1)
				
	def crossover_individuals(self,parent_b):
		n=self.size
		m=np.size(parent_b)
		if m!=n :
			raise IncompatibleChromosome, "size of parent_b and self.chromosome must agree"
		i=random.randint(0,n-1)
		j=random.randint(0,n-1)
		enfant=np.zeros(n)
		s=random.random()
		if i>j:
			temp=i
			i=j
			j=temp
		if s<0.5:
			if i!=j:
				enfant[0:i]=self.chromosome[0:i]
				enfant[i+1:j]=parent_b[i+1:j]
				if j<n:
					enfant[j+1:n-1]=self.chromosome[j+1:n-1]
			else:
				enfant[0:i]=self.chromosome[0:i]
				enfant[i+1:n-1]=parent_b[i+1:n-1]
		else:
			if i!=j:
				enfant[0:i]=parent_b[0:i]
				enfant[i+1:j]=self.chromosome[i+1:j]
				if j<n:
					enfant[j+1:n-1]=parent_b[j+1:n-1]
			else:
				enfant[0:i]=parent_b[0:i]
				enfant[i+1:n-1]=self.chromosome[i+1:n-1]		
		return enfant


	def evaluate_fitness(self,mu,setofintegers):#the fitness function is designed to maximise the number of integers chosen and minimise the value of their sum. mu is a parameter between 0 and 1 that's meant to give a strong advanage to a solution whose sum is actually 0.
		n=np.dot(self.chromosome,np.ones(self.size))
		sigma=abs(np.dot(self.chromosome,setofintegers))
		self.fitnessscore=n/(sigma+mu)
		return self.fitnessscore

class Population:
	def __init__(self,populationsize,chromosomesize):#intialise the population of a generation by stocking it in an array of individuals.
		if populationsize<0:
			raise OutOfRangeError, "populationsize can't be a negative number"
		elif not populationsize == int(populationsize):
			raise NotIntegerError, "populationsize can't be a decimal number"
		self.populationsize=populationsize
		self.generation=[Individual(chromosomesize) for i in range (populationsize)]
		self.totalcalculated=False

	
	def choice_crossover(self): #randomly chooses 1 parent who is going to breed based on its fitness function
		if not self.totalcalculated:
			self.total=0 #it is the sum of all the values of the fitness functions of a population
			for i in range(self.populationsize):
				self.total+=self.generation[i].fitnessscore
			self.totalcalculated=True
		n=random.random()
		i=0
		s=self.generation[0].fitnessscore
		s=s/self.total
		while (i<self.populationsize and s<n):
			i+=1
			s+=self.generation[i].fitnessscore/self.total
		return i 

class Generations:
	def __init__(self,generationsnumber,populationsize,chromosomesize):
		if generationsnumber<0:
			raise OutOfRangeError, "generationsnumber must be a positive number"
		elif not generationsnumber == int(generationsnumber):
			raise NotIntegerError, "generationsnumber must be an integer"
		self.size=generationsnumber
		self.generations=[Population(populationsize,chromosomesize) for i in range(generationsnumber)]
	
	
