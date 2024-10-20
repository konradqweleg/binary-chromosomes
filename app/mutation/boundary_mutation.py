import random

from app.binary_chromosome import BinaryChromosome
from app.mutation.mutation_method import MutationMethod

import random
from app.binary_chromosome import BinaryChromosome
from app.mutation.mutation_method import MutationMethod


class BoundaryMutation(MutationMethod):

    def __init__(self, probability_to_mutate):
        self.probability_to_mutate = probability_to_mutate

    def mutate(self, chromosomes_to_mutate):
        new_chromosomes = []
        for chromosome in chromosomes_to_mutate:

            new_gens_for_chromosome = list(chromosome.chromosome_data)

            if random.random() < self.probability_to_mutate:

                if random.random() < 0.5:
                    gene_to_mutate = 0
                else:
                    gene_to_mutate = len(new_gens_for_chromosome) - 1

                new_gens_for_chromosome[gene_to_mutate] = 1 if new_gens_for_chromosome[gene_to_mutate] == 0 else 0

            new_chromosomes.append(BinaryChromosome.copy_with_new_chromosomes(chromosome, new_gens_for_chromosome))

        return new_chromosomes
