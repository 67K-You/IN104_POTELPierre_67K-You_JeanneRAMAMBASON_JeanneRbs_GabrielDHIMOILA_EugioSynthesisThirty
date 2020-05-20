
# -*- coding: utf-8 -*-

import GA
from GA import *
import time


#Define global variables
t=time.time()
file='small'
#file='medium'
#file='large'
#file='extralarge'
#file=file+'Rand'
file=file+'.txt'
numberofgenerations=10
sizeofpopulation=20
mu=0.02

#Genetic Algorithm
if __name__ == "__main__":
	setofintegers=txttoarray(file) #convert the text file to an array
	sizeofchromosome=setofintegers.shape[0]
	solutions=Generations(numberofgenerations,sizeofpopulation,sizeofchromosome) #initialize the solution as a composite class/matrix which contains every solution that existed
	
	for i in range(sizeofpopulation): #initialize the first generation randomly and evaluate the fitness function of the individuals
		solutions.generations[0].generation[i].setrandom_individuals()
		solutions.generations[0].generation[i].evaluate_fitness(mu,setofintegers)
	
	for j in range(1,numberofgenerations):#the breeding process
		for k in range(sizeofpopulation):
			parenta=solutions.generations[j-1].choice_crossover()#choose randomly two parents but try to maximise their fitness function
			parentb=solutions.generations[j-1].choice_crossover()
			solutions.generations[j].generation[k].chromosome=solutions.generations[j-1].generation[parenta].crossover_individuals(solutions.generations[j-1].generation[parentb].chromosome) #let them mate and create an offspring
			solutions.generations[j].generation[k].mutate_individuals() #the offspring mutates
			solutions.generations[j].generation[k].evaluate_fitness(mu,setofintegers) #define its fitness score
	elapsed=time.time()-t
	print(elapsed)#print how much time the genetic algorithm takes

#data treatment
	for i in range(numberofgenerations):
		solutions.generations[i].generation.sort(key=lambda individu: individu.fitnessscore,reverse=True)
		print(np.dot(solutions.generations[i].generation[0].chromosome,setofintegers))
		print(solutions.generations[i].generation[0].fitnessscore)
		print(solutions.generations[i].generation[0].chromosome)

