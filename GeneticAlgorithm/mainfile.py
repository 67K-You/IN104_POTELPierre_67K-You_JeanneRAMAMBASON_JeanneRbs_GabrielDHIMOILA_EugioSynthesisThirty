
# -*- coding: utf-8 -*-

import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm

#Define global variables
t=time.time()
#file='small'
#file='medium'
#file='large'
file='extraLarge'
#file=file+'Rand'
if file=='large':
	import GAmodified
	from GAmodified import *
else:
	import GA
	from GA import *
output=file
output=output+'sol.out'
file=file+'.txt'
numberofgenerations=50
sizeofpopulation=30
mu=0.02
visualisation1=False #plots the fitnessscore of a whole population as a graph which goes to the next generation every second
visualisation2=False #shows a visual representation of the pick rate of the integers which goes to the next generation every second
#both visualisations output a mp4 video in the current working directory

#Genetic Algorithm
if __name__ == "__main__":
	setofintegers=txttoarray(file) #convert the text file to an array
	sizeofchromosome=setofintegers.shape[0]
	solutions=Generations(numberofgenerations,sizeofpopulation,sizeofchromosome) #initialize the solution as a composite class/matrix which contains every solution that existed
	
	for i in range(sizeofpopulation): #initialize the first generation randomly and evaluate the fitness function of the individuals
		solutions.generations[0].generation[i].setrandom_individuals(setofintegers)
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


#only for animation and visualisation purpose
#data treatment no genetic algorithmic involved
	somme=0
	indice=0
	nombreentiers=0
	for i in range(numberofgenerations):
		solutions.generations[i].generation.sort(key=lambda individu: individu.fitnessscore,reverse=True)
		if np.dot(solutions.generations[i].generation[0].chromosome,setofintegers)==0 and i+1!=indice and np.dot(solutions.generations[i].generation[0].chromosome,np.ones(sizeofchromosome))>nombreentiers:
			indice=i+1
			nombreentiers=np.dot(solutions.generations[i].generation[0].chromosome,np.ones(sizeofchromosome))
	print('indice=')
	print(indice)
	print('nombre d entiers=')
	print(nombreentiers)
	print(elapsed)
	np.savetxt(output,solutions.generations[indice-1].generation[0].chromosome,delimiter=', ')
	if visualisation1: 

		fig, ax = plt.subplots()
		xdata, ydata = np.linspace(0,sizeofpopulation-1,num=sizeofpopulation), [solutions.generations[0].generation[k].fitnessscore for k in range(sizeofpopulation)]
		ln, = plt.plot([], [], '-o')


		def init():
			ax.set_xlim(0, sizeofpopulation-1)
			ax.set_ylim(0, solutions.generations[i].generation[0].fitnessscore+2)


		def update(frame):
			ydata=[solutions.generations[frame].generation[k].fitnessscore for k in range(sizeofpopulation)]
			ln.set_data(xdata, ydata)
			ax.set_ylim(0, np.amax(ydata))
			return ln,
 
		anim = animation.FuncAnimation(fig, update, frames=numberofgenerations,init_func=init,interval=10000/numberofgenerations)
		anim.save('fitnessscoreovertime.mp4',writer='ffmpeg')
		plt.show()

	if visualisation2:

		(a,b)=factor_partial(sizeofchromosome)
		print(a)
		print(b)
		fig=plt.figure()
		X=np.zeros(sizeofchromosome)
		for k in range(sizeofpopulation):
			X=np.add(X,solutions.generations[0].generation[k].chromosome)
		p=float(sizeofpopulation)
		X/=p
		print(X)
		X=X.reshape((b,a))
		print(X)
		i = plt.imshow(X, cmap=cm.Reds, interpolation='nearest',animated=True)


		def update(frame):
			X=solutions.generations[frame].generation[0].chromosome
			for k in range(1,sizeofpopulation):
				X=np.add(X,solutions.generations[frame].generation[k].chromosome)
			X/=sizeofpopulation

			X=X.reshape((b,a))
			i.set_array(X)
			return [i]


		anim = animation.FuncAnimation(fig, update, frames=numberofgenerations,interval=10000/numberofgenerations,blit=True)
		anim.save('numberpickrateovertime.mp4',writer='ffmpeg')
		plt.show()





