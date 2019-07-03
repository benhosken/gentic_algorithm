import random
import math

class Chromosome:
  @staticmethod
  def new_char():
    rand_ord = random.randrange(63, 122)
    if rand_ord == 63:
      rand_ord = 32
    elif rand_ord == 64:
      rand_ord = 46
    return chr(rand_ord)

  def __init__(self, gene_count):
    # The genetic sequence
    self.genes = list(map(lambda x: Chromosome.new_char(), range(gene_count)))

    # fitness score
    self.fitness = 0

  # Converts character array to a String
  def get_phrase(self):
    return "".join(self.genes)

  # Fitness function (returns floating point % of "correct" characters)
  def calc_fitness(self, target):
    score = 0
    for idx, gene in enumerate(self.genes):
      if gene == target[idx]:
        score = score + 1
    self.fitness = score / len(target)
    return self.fitness

  # Crossover
  def crossover(self, partner):
    # New children
    child_1 = Chromosome(len(self.genes))
    child_2 = Chromosome(len(self.genes))

    # where to splice
    split_point = random.randrange(len(self.genes)) # Pick a split point

    # AB and BA
    child_1.genes = self.genes[:split_point] + partner.genes[split_point:]
    child_2.genes = partner.genes[:split_point] + self.genes[split_point:]
    return child_1, child_2

  # Based on a mutation probability, picks a new random character
  def mutate(self, mutation_rate):
    for idx in range(len(self.genes)):
      if random.random() < mutation_rate:
        self.genes[idx] = Chromosome.new_char()

