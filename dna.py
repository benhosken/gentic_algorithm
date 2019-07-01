import random

class DNA:
  @classmethod
  def newChar(cls):
    rand_ord = random.randrange(63, 122)
    if rand_ord == 63:
      rand_ord = 32
    elif rand_ord == 64:
      rand_ord = 46
    return chr(rand_ord)

  def __init__(self, gene_count):
    print("DNA")
    # The genetic sequence
    self.genes = list(map(lambda x: DNA.newChar(), range(gene_count)))

    # fitness score
    self.fitness = 0

  def getPhrase(self):
    return "".join(self.genes)

  def
