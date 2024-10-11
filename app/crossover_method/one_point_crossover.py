import random

from app.binary_chromosome import BinaryChromosome
from app.crossover_method.crossover_method import CrossoverMethod


class OnePointCrossover(CrossoverMethod):

    def __init__(self, probability_to_crossover):
        self.probability_to_crossover = probability_to_crossover
    def crossover(self, chromosomes_to_crossover):
        new_chromosomes = []
        for i in range(0, len(chromosomes_to_crossover), 2):
            parent1, parent2 = chromosomes_to_crossover[i], chromosomes_to_crossover[i + 1]
            if random.random() < self.probability_to_crossover:
                if len(parent1.chromosomes) > 1:
                    point = random.randint(1, len(parent1.chromosomes) - 1)
                    # Ensure the crossover point is even
                    while point % 2 != 0:
                        point = random.randint(1, len(parent1.chromosomes) - 1)
                else:
                    point = 1  # If the chromosome length is 1, the crossover point is set to 1

                child1_chromosomes = parent1.chromosomes[:point] + parent2.chromosomes[point:]
                child2_chromosomes = parent2.chromosomes[:point] + parent1.chromosomes[point:]

                new_child_1_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent1, child1_chromosomes)
                new_child_2_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent2, child2_chromosomes)
                new_chromosomes.extend([new_child_1_chromosomes, new_child_2_chromosomes])
            else:
                new_chromosomes.extend([parent1, parent2])
        return new_chromosomes