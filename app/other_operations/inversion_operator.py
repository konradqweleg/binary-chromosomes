import random
from app.binary_chromosome import BinaryChromosome
from app.other_operations.operation import Operation


class InversionOperator(Operation):

    def __init__(self, probability_to_inversion):
        self.probability_to_mutate = probability_to_inversion



    def apply(self, chromosomes_to_mutate):
        new_chromosomes = []
        for chromosome in chromosomes_to_mutate:
            new_gens_for_chromosome = list(chromosome.chromosome_data)
            print("chromosome: ", chromosome.chromosome_data)

            if random.random() < self.probability_to_mutate:

                point1 = random.randint(0, len(new_gens_for_chromosome) - 2)
                point2 = random.randint(point1 + 1, len(new_gens_for_chromosome) - 1)

                print(f"point1: {point1}, point2: {point2}")
                print("left subarray: ", new_gens_for_chromosome[point1:point2+1])
                print("right subarray: ", new_gens_for_chromosome[point1:point2 + 1])
                print("right subarray after mutation: ", new_gens_for_chromosome[point2 + 1:])

                # Odwracamy fragment pomiędzy point1 a point2
                new_gens_for_chromosome[point1:point2 + 1] = reversed(new_gens_for_chromosome[point1:point2 + 1])
                print(f"new_gens_for_chromosome: {new_gens_for_chromosome} vs {chromosome.chromosome_data}")

            new_chromosomes.append(BinaryChromosome.copy_with_new_chromosomes(chromosome, new_gens_for_chromosome))

        return new_chromosomes

