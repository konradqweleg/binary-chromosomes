import random
import logging

from app.binary_chromosome import BinaryChromosome
from app.mutation.mutation_method import MutationMethod


class OnePointMutation(MutationMethod):

    def __init__(self, probability_to_mutate):
        self.probability_to_mutate = probability_to_mutate
        self.logger = logging.getLogger(__name__)

    def mutate(self, chromosomes_to_mutate):
        self.logger.debug("Mutating method [one point mutation]")
        new_chromosomes = []
        for chromosome in chromosomes_to_mutate:
            new_gens_for_chromosome = list(chromosome.chromosome_data)
            self.logger.debug(f"Original chromosome: {new_gens_for_chromosome}")

            if random.random() < self.probability_to_mutate:
                gene_to_mutate = random.randint(0, len(new_gens_for_chromosome) - 1)
                self.logger.debug(f"Mutating gene at position {gene_to_mutate}")

                if new_gens_for_chromosome[gene_to_mutate] == 0:
                    new_gens_for_chromosome[gene_to_mutate] = 1
                else:
                    new_gens_for_chromosome[gene_to_mutate] = 0

                self.logger.debug(f"Mutated chromosome: {new_gens_for_chromosome}")

            new_chromosomes.append(BinaryChromosome.copy_with_new_chromosomes(chromosome, new_gens_for_chromosome))

        return new_chromosomes

    def __str__(self):
        return "One point mutation"