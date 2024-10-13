import random

from app.binary_chromosome import BinaryChromosome
from app.mutation.mutation_method import MutationMethod


class OnePointMutation(MutationMethod):

    def __init__(self, probability_to_mutate):
        self.probability_to_mutate = probability_to_mutate

    def mutate(self, chromosomes_to_mutate):
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
            new_chromosomes.append(BinaryChromosome.copy_with_new_chromosomes(chromosome,new_gens_for_chromosome))
        return new_chromosomes