import random

from app.binary_chromosome import BinaryChromosome
from app.mutation.mutation_method import MutationMethod


class OnePointMutation(MutationMethod):

    def __init__(self, probability_to_mutate):
        self.probability_to_mutate = probability_to_mutate

    def mutate(self, chromosomes_to_mutate):
        new_chromosomes = []
        for chromosome in chromosomes_to_mutate:
            if random.random() < self.probability_to_mutate:
                # Mutate one random gene in each sublist
                mutated_genes = [sublist[:] for sublist in chromosome.chromosome_data]
                for sublist in mutated_genes:
                    if sublist:
                        point = random.randint(0, len(sublist) - 1)
                        sublist[point] = 1 - sublist[point]  # Assuming binary genes
                new_chromosome = BinaryChromosome.copy_with_new_chromosomes(chromosome, mutated_genes)
                new_chromosomes.append(new_chromosome)
            else:
                new_chromosomes.append(chromosome)
        return new_chromosomes