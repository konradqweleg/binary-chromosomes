import random
import logging
from app.binary_chromosome import BinaryChromosome
from app.crossover_method.crossover_method import CrossoverMethod

class OnePointCrossover(CrossoverMethod):

    def __init__(self, probability_to_crossover):
        self.probability_to_crossover = probability_to_crossover
        self.logger = logging.getLogger(__name__)

    def crossover(self, chromosomes_to_crossover, expected_new_population_size):
        self.logger.debug("Crossover Method: One Point Crossover")
        self.logger.debug("Probability to crossover: %s", self.probability_to_crossover)
        self.logger.debug("Chromosomes to crossover: %s", [str(chromosome) for chromosome in chromosomes_to_crossover])
        new_chromosomes = []

        while len(new_chromosomes) < expected_new_population_size:
            idx1, idx2 = random.sample(range(len(chromosomes_to_crossover)), 2)
            parent1, parent2 = chromosomes_to_crossover[idx1], chromosomes_to_crossover[idx2]
            if random.random() < self.probability_to_crossover:
                if len(parent1.chromosome_data) > 1:
                    point = random.randint(1, len(parent1.chromosome_data) - 1)
                else:
                    point = 1

                child1_chromosomes = parent1.chromosome_data[:point] + parent2.chromosome_data[point:]
                child2_chromosomes = parent2.chromosome_data[:point] + parent1.chromosome_data[point:]

                new_child_1_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent1, child1_chromosomes)
                new_child_2_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent2, child2_chromosomes)
                new_chromosomes.extend([new_child_1_chromosomes, new_child_2_chromosomes])

                self.logger.debug("Parent 1 chromosomes: %s", parent1)
                self.logger.debug("Parent 2 chromosomes: %s", parent2)
                self.logger.debug("New child 1 chromosomes: %s", new_child_1_chromosomes)
                self.logger.debug("New child 2 chromosomes: %s", new_child_2_chromosomes)

        new_chromosomes = new_chromosomes[:expected_new_population_size]

        self.logger.debug("Chromosomes after crossover: %s", [str(chromosome) for chromosome in new_chromosomes])
        return new_chromosomes

    def __str__(self):
        return "One Point Crossover"