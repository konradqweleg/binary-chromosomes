import random
import copy

from app.crossover_method.one_point_crossover import OnePointCrossover
from app.mutation.boundary_mutation import BoundaryMutation
from app.population import Population
from app.selection.best_selection import BestSelection


class GeneticAlgorithm:
    def __init__(self, population_size, lower_bounds, upper_bounds, precision, num_iterations, selection_method, crossover_method, mutation_method, crossover_probability=0.7, tournament_size=3, elitism_rate=0.1):
        self.population_size = population_size
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.precision = precision
        self.num_iterations = num_iterations
        self.selection_method = selection_method
        self.crossover_method = crossover_method
        self.crossover_probability = crossover_probability
        self.tournament_size = tournament_size
        self.best_fitness = float('inf')
        self.best_chromosome = None
        self.mutation_method = mutation_method
        self.population = Population(population_size, lower_bounds, upper_bounds, precision)
        self.elitism_rate = elitism_rate
        random.seed(42)

    def fitness_function(self, variables):
        return sum([x * x + 5 for x in variables])

    def select(self, fitness_scores):
        return self.selection_method.select(self.population.chromosomes, fitness_scores)

    def crossover(self, chromosomes_to_crossover):
        if random.random() < self.crossover_probability:
            return self.crossover_method.crossover(chromosomes_to_crossover)
        else:
            return chromosomes_to_crossover

    def mutate(self, chromosomes_to_mutate):
        return self.mutation_method.mutate(chromosomes_to_mutate)

    def run(self):
        for iteration in range(self.num_iterations):
            print(f"\nIteration {iteration + 1}/{self.num_iterations}")

            # Evaluate population
            fitness_scores = self.population.evaluate(self.fitness_function)
            print("Fitness scores for the population:", fitness_scores)
            print("Decoded values:", [chromosome.decode() for chromosome in self.population.chromosomes])

            for i, score in enumerate(fitness_scores):
                if score < self.best_fitness:
                    print("Found a better score:", score)
                    print("Decoded values:->", self.population.chromosomes[i].decode())
                    self.best_fitness = score
                    self.best_chromosome = copy.deepcopy(self.population.chromosomes[i])

            # Select, crossover, and mutate chromosomes
            new_population = []

            # Elitism: carry over the best individuals
            num_elites = int(self.elitism_rate * self.population_size)
            elite_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i])[:num_elites]
            elites = [self.population.chromosomes[i] for i in elite_indices]
            new_population.extend(elites)

            print("Elites:", [str(chromosome) for chromosome in elites])

            # Select the rest of the population
            chromosomes_to_crossover = self.select(fitness_scores)
            self.population.chromosomes = [chromosome for chromosome in self.population.chromosomes if chromosome not in chromosomes_to_crossover]

            print("Chromosomes not to cross", [str(chromosome) for chromosome in self.population.chromosomes])
            print("Chromosomes to crossover:", [str(chromosome) for chromosome in chromosomes_to_crossover])
            crossovered_chromosomes = self.crossover(chromosomes_to_crossover)

            print("Crossovered chromosomes:", [str(chromosome) for chromosome in crossovered_chromosomes])
            self.population.chromosomes.extend(crossovered_chromosomes)
            print("Population after crossover:")
            print(self.population)

            mutated_chromosomes = self.mutate(self.population.chromosomes)
            print("Mutated chromosomes:", mutated_chromosomes)
            print("Mutated chromosomes:", type(mutated_chromosomes))
            for x in mutated_chromosomes:
                print("Decoded values of mutated chromosomes:", x.chromosomes)

            self.population.chromosomes = mutated_chromosomes
            print("Chromosomes 99", [str(chromosome) for chromosome in self.population.chromosomes])

            # Ensure the new population size is correct
            new_population.extend(self.population.chromosomes[:self.population_size - len(new_population)])
            self.population.chromosomes = new_population

        print("\nBest result after iterations:")
        print("Fitness function:", self.best_fitness)
        print("Best chromosome:", self.best_chromosome)
        print("Decoded values of the best chromosome:", self.best_chromosome.decode())
        print(self.fitness_function(self.best_chromosome.decode()))


if __name__ == '__main__':
    lower_bounds = [-10]
    upper_bounds = [10]
    precision = 0.000001
    population_size = 5
    num_iterations = 100
    selection_method = BestSelection(0.40)
    crossover_method = OnePointCrossover(0.30)  # Options: OnePointCrossover, TwoPointCrossover, ThreePointCrossover, UniformCrossover, GranularCrossover
    crossover_probability = 0.7
    tournament_size = 3

    ga = GeneticAlgorithm(population_size, lower_bounds, upper_bounds, precision, num_iterations, selection_method, crossover_method, BoundaryMutation(0.1), crossover_probability, tournament_size)
    ga.run()