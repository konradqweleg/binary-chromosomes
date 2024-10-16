import random
from app.binary_chromosome import BinaryChromosome
from app.crossover_method.crossover_method import CrossoverMethod

class GranularCrossover(CrossoverMethod):

    def __init__(self, probability_to_crossover, block_size, probability_to_crossover_block):
        self.probability_to_crossover = probability_to_crossover
        self.block_size = block_size
        self.probability_to_crossover_block = probability_to_crossover_block

    def crossover(self, chromosomes_to_crossover, expected_new_population_size):
        print("\n")
        print("Crossover Method: Granular Crossover")
        print("Probability to crossover: ", self.probability_to_crossover)
        print("Block size: ", self.block_size)
        print("Chromosomes to crossover: ", [str(chromosome) for chromosome in chromosomes_to_crossover])
        new_chromosomes = []

        while len(new_chromosomes) < expected_new_population_size:
            idx1, idx2 = random.sample(range(len(chromosomes_to_crossover)), 2)
            parent1, parent2 = chromosomes_to_crossover[idx1], chromosomes_to_crossover[idx2]
            print("Parent 1: ", parent1)
            print("Parent 2: ", parent2)
            if random.random() < self.probability_to_crossover:
                child1_genes = []
                child2_genes = []
                for i in range(0, len(parent1.chromosome_data), self.block_size):
                    if random.random() < self.probability_to_crossover_block:
                        print("Crossover block: ", parent1.chromosome_data[i:i + self.block_size], parent2.chromosome_data[i:i + self.block_size])
                        child1_genes.extend(parent2.chromosome_data[i:i + self.block_size])
                        child2_genes.extend(parent1.chromosome_data[i:i + self.block_size])
                    else:
                        print("No crossover block: ", parent1.chromosome_data[i:i + self.block_size], parent2.chromosome_data[i:i + self.block_size])
                        child1_genes.extend(parent1.chromosome_data[i:i + self.block_size])
                        child2_genes.extend(parent2.chromosome_data[i:i + self.block_size])

                new_child_1_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent1, child1_genes)
                new_child_2_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent2, child2_genes)
                print("Child 1: ", new_child_1_chromosomes)
                print("Child 2: ", new_child_2_chromosomes)
                new_chromosomes.extend([new_child_1_chromosomes, new_child_2_chromosomes])

        new_chromosomes = new_chromosomes[:expected_new_population_size]

        print("Chromosomes after crossover: ", [str(chromosome) for chromosome in new_chromosomes])
        return new_chromosomes