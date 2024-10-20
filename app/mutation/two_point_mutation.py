import random

from app.binary_chromosome import BinaryChromosome
from app.mutation.mutation_method import MutationMethod


class TwoPointMutation(MutationMethod):

    def __init__(self, probability_to_mutate):
        self.probability_to_mutate = probability_to_mutate

    def mutate(self, chromosomes_to_mutate):
        new_chromosomes = []
        for chromosome in chromosomes_to_mutate:
            new_gens_for_chromosome = list(chromosome.chromosome_data)

            if random.random() < self.probability_to_mutate:

                gene_to_mutate_1 = random.randint(0, len(new_gens_for_chromosome) - 1)
                gene_to_mutate_2 = random.randint(0, len(new_gens_for_chromosome) - 1)

                while gene_to_mutate_2 == gene_to_mutate_1:
                    gene_to_mutate_2 = random.randint(0, len(new_gens_for_chromosome) - 1)

                new_gens_for_chromosome[gene_to_mutate_1] = 1 if new_gens_for_chromosome[gene_to_mutate_1] == 0 else 0
                new_gens_for_chromosome[gene_to_mutate_2] = 1 if new_gens_for_chromosome[gene_to_mutate_2] == 0 else 0

            new_chromosomes.append(BinaryChromosome.copy_with_new_chromosomes(chromosome, new_gens_for_chromosome))

        return new_chromosomes
