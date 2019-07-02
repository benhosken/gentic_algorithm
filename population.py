class Population:
  def __init__(self, target, mutation_rate, pop_size):
    print("Population")
    self.target = target
    self.mutation_rate = mutation_rate
    self.pop_size = pop_size

  def is_finished(self):
    # should match the target against the best scoring DNA
    self.get_fittest().get_phrase() == self.target

  def perform_natural_selection(self):
    pass

  def generate(self):
    pass

  def calc_fitness(self):
    pass

  def evaluate(self):
    pass

  def get_fittest(self):
    pass
