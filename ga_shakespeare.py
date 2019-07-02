from dna import DNA
from population import Population

def run():
  print("Running")

  target = "BENJAMIN"
  d1 = DNA(len(target))
  print(d1.getPhrase())

  d2 = DNA(len(target))
  print(d2.getPhrase())

  # print(d2.calcFitness(target))

  d12 = d1.crossover(d2)
  print(d12.getPhrase())

  d12.mutate(0.4)
  print(d12.getPhrase())

if __name__ == "__main__":
  run()




