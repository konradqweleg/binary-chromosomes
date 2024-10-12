import random

from app.binary_chromosome import BinaryChromosome
from app.crossover_method.crossover_method import CrossoverMethod


class GranularCrossover(CrossoverMethod):

    def __init__(self, probability_to_crossover, granularity=3):
        self.probability_to_crossover = probability_to_crossover
        self.granularity = granularity

    def crossover(self, chromosomes_to_crossover):
        new_chromosomes = []
        for i in range(0, len(chromosomes_to_crossover), 2):
            parent1, parent2 = chromosomes_to_crossover[i], chromosomes_to_crossover[i + 1]
            if random.random() < self.probability_to_crossover:
                child1_genes = []
                child2_genes = []
                for j in range(0, len(parent1.chromosomes), self.granularity):
                    if random.random() < 0.5:
                        child1_genes.extend(parent1.chromosomes[j:j + self.granularity])
                        child2_genes.extend(parent2.chromosomes[j:j + self.granularity])
                    else:
                        child1_genes.extend(parent2.chromosomes[j:j + self.granularity])
                        child2_genes.extend(parent1.chromosomes[j:j + self.granularity])

                new_child_1_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent1, child1_genes)
                new_child_2_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent2, child2_genes)
                new_chromosomes.extend([new_child_1_chromosomes, new_child_2_chromosomes])
            else:
                new_chromosomes.extend([parent1, parent2])
        return new_chromosomes