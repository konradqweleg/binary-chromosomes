import random

from app.binary_chromosome import BinaryChromosome
from app.mutation.mutation_method import MutationMethod

class InversionMutation(MutationMethod):

    def __init__(self, probability_to_mutate):
        self.probability_to_mutate = probability_to_mutate

    def mutate(self, chromosomes_to_mutate):
        new_chromosomes = []
        for chromosome in chromosomes_to_mutate:
            if random.random() < self.probability_to_mutate:
                # Perform inversion mutation on each sublist
                mutated_genes = [sublist[:] for sublist in chromosome.chromosomes]
                for sublist in mutated_genes:
                    if len(sublist) > 1:
                        start, end = sorted(random.sample(range(len(sublist)), 2))
                        sublist[start:end+1] = reversed(sublist[start:end+1])
                new_chromosome = BinaryChromosome.copy_with_new_chromosomes(chromosome, mutated_genes)
                new_chromosomes.append(new_chromosome)
            else:
                new_chromosomes.append(chromosome)
        return new_chromosomes