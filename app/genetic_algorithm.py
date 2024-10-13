import random
import copy

from app.bit_length_calculator import BitLengthMatchToPrecision
from app.crossover_method.one_point_crossover import OnePointCrossover
from app.mutation.boundary_mutation import BoundaryMutation
from app.population import Population
from app.selection.best_selection import BestSelection

# UWAGA RANDOM SEED USTAWIONY NA 42 w klasie generujacej chromosomy i tej klasie
class GeneticAlgorithm:
    def __init__(self,length_chromosome_calculator, population_size, lower_bounds, upper_bounds, num_iterations, selection_method,
                 crossover_method, mutation_method, num_variables, elitism_rate,fittness_function=None):
        self.population_size = population_size
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.num_iterations = num_iterations
        self.selection_method = selection_method
        self.crossover_method = crossover_method
        self.num_variables = num_variables
        self.mutation_method = mutation_method
        self.fitness_function = fittness_function
        self.population = Population(length_chromosome_calculator,population_size, lower_bounds, upper_bounds, num_variables)
        self.elitism_rate = elitism_rate
        random.seed(42)

    def fitness_function(self, variables):
        return self.fitness_function(variables)

    def select(self, fitness_scores):
        return self.selection_method.select(self.population.get_chromosomes(), fitness_scores)

    def crossover(self, chromosomes_to_crossover):
        return self.crossover_method.crossover(chromosomes_to_crossover)

    def mutate(self, chromosomes_to_mutate):
        return self.mutation_method.mutate(chromosomes_to_mutate)

    def handle_elites(self, fitness_scores):
        num_elites = int(self.elitism_rate * self.population_size)
        elite_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i])[:num_elites]
        elites = [self.population._chromosomes[i] for i in elite_indices]
        print("Elites:", [str(chromosome) for chromosome in elites])
        return elites

    def update_best_chromosome(self, fitness_scores):
        for i, score in enumerate(fitness_scores):
            if score < self.best_fitness:
                self.best_fitness = score
                self.best_chromosome = copy.deepcopy(self.population._chromosomes[i])

    def run(self):
        for iteration in range(self.num_iterations):
            print(f"\nIteration {iteration + 1}/{self.num_iterations}")

            fitness_scores = self.population.evaluate(self.fitness_function)
            print("Fitness scores for the population:", fitness_scores)
            print("Decoded values:", [chromosome.decode() for chromosome in self.population._chromosomes])

            self.update_best_chromosome(fitness_scores)

            new_population = self.handle_elites(fitness_scores)

            chromosomes_to_crossover = self.select(fitness_scores)
            self.population._chromosomes = [chromosome for chromosome in self.population._chromosomes if
                                            chromosome not in chromosomes_to_crossover]

            crossovered_chromosomes = self.crossover(chromosomes_to_crossover)
            self.population._chromosomes.extend(crossovered_chromosomes)


            mutated_chromosomes = self.mutate(self.population._chromosomes)
            self.population._chromosomes = mutated_chromosomes

            new_population.extend(self.population._chromosomes[:self.population_size - len(new_population)])
            self.population._chromosomes = new_population

        print("\nBest result after iterations:")
        print("Fitness function:", self.best_fitness)
        print("Best chromosome:", self.best_chromosome)
        print("Decoded values of the best chromosome:", self.best_chromosome.decode())
        print(self.fitness_function(self.best_chromosome.decode()))


if __name__ == '__main__':
    lower_bounds = [-10]
    upper_bounds = [10]
    precision = 0.000001
    population_size = 10
    num_iterations = 100
    selection_method = BestSelection(0.20)
    crossover_method = OnePointCrossover(
        0.99)
    crossover_probability = 1.0
    tournament_size = 3

    def fitness_function(variables):
        return sum([x * x + 5 for x in variables])

    chromosome_length_calculator = BitLengthMatchToPrecision(precision, lower_bounds, upper_bounds, 1)

    ga = GeneticAlgorithm(chromosome_length_calculator,population_size, lower_bounds, upper_bounds, precision, num_iterations, selection_method,
                          crossover_method, BoundaryMutation(0.1), crossover_probability, tournament_size,fitness_function)
    ga.run()