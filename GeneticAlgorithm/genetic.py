import random as rand
from math import *

class Individual:
	def __init__(self, liste, chromosome = None):
		self.liste = liste
		self.length = len(liste)

		if chromosome is None:
			self.chromosome = [rand.randint(0, 1) for i in range(self.length)]
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


class Population:
	def __init__(self, size, liste):
		self.size = size
		self.liste = liste
		self.individuals = [Individual(liste) for i in range(size)]
		self.best = None
		self.nb_generations = 0
		self.evaluate_individuals()

	def select_individuals(self):
		selected = [Individual(self.liste, chromosome = self.best.chromosome)]
		parents = rand.choices(self.individuals, weights = self.scores, k = 2 * self.size)

		for i in range(1, self.size):
			selected.append(Individual.crossover(parents[2 * i], parents[2 * i + 1]))

		self.individuals = selected

	def mutate_individuals(self, rate = 0.1):
		for individual in self.individuals:
			individual.mutate(rate)

	def evaluate_individuals(self):
		for individual in self.individuals:
			individual.evaluate_fitness()

		sort_key = lambda individual : individual.score
		self.individuals = sorted(self.individuals, key = sort_key, reverse = True)
		self.scores = [individual.score for individual in self.individuals]

		if self.best is None or self.best.score < self.scores[0]:
			self.best = self.individuals[0]
			self.best_score = self.scores[0]

	def next_generation(self, mutation_rate = 0.1):
		self.select_individuals()
		self.mutate_individuals(rate = mutation_rate)
		self.evaluate_individuals()
		self.nb_generations += 1

	def __str__(self):
		return str(self.scores)


def get_sub_list(liste, pop_size = 1000, iterations = 1000, print_progression = False):
	pop = Population(pop_size, liste)
	last_print = -0.01
	mutation_rate = 2 / len(liste)

	for i in range(iterations):
		if print_progression and i / iterations >= last_print + 0.01:
			last_print += 0.01
			print((100 * i) // iterations, "% best length = ", len(pop.best.get_sub_list()), ", sum = ", sum(pop.best.get_sub_list()), sep = "")

		pop.next_generation(mutation_rate = mutation_rate)

	return pop.best.get_sub_list()


if __name__ == "__main__":
	inputs = list(set([rand.randint(-8192, 8192) * 8192 + rand.randint(-8192, 8192) for i in range(10000)]))
	print("inputs =", inputs)
	outputs = get_sub_list(inputs, pop_size = 1000, iterations = 100, print_progression = True)
	print("\ninputs =", inputs, "\noutputs =", outputs, "\nlength =", len(outputs), "sum =", sum(outputs))