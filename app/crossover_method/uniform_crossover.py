import random
from app.binary_chromosome import BinaryChromosome
from app.crossover_method.crossover_method import CrossoverMethod

class UniformCrossover(CrossoverMethod):

    def __init__(self, probability_to_crossover, probability_to_crossover_gene):
        self.probability_to_crossover = probability_to_crossover
        self.probability_to_crossover_gene = probability_to_crossover_gene

    def crossover(self, chromosomes_to_crossover, expected_new_population_size):
        print("\n")
        print("Crossover Method: Uniform Crossover")
        print("Probability to crossover: ", self.probability_to_crossover)
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
                for gene1, gene2 in zip(parent1.chromosome_data, parent2.chromosome_data):
                    if random.random() < self.probability_to_crossover_gene:
                        print("Crossover gene: ", gene1, gene2)
                        child1_genes.append(gene2)
                        child2_genes.append(gene1)
                    else:
                        print("No crossover gene: ", gene1, gene2)
                        child1_genes.append(gene1)
                        child2_genes.append(gene2)

                new_child_1_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent1, child1_genes)
                new_child_2_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent2, child2_genes)
                print("Child 1: ", new_child_1_chromosomes)
                print("Child 2: ", new_child_2_chromosomes)
                new_chromosomes.extend([new_child_1_chromosomes, new_child_2_chromosomes])

        new_chromosomes = new_chromosomes[:expected_new_population_size]

        print("Chromosomes after crossover: ", [str(chromosome) for chromosome in new_chromosomes])
        return new_chromosomes