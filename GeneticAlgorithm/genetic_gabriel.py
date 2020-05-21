import random as rand
from threading import Thread
from math import *

NB_THREADS = 8 # 1 ou 0 = no multi threading

class Individual:
	def __init__(self, liste, chromosome = None):
		self.liste = liste
		self.length = len(liste)

		if chromosome is None:
			self.chromosome = [int(rand.random() < 0.5) for i in range(self.length)]
		else:
			self.chromosome = list(chromosome)

		self.score = 0

	@staticmethod
	def crossover(parent1, parent2):
		chromosome = []

		for i in range(parent1.length):
			if rand.randint(0, 1):
				chromosome.append(parent1.chromosome[i])
			else:
				chromosome.append(parent2.chromosome[i])

		return Individual(parent1.liste, chromosome = chromosome)

	def evaluate_fitness(self):
		from math import exp
		sub_liste = self.get_sub_list()
		s = sum(sub_liste)
		self.score = 1 + len(sub_liste) if s == 0 else 1 / (1 + abs(s))
		return self.score

	def mutate(self, rate):
		for i in range(self.length):
			if rand.random() < rate:
				self.chromosome[i] = 1 - self.chromosome[i]

	def get_sub_list(self):
		return [self.liste[i] for i, e in enumerate(self.chromosome) if e]

	def __str__(self):
		return str(self.score)

class MutationThread(Thread):
	def __init__(self, individuals, rate, imin, imax):
		Thread.__init__(self)
		self.individuals = individuals
		self.rate = rate
		self.imin = imin
		self.imax = imax

	def run(self):
		for i in range(self.imin, self.imax):
			self.individuals[i].mutate(self.rate)

class EvaluationThread(Thread):
	def __init__(self, individuals, imin, imax):
		Thread.__init__(self)
		self.individuals = individuals
		self.imin = imin
		self.imax = imax

	def run(self):
		for i in range(self.imin, self.imax):
			self.individuals[i].evaluate_fitness()

class Population:
	def __init__(self, size, liste):
		self.size = size
		self.liste = liste
		self.individuals = [Individual(liste) for i in range(size)]
		self.best = None
		self.best_generation = 0
		self.nb_generations = 0
		self.evaluate_individuals()

	def select_individuals(self):
		selected = [Individual(self.liste, chromosome = self.best.chromosome)]
		parents = rand.choices(self.individuals, weights = self.scores, k = 2 * self.size)

		for i in range(1, self.size):
			selected.append(Individual.crossover(parents[2 * i], parents[2 * i + 1]))

		self.individuals = selected

	def mutate_individuals(self, rate = 0.1):
		if NB_THREADS <= 1:
			for individual in self.individuals:
				individual.mutate(rate)
		else:
			threads = []

			for i in range(NB_THREADS):
				imin = int(i / NB_THREADS * self.size)
				imax = int((i + 1) / NB_THREADS * self.size)
				t = MutationThread(self.individuals, rate, imin, imax)
				t.start()
				threads.append(t)

			for t in threads:
				t.join()

	def evaluate_individuals(self):
		if NB_THREADS <= 1:
			for individual in self.individuals:
				individual.evaluate_fitness()
		else:
			threads = []

			for i in range(NB_THREADS):
				imin = int(i / NB_THREADS * self.size)
				imax = int((i + 1) / NB_THREADS * self.size)
				t = EvaluationThread(self.individuals, imin, imax)
				t.start()
				threads.append(t)

			for t in threads:
				t.join()

		sort_key = lambda individual : individual.score
		self.individuals = sorted(self.individuals, key = sort_key, reverse = True)
		self.scores = [individual.score for individual in self.individuals]

		if self.best is None or self.best.score < self.scores[0]:
			self.best = self.individuals[0]
			self.best_score = self.scores[0]
			self.best_generation = self.nb_generations

	def next_generation(self, mutation_rate = 0.1):
		self.nb_generations += 1
		self.select_individuals()
		self.mutate_individuals(rate = mutation_rate)
		self.evaluate_individuals()

	def __str__(self):
		return str(self.scores)


def get_sub_list(liste, pop_size = 1000, generations = 1000, print_progression = False):
	pop = Population(pop_size, liste)
	last_print = -0.01
	mutation_rate = 1 / len(liste)

	for i in range(generations):
		if print_progression and i / generations >= last_print + 0.01:
			last_print += 0.01
			print((100 * i) // generations, "% best length = ", len(pop.best.get_sub_list()), ", sum = ", sum(pop.best.get_sub_list()), sep = "")

		pop.next_generation(mutation_rate = mutation_rate)

	return pop.best.get_sub_list(), pop.best_generation


if __name__ == "__main__":
	#inputs = list(set([512 * rand.randint(-512, 512) + rand.randint(-512, 512) for i in range(1000)]))
	inputs = []

	with open("extralarge.txt", "r") as file:
		file.readline()
		line = file.readline()
		inputs = line.split(", ")
		inputs = [int(i) for i in inputs]
		print(inputs)

	import time
	t0 = time.time()
	print("inputs =", inputs, "\n")
	outputs, best_generations = get_sub_list(inputs, pop_size = 100, generations = 100, print_progression = True)
	print("\ninputs =", inputs, "\noutputs =", outputs)
	print()
	print("\nlength = ", len(outputs), ", sum = ", sum(outputs), ", atteint en ", best_generations, " generations.", sep="")
	print("programme terminé en", time.time() - t0, "s.")