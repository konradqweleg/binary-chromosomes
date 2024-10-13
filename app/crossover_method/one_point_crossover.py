import random

from app.binary_chromosome import BinaryChromosome
from app.crossover_method.crossover_method import CrossoverMethod


class OnePointCrossover(CrossoverMethod):

    def __init__(self, probability_to_crossover):
        self.probability_to_crossover = probability_to_crossover

    def crossover(self, chromosomes_to_crossover):
        print("\n")
        print("Crossover Method: One Point Crossover")
        print("Probability to crossover: ", self.probability_to_crossover)
        print("Chromosomes to crossover: ", [str(chromosome) for chromosome in chromosomes_to_crossover])
        new_chromosomes = []
        crossover_info = []
        crossover_points = []
        for i in range(0, len(chromosomes_to_crossover), 2):
            parent1, parent2 = chromosomes_to_crossover[i], chromosomes_to_crossover[i + 1]
            if random.random() < self.probability_to_crossover:
                if len(parent1.chromosome_data[0]) > 1:
                    point = random.randint(1, len(parent1.chromosome_data[0]) - 1)
                    while point % 2 != 0:
                        point = random.randint(1, len(parent1.chromosome_data[0]) - 1)
                else:
                    point = 1

                child1_chromosomes = parent1.chromosome_data[0][:point] + parent2.chromosome_data[0][point:]
                child2_chromosomes = parent2.chromosome_data[0][:point] + parent1.chromosome_data[0][point:]


                new_child_1_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent1, child1_chromosomes)
                new_child_2_chromosomes = BinaryChromosome.copy_with_new_chromosomes(parent2, child2_chromosomes)
                new_chromosomes.extend([new_child_1_chromosomes, new_child_2_chromosomes])
                crossover_info.extend([f"{str(parent1)}+", f"{str(parent2)}+"])
                crossover_points.append(point)
            else:
                new_chromosomes.extend([parent1, parent2])
                crossover_info.extend([f"{str(parent1)}-", f"{str(parent2)}-"])
                crossover_points.append(None)


        print("Crossover info: ", crossover_info)
        print("Crossover points: ", crossover_points)
        print("Chromosomes after crossover: ", [str(chromosome) for chromosome in new_chromosomes])
        return new_chromosomes