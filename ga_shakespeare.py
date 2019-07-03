from population import Population

def run():
  print("Running")

  target = "To be of not to be."

  pop_size = 200
  mutation_rate = 0.015

  population = Population(target, mutation_rate, pop_size)
  # Calculate initial fitness
  population.calc_fitness()

  while not population.is_finished():
    # Mate and generate the next generation
    population.procreate()

    # Calculate fitness
    population.calc_fitness()

    fittest = population.get_fittest()
    print("Generation:", population.generation)
    print(fittest.get_phrase(), fittest.fitness)


if __name__ == "__main__":
  run()




