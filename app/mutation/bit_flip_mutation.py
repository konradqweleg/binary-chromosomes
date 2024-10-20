import random
import logging

from app.binary_chromosome import BinaryChromosome
from app.mutation.mutation_method import MutationMethod


class BitFlipMutation(MutationMethod):

    def __init__(self, probability_to_mutate):
        self.probability_to_mutate = probability_to_mutate
        self.logger = logging.getLogger(__name__)

    def mutate(self, chromosomes_to_mutate):
        self.logger.debug("Mutating method [bit flip mutation]")
        new_chromosomes = []
        for chromosome in chromosomes_to_mutate:
            new_gens_for_chromosome = []
            for gens in chromosome.chromosome_data:
                if random.random() < self.probability_to_mutate:
                    if gens == 0:
                        new_gens_for_chromosome.append(1)
                    else:
                        new_gens_for_chromosome.append(0)
                else:
                    new_gens_for_chromosome.append(gens)
            new_chromosome = BinaryChromosome.copy_with_new_chromosomes(chromosome, new_gens_for_chromosome)
            new_chromosomes.append(new_chromosome)
            self.logger.debug(f'Mutated chromosome: {new_chromosome.chromosome_data}')
        return new_chromosomes

    def __str__(self):
        return "Bit flip mutation"