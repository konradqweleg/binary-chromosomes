import random
from app.binary_chromosome import BinaryChromosome
from app.crossover_method.crossover_method import CrossoverMethod

class ThreePointCrossover(CrossoverMethod):

    def __init__(self, probability_to_crossover):
        self.probability_to_crossover = probability_to_crossover

    def crossover(self, chromosomes_to_crossover, expected_new_population_size):
        print("\n")
        print("Crossover Method: Three Point Crossover")
        print("Probability to crossover: ", self.probability_to_crossover)
        print("Chromosomes to crossover: ", [str(chromosome) for chromosome in chromosomes_to_crossover])
        new_chromosomes = []

        while len(new_chromosomes) < expected_new_population_size:
            idx1, idx2 = random.sample(range(len(chromosomes_to_crossover)), 2)
            parent1, parent2 = chromosomes_to_crossover[idx1], chromosomes_to_crossover[idx2]
            if random.random() < self.probability_to_crossover:
                if len(parent1.chromosome_data) > 3:
                    points = sorted(random.sample(range(1, len(parent1.chromosome_data)), 3))
                else:
                    points = [1, len(parent1.chromosome_data) // 2, len(parent1.chromosome_data)]

                print("Points: ", points)
                child1_chromosomes = (parent1.chromosome_data[:points[0]] +
                                      parent2.chromosome_data[points[0]:points[1]] +
                                      parent1.chromosome_data[points[1]:points[2]] +
                                      parent2.chromosome_data[points[2]:])
                child2_chromosomes = (parent2.chromosome_data[:points[0]] +
                                      parent1.chromosome_data[points[0]:points[1]] +
                                      parent2.chromosome_data[points[1]:points[2]] +
                                      parent1.chromosome_data[points[2]:])

                print("Parent 1 chromosomes: ", parent1)
                print("Parent 2 chromosomes: ", parent2)
                print("New child 1 chromosomes: ", child1_chromosomes)
                print("New child 2 chromosomes: ", child2_chromosomes)
                new_child_1_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent1, child1_chromosomes)
                new_child_2_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent2, child2_chromosomes)
                new_chromosomes.extend([new_child_1_chromosomes, new_child_2_chromosomes])


        new_chromosomes = new_chromosomes[:expected_new_population_size]

        print("Chromosomes after crossover: ", [str(chromosome) for chromosome in new_chromosomes])
        return new_chromosomes