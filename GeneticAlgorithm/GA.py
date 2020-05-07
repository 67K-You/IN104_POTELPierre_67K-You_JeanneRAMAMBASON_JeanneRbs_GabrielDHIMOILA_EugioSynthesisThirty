# -*- coding: utf-8 -*-
import numpy as np
import random

#Define exceptions
class GeneticsError(Exception): pass

class Solution:
	def __init__(self,size):#give the size of the solution (it's suposed to be the same as the size of the set of integers)
		self.size=size

	def setrandom(self): #initialises the value of chromosome with 0 and 1 chosen at following a random uniform distribution
		self.chromosome=np.random.randint(2, self.size)

	def mutation(self): #randomly invert one of the allele of the chromosome
		i=random.randint(1,size)
		if self.chromosome[i]==1:
			self.chromosome[i]=0
		else:
			self.chromosome[i]=1



