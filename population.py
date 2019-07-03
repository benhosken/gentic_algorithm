from dna import DNA
import numpy as np

class Population:
  def __init__(self, target, mutation_rate, pop_size):
    print("Constructing Population")
    self.target = target
    self.mutation_rate = mutation_rate
    self.pop_size = pop_size

    self.population = list(map(lambda x: DNA(len(self.target)), range(pop_size)))

    self.fittest = None

    self.generation = 1

  def is_finished(self):
    # should match the target against the best scoring DNA
    if self.fittest == None:
      return False

    return self.fittest.get_phrase() == self.target


  def procreate(self):

    raw_fitnesses = np.array(list(map(lambda dna: dna.fitness, self.population)))

    selection_probabilities = raw_fitnesses / np.sum(raw_fitnesses)

    new_population = list()
    # generate the children by randomly selection two parents and crossing them over
    for i in range(self.pop_size):
      parent_a = np.random.choice(self.population, p=selection_probabilities)
      parent_b = np.random.choice(self.population, p=selection_probabilities)
      child = parent_a.crossover(parent_b)
      child.mutate(self.mutation_rate)
      new_population.append(child)

    self.population = new_population
    self.generation = self.generation + 1

  def calc_fitness(self):
    for dna in self.population:
      dna.calc_fitness(self.target)

  def get_fittest(self):
    self.fittest = None
    for dna in self.population:
      if self.fittest == None or dna.fitness > self.fittest.fitness:
        self.fittest = dna

    return self.fittest
