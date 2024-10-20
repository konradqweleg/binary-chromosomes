from app.binary_chromosome import BinaryChromosome

class Population:
    def __init__(self, binary_length_calculator, population_size, lower_bounds, upper_bounds, num_variables):
        self.population_size = population_size
        self._chromosomes = [
            BinaryChromosome(binary_length_calculator, lower_bounds, upper_bounds, num_variables) for _ in
            range(population_size)
        ]

    def get_chromosomes(self):
        return self._chromosomes

    def evaluate(self, fitness_function):
        result = [fitness_function(chromosome.decode()) for chromosome in self._chromosomes]
        return result

    def __str__(self):
        return '\n'.join([str(chromosome) for chromosome in self._chromosomes])

    @property
    def chromosomes(self):
        return self._chromosomes