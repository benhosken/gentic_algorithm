from chromosome import Chromosome
import numpy as np

class Population:
  def __init__(self, target, mutation_rate, pop_size):
    print("Constructing Population")
    self.target = target
    self.mutation_rate = mutation_rate
    self.passthrough_rate = 0.4
    self.pop_size = pop_size

    self.population = list(map(lambda x: Chromosome(len(self.target)), range(pop_size)))

    self.fittest = None

    self.generation = 1

  def is_finished(self):
    # should match the target against the best scoring Chromosome
    if self.fittest == None:
      return False

    return self.fittest.get_phrase() == self.target


  def procreate(self):

    raw_fitnesses = np.array(list(map(lambda chromosome: chromosome.fitness, self.population)))

    selection_probabilities = raw_fitnesses / np.sum(raw_fitnesses)

    passthrough_count = int(self.pop_size * self.passthrough_rate)
    top_chromes = np.argpartition(raw_fitnesses, -passthrough_count)[-passthrough_count:]
    new_population = list()
    for i in top_chromes:
      new_population.append(self.population[i])

    # generate the children by randomly selection two parents and crossing them over
    for i in range(int((self.pop_size - passthrough_count) / 2)):
      parent_a = np.random.choice(self.population, p=selection_probabilities)
      parent_b = np.random.choice(self.population, p=selection_probabilities)
      child_ab, child_ba = parent_a.crossover(parent_b)
      child_ab.mutate(self.mutation_rate)
      child_ba.mutate(self.mutation_rate)
      new_population.append(child_ab)
      new_population.append(child_ba)

    self.population = new_population
    self.generation = self.generation + 1

  def calc_fitness(self):
    for chromosome in self.population:
      chromosome.calc_fitness(self.target)

  def get_fittest(self):
    raw_fitnesses = np.array(list(map(lambda chromosome: chromosome.fitness, self.population)))
    self.fittest = self.population[np.argmax(raw_fitnesses)]

    return self.fittest
