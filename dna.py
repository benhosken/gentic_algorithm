import random
import math

class DNA:
  @staticmethod
  def new_char():
    rand_ord = random.randrange(63, 122)
    if rand_ord == 63:
      rand_ord = 32
    elif rand_ord == 64:
      rand_ord = 46
    return chr(rand_ord)

  def __init__(self, gene_count):
    print("DNA")
    # The genetic sequence
    self.genes = list(map(lambda x: DNA.new_char(), range(gene_count)))

    # fitness score
    self.fitness = 0

  # Converts character array to a String
  def get_phrase(self):
    return "".join(self.genes)

  # Fitness function (returns floating point % of "correct" characters)
  def calcFitness(self, target):
    score = 0
    for idx, gene in enumerate(self.genes):
      if gene == target[idx]:
        score =+ 1
    return score / len(target)

  # Crossover
  def crossover(self, partner):
    # A new child
    child = DNA(len(self.genes))

    split_point = random.randrange(len(self.genes)) # Pick a split point

    child.genes = self.genes[:split_point] + partner.genes[split_point:]
    return child

  # Based on a mutation probability, picks a new random character
  def mutate(self, mutation_rate):
    for idx in range(len(self.genes)):
      if random.random() < mutation_rate:
        self.genes[idx] = DNA.new_char()

