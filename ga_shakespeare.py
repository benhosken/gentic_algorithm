from dna import DNA
from population import Population

def run():
  print("Running")

  target = "BENJAMIN"
  d1 = DNA(len(target))
  print(d1.get_phrase())

  d2 = DNA(len(target))
  print(d2.get_phrase())

  # print(d2.calcFitness(target))

  d12 = d1.crossover(d2)
  print(d12.get_phrase())

  d12.mutate(0.4)
  print(d12.get_phrase())

  pop_size = 20
  mutation_rate = 0.01

  population = Population(target, mutation_rate, pop_size)

  while !population.is_finished:
    # Generate mating pool
    population.perform_natural_selection()
    # Create next generation
    population.generate()
    # Calculate fitness
    population.calc_fitness()

    population.evaluate()

    print(population.get_fittest())


if __name__ == "__main__":
  run()




