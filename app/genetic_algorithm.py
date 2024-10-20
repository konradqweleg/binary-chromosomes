import math
import random
import copy

from app.bit_length_calculator import BitLengthMatchToPrecision
from app.crossover_method.granular_crossover import GranularCrossover
from app.crossover_method.one_point_crossover import OnePointCrossover
from app.crossover_method.three_point_crossover import ThreePointCrossover
from app.crossover_method.two_point_crossover import TwoPointCrossover
from app.crossover_method.uniform_crossover import UniformCrossover
from app.mutation.boundary_mutation import BoundaryMutation
from app.mutation.bit_flip_mutation import BitFlipMutation
from app.population import Population
from app.selection.best_selection import BestSelection


# UWAGA RANDOM SEED USTAWIONY NA 42 w klasie generujacej chromosomy i tej klasie
class GeneticAlgorithm:
    def __init__(self, length_chromosome_calculator, population_size, lower_bounds, upper_bounds, num_iterations,
                 selection_method,
                 crossover_method, mutation_method, num_variables, elitism_rate, fittness_function=None):
        self.population_size = population_size
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.num_iterations = num_iterations
        self.selection_method = selection_method
        self.crossover_method = crossover_method
        self.num_variables = num_variables
        self.mutation_method = mutation_method
        self.fitness_function = fittness_function
        self.population = Population(length_chromosome_calculator, population_size, lower_bounds, upper_bounds,
                                     num_variables)
        self.elitism_rate = elitism_rate

        self.best_chromosome = float('inf')
        self.best_fitness = float('inf')

        self.the_best_chromosome_last_population = None
        self.the_best_fitness_last_population = float('inf')
      #  random.seed(42)

    def fitness_function(self, variables):
        return self.fitness_function(variables)

    def select(self, fitness_scores):
        return self.selection_method.select(self.population.get_chromosomes(), fitness_scores)

    def crossover(self, chromosomes_to_crossover):
        population_size_minus_elites = self.population_size - int(self.elitism_rate * self.population_size)
        return self.crossover_method.crossover(chromosomes_to_crossover, population_size_minus_elites)

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

    def find_best_chromosome_in_last_iteration(self,fittness_scores):
        for i, score in enumerate(fittness_scores):
            if score < self.the_best_fitness_last_population:
                self.the_best_fitness_last_population = score
                self.the_best_chromosome_last_population = copy.deepcopy(self.population._chromosomes[i])
    def run(self):
        for iteration in range(self.num_iterations):
            print(f"\nIteration {iteration + 1}/{self.num_iterations}")

            fitness_scores = self.population.evaluate(self.fitness_function)
            print("Fitness scores for the population:", fitness_scores)
            print("Decoded values:", [chromosome.decode() for chromosome in self.population._chromosomes])

            self.update_best_chromosome(fitness_scores)

            elites = self.handle_elites(fitness_scores)

            chromosomes_to_crossover = self.select(fitness_scores)

            crossovered_chromosomes = self.crossover(chromosomes_to_crossover)
            print("Crossovered chromosomes:", [str(chromosome) for chromosome in crossovered_chromosomes])
            self.population._chromosomes = crossovered_chromosomes

            mutated_chromosomes = self.mutate(self.population.get_chromosomes())
            self.population._chromosomes = mutated_chromosomes
            self.population._chromosomes.extend(elites)
            #new_population.extend(self.population._chromosomes[:self.population_size - len(new_population)])
            #self.population._chromosomes = new_population

        self.find_best_chromosome_in_last_iteration(fitness_scores)
        print("\nBest result after iterations:")
        print("Fitness function:", self.best_fitness)
        print("Best chromosome:", self.best_chromosome)
        print("Decoded values of the best chromosome:", self.best_chromosome.decode())
        print("\nBest result in last population:")
        print("Fitness function:", self.the_best_fitness_last_population)
        print("Best chromosome:", self.the_best_chromosome_last_population)


if __name__ == '__main__':
    lower_bounds = -500.0
    upper_bounds = 500.0
    precision = 0.000001
    population_size = 20
    num_iterations = 2000
    selection_method = BestSelection(0.20)

    tournament_size = 3



    def fitness_function(variables):
        #return variables[0] * variables[0] + 5
        #return sum([x * x + 5 for x in variables]) # To i to wyżej to to samo
        #return variables[0] * variables[0] * variables[0] - 24 * variables[1] * variables[1] + 180 *variables[2]
        return (variables[0] * variables[0] * variables[0]) - (24 * variables[0]* variables[0]) - (180 *variables[0])


    def fitness_function_szwefel(variables):

        # Global Minimum:
        # Function Value: 2.545567497236334e-5
        # Coordinates: [420.9687, 420.9687]
        # This means that the global minimum of the Schwefel function is achieved at the point (420.9687, 420.9687)
        # with a function value close to zero, which is the theoretical minimum of the function.

        # Local Minimum:
        # Function Value: 118.43836006957031
        # Coordinates: [-302.5249351839932, 420.9687467475071]

        n = len(variables)  # Liczba wymiarów
        sum_term = 0.0

        for x in variables:
            sum_term += x * math.sin(math.sqrt(abs(x)))

        return 418.9829 * n - sum_term

    chromosome_length_calculator = BitLengthMatchToPrecision(precision, lower_bounds, upper_bounds, 3)

    crossover_method = OnePointCrossover(0.99)
    crossover_method = TwoPointCrossover(0.99)
    crossover_method = ThreePointCrossover(0.99)
    crossover_method = GranularCrossover(0.99, 2, 0.5)
    crossover_method = UniformCrossover(0.99, 0.5)


    ga = GeneticAlgorithm(chromosome_length_calculator, population_size, lower_bounds, upper_bounds, num_iterations,
                          selection_method,
                          crossover_method, BitFlipMutation(0.01), 3, 0.1, fitness_function_szwefel)
    ga.run()


#print(fitness_function_szwefel([118.43]))
