import logging
import random
from app.binary_chromosome import BinaryChromosome
from app.other_operations.operation import Operation


class InversionOperator(Operation):

    def __init__(self, probability_to_inversion):
        self.probability_to_mutate = probability_to_inversion
        self.logger = logging.getLogger(__name__)

    def apply(self, chromosomes_to_mutate):
        new_chromosomes = []
        for chromosome in chromosomes_to_mutate:
            new_gens_for_chromosome = list(chromosome.chromosome_data)
            self.logger.debug("chromosome: %s", chromosome.chromosome_data)

            if random.random() < self.probability_to_mutate:
                point1 = random.randint(0, len(new_gens_for_chromosome) - 2)
                point2 = random.randint(point1 + 1, len(new_gens_for_chromosome) - 1)

                self.logger.debug("point1: %d, point2: %d", point1, point2)
                self.logger.debug("left subarray: %s", new_gens_for_chromosome[point1:point2 + 1])
                self.logger.debug("right subarray: %s", new_gens_for_chromosome[point1:point2 + 1])
                self.logger.debug("right subarray after mutation: %s", new_gens_for_chromosome[point2 + 1:])

                new_gens_for_chromosome[point1:point2 + 1] = reversed(new_gens_for_chromosome[point1:point2 + 1])
                self.logger.debug("new_gens_for_chromosome: %s vs %s", new_gens_for_chromosome,
                                  chromosome.chromosome_data)

            new_chromosomes.append(BinaryChromosome.copy_with_new_chromosomes(chromosome, new_gens_for_chromosome))

        return new_chromosomes

    def __str__(self):
        return "Inversion operator"
