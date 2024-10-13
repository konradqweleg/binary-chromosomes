import random

from app.binary_chromosome import BinaryChromosome
from app.mutation.mutation_method import MutationMethod


class BoundaryMutation(MutationMethod):

    def __init__(self, probability_to_mutate):
        self.probability_to_mutate = probability_to_mutate

    def mutate(self, chromosomes_to_mutate):
        print("Chromosomes to mutate !!", [str(chromosome) for chromosome in chromosomes_to_mutate])
        new_chromosomes = []
        for chromosome in chromosomes_to_mutate:
            if random.random() < self.probability_to_mutate:
                # Mutate the first and last gene of each sublist
                mutated_genes = [sublist[:] for sublist in chromosome.chromosome_data]
                for sublist in mutated_genes:
                    if sublist:
                        sublist[0] = 1 - sublist[0]  # Assuming binary genes
                        sublist[-1] = 1 - sublist[-1]
                new_chromosome = BinaryChromosome.copy_with_new_chromosomes(chromosome, mutated_genes)
                new_chromosomes.append(new_chromosome)
            else:
                new_chromosomes.append(chromosome)
        print("Chromosomes after mutate !!", [str(chromosome) for chromosome in chromosomes_to_mutate])
        print("MUTATE:" + str(new_chromosomes))
        return new_chromosomes