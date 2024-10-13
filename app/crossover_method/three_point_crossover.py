import random

from app.binary_chromosome import BinaryChromosome
from app.crossover_method.crossover_method import CrossoverMethod


class ThreePointCrossover(CrossoverMethod):

    def __init__(self, probability_to_crossover):
        self.probability_to_crossover = probability_to_crossover

    def crossover(self, chromosomes_to_crossover):
        new_chromosomes = []
        for i in range(0, len(chromosomes_to_crossover), 2):
            parent1, parent2 = chromosomes_to_crossover[i], chromosomes_to_crossover[i + 1]
            if random.random() < self.probability_to_crossover:
                points = sorted(random.sample(range(1, len(parent1.chromosome_data)), 3))
                child1_genes = (parent1.chromosome_data[:points[0]] + parent2.chromosome_data[points[0]:points[1]] +
                                parent1.chromosome_data[points[1]:points[2]] + parent2.chromosome_data[points[2]:])
                child2_genes = (parent2.chromosome_data[:points[0]] + parent1.chromosome_data[points[0]:points[1]] +
                                parent2.chromosome_data[points[1]:points[2]] + parent1.chromosome_data[points[2]:])

                new_child_1_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent1, child1_genes)
                new_child_2_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent2, child2_genes)
                new_chromosomes.extend([new_child_1_chromosomes, new_child_2_chromosomes])
            else:
                new_chromosomes.extend([parent1, parent2])
        return new_chromosomes