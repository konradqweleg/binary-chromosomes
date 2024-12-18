import math
import copy

import numpy as np

from app.bit_length_calculator import BitLengthMatchToPrecision
from app.crossover_method.granular_crossover import GranularCrossover
from app.crossover_method.one_point_crossover import OnePointCrossover
from app.crossover_method.three_point_crossover import ThreePointCrossover
from app.crossover_method.two_point_crossover import TwoPointCrossover
from app.crossover_method.uniform_crossover import UniformCrossover
from app.functions.cec_2014_f1 import Cec2014F1
from app.functions.griewank import Griewank
from app.functions.szwefel import Szwefel
from app.functions.szwefel_custom_impl import SzwefelCustomImpl
from app.mutation.bit_flip_mutation import BitFlipMutation
from app.other_operations.inversion_operator import InversionOperator
from app.population import Population
from app.selection.best_selection import BestSelection
import logging
import matplotlib.pyplot as plt
import time

def setup_logger(log_level=logging.INFO):
    with open('app.log', 'w'):
        pass
    logger = logging.getLogger()
    logger.setLevel(log_level)

    file_handler = logging.FileHandler('app.log')
    console_handler = logging.StreamHandler()

    file_handler.setLevel(log_level)
    console_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def set_log_level(log_level):
    logger = logging.getLogger()
    logger.setLevel(log_level)
    for handler in logger.handlers:
        handler.setLevel(log_level)


setup_logger()
set_log_level(logging.INFO)


# set_log_level(logging.DEBUG)
# UWAGA RANDOM SEED USTAWIONY NA 42 w klasie generujacej chromosomy i tej klasie
class GeneticAlgorithm:
    def __init__(self, length_chromosome_calculator, population_size, lower_bounds, upper_bounds, num_iterations,
                 selection_method,
                 crossover_method, mutation_method, num_variables, elitism_rate, other_operation=None,
                 fittness_function=None, optimization_type='maximization'):

        self.logger = logging.getLogger(__name__)

        self.logger.info("Selected parameters:")
        self.logger.info(f"Population size: {population_size}")
        self.logger.info(f"Lower bounds: {lower_bounds}")
        self.logger.info(f"Upper bounds: {upper_bounds}")
        self.logger.info(f"Number of iterations: {num_iterations}")
        self.logger.info(f"Selection method: {selection_method}")
        self.logger.info(f"Crossover method: {crossover_method}")
        self.logger.info(f"Mutation method: {mutation_method}")
        self.logger.info(f"Number of variables: {num_variables}")
        self.logger.info(f"Elitism rate: {elitism_rate}")
        self.logger.info(f"Other operations: {other_operation}")
        self.logger.info(f"Optimization type: {optimization_type}")

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

        self.best_chromosome = float('inf') if optimization_type == 'minimization' else float('-inf')
        self.best_fitness = float('inf') if optimization_type == 'minimization' else float('-inf')
        self.the_best_chromosome_last_population = None
        self.the_best_fitness_last_population = float('inf') if optimization_type == 'minimization' else float('-inf')


        self.other_operations = other_operation
        self.optimization_type = optimization_type
        self.logger = logging.getLogger(__name__)

    def fitness_function(self, variables):
        self.logger.debug(f"Calculating fitness function for variables: {variables}")
        return self.fitness_function(variables)

    def select(self, fitness_scores):
        self.logger.debug(f"Selecting chromosomes with fitness scores: {fitness_scores}")
        return self.selection_method.select(self.population.get_chromosomes(), fitness_scores, self.optimization_type)

    def crossover(self, chromosomes_to_crossover):
        self.logger.debug(f"Crossovering chromosomes: {chromosomes_to_crossover}")
        population_size_minus_elites = self.population_size - int(self.elitism_rate * self.population_size)
        return self.crossover_method.crossover(chromosomes_to_crossover, population_size_minus_elites)

    def mutate(self, chromosomes_to_mutate):
        self.logger.debug(f"Mutating chromosomes: {chromosomes_to_mutate}")
        return self.mutation_method.mutate(chromosomes_to_mutate)

    def handle_elites(self, fitness_scores):
        self.logger.debug(f"Handling elites for fitness scores: {fitness_scores}")
        num_elites = int(self.elitism_rate * self.population_size)

        if self.optimization_type == 'maximization':
            elite_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i], reverse=True)[
                            :num_elites]
        else:  # minimization
            elite_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i])[:num_elites]

        elites = [self.population.chromosomes[i] for i in elite_indices]
        return elites

    def update_best_chromosome(self, fitness_scores):
        for i, score in enumerate(fitness_scores):
            if (self.optimization_type == 'minimization' and score < self.best_fitness) or \
                    (self.optimization_type == 'maximization' and score > self.best_fitness):
                self.logger.debug(f"Updating best chromosome with score: {score}")
                self.best_fitness = score
                self.best_chromosome = copy.deepcopy(self.population._chromosomes[i])

    def find_best_chromosome_in_last_iteration(self, fitness_scores):
        for i, score in enumerate(fitness_scores):
            if (self.optimization_type == 'minimization' and score < self.the_best_fitness_last_population) or \
                    (self.optimization_type == 'maximization' and score > self.the_best_fitness_last_population):
                self.logger.debug(f"Updating best chromosome in last population with score: {score}")
                self.the_best_fitness_last_population = score
                self.the_best_chromosome_last_population = copy.deepcopy(self.population._chromosomes[i])

    def run(self):
        start_time = time.time()
        value_function_on_iteration = []
        avg_fitness_on_iteration = []
        std_dev_fitness_on_iteration = []
        value_fitness_function_on_iteration = []
        for iteration in range(self.num_iterations):
            if iteration % 100 == 0 or iteration == self.num_iterations - 1:
                self.logger.info(f"Iteration {iteration + 1}/{self.num_iterations}")

            fitness_scores = self.population.evaluate(self.fitness_function)
            if iteration % 100 == 0 or iteration == self.num_iterations - 1:
                self.logger.info(f"Fitness scores for the population: {fitness_scores}")
            self.logger.debug(f"Decoded values: {[chromosome.decode() for chromosome in self.population._chromosomes]}")

            self.update_best_chromosome(fitness_scores)

            elites = self.handle_elites(fitness_scores)
            self.logger.debug(f"Elites: {elites}")

            chromosomes_to_crossover = self.select(fitness_scores)
            self.logger.debug(f"Chromosomes to crossover: {chromosomes_to_crossover}")
            crossovered_chromosomes = self.crossover(chromosomes_to_crossover)
            self.logger.debug(f"Crossovered chromosomes: {crossovered_chromosomes}")

            self.population._chromosomes = crossovered_chromosomes
            self.logger.debug(f"Population after crossover: {self.population._chromosomes}")
            mutated_chromosomes = self.mutate(self.population.get_chromosomes())
            self.logger.debug(f"Mutated chromosomes: {mutated_chromosomes}")

            if self.other_operations is not None:
                mutated_chromosomes = self.other_operations.apply(mutated_chromosomes)
                self.logger.debug(f"Chromosomes after other operations: {mutated_chromosomes}")

            self.population._chromosomes = mutated_chromosomes
            self.logger.debug(f"Population after all: {self.population._chromosomes}")
            self.population._chromosomes.extend(elites)
            self.logger.debug(f"Population after adding elites: {self.population._chromosomes}")
            value_function_on_iteration.append(self.best_fitness)
            value_fitness_function_on_iteration.append(fitness_scores)
            avg_fitness_on_iteration.append(np.mean(fitness_scores))
            std_dev_fitness_on_iteration.append(np.std(fitness_scores))

        self.find_best_chromosome_in_last_iteration(fitness_scores)
        end_time = time.time()
        time_elapsed = end_time - start_time
        self.logger.info(f"Time elapsed: {time_elapsed}")
        self.logger.debug("Best result after iterations:")
        self.logger.debug("Fitness function: %f", self.best_fitness)
        self.logger.debug("Best chromosome: %s", self.best_chromosome)
        self.logger.debug("Decoded values of the best chromosome: %s", self.best_chromosome.decode())
        self.logger.info("Best result in last population:")
        self.logger.info("Fitness function: %f", self.the_best_fitness_last_population)
        self.logger.info("Best chromosome: %s", self.the_best_chromosome_last_population)
        self.logger.info("Decoded values of the best chromosome: %s", self.the_best_chromosome_last_population.decode())
        return value_fitness_function_on_iteration, value_function_on_iteration, avg_fitness_on_iteration, std_dev_fitness_on_iteration, self.the_best_fitness_last_population, self.the_best_chromosome_last_population.decode(),time_elapsed


if __name__ == '__main__':
    conf_lower_bounds = -500.0
    conf_upper_bounds = 500.0
    conf_precision = 0.0001
    conf_population_size = 10
    conf_num_iterations = 10000
    conf_selection_method = BestSelection(0.20)
    conf_tournament_size = 3

    conf_chromosome_length_calculator = BitLengthMatchToPrecision(conf_precision, conf_lower_bounds, conf_upper_bounds,
                                                                  3)
    conf_crossover_method = OnePointCrossover(0.99)
    conf_crossover_method = TwoPointCrossover(0.99)
    conf_crossover_method = ThreePointCrossover(0.99)
    conf_crossover_method = GranularCrossover(0.99, 2, 0.5)
    conf_crossover_method = UniformCrossover(0.50, 0.05)

    conf_inversion_action = InversionOperator(0.01)

    conf_mutation_method = BitFlipMutation(0.01)

    conf_elitism_rate = 0.2

    conf_num_variables = 3


    def fitness_function(variables):
        # return variables[0] * variables[0] + 5
        # return sum([x * x + 5 for x in variables]) # To i to wyżej to to samo
        # return variables[0] * variables[0] * variables[0] - 24 * variables[1] * variables[1] + 180 *variables[2]
        return (variables[0] * variables[0] * variables[0]) - (24 * variables[0] * variables[0]) - (180 * variables[0])


    def test_square_function(variables):
        return sum([x * x for x in variables])
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


szwfFunc = SzwefelCustomImpl()
# szwfFunc = SzwefelCustomImpl()
# szwfFunc = Griewank()
# szwfFunc = Cec2014F1()

# ga = GeneticAlgorithm(conf_chromosome_length_calculator, conf_population_size, conf_lower_bounds, conf_upper_bounds,
#                       conf_num_iterations,
#                       conf_selection_method,
#                       conf_crossover_method, conf_mutation_method, conf_num_variables, conf_elitism_rate,
#                       conf_inversion_action,
#                       szwfFunc, 'minimization') #minimization
# fitness_value, value_function_on_iteration, avg_on_iteration, std_on_iteration, best_fitness, best_chromosome_value,time_calculation = ga.run()
# #print(value_function_on_iteration)
# print(best_fitness)
# print(best_chromosome_value)
# print(time_calculation)


# def draw_function_value_over_iterations(value_function_on_iteration):
#     import matplotlib.pyplot as plt
#     plt.figure(figsize=(10, 6))
#     plt.plot(value_function_on_iteration)
#     plt.xlabel('Iteration')
#     plt.ylabel('Fitness Value')
#     plt.title('Fitness Value Over Iterations')
#     plt.grid(True)
#     plt.savefig('results/fitness_value_over_iterations.png')
#     plt.show()
#
#
# def plot_avg_fitness_over_iteration(avg_fitness_on_iteration):
#     plt.figure(figsize=(10, 6))
#     plt.plot(avg_fitness_on_iteration, label='Average Fitness Value')
#     plt.xlabel('Iteration')
#     plt.ylabel('Fitness Value')
#     plt.title('Average Fitness Value Over Iterations')
#     plt.legend()
#     plt.grid(True)
#     plt.savefig('results/avg_fitness_over_iterations.png')
#     plt.show()
#
#
# def plot_std_dev_fitness_over_iteration(std_dev_fitness_on_iteration):
#     plt.figure(figsize=(10, 6))
#     plt.plot(std_dev_fitness_on_iteration, label='Standard Deviation of Fitness Value')
#     plt.xlabel('Iteration')
#     plt.ylabel('Fitness Value')
#     plt.title('Standard Deviation of Fitness Value Over Iterations')
#     plt.legend()
#     plt.grid(True)
#     plt.savefig('results/std_dev_fitness_over_iterations.png')
#     plt.show()
#
#
# def save_results_to_file(filename, value_function_on_iteration, avg_fitness_on_iteration, std_dev_fitness_on_iteration):
#     with open(filename, 'w') as file:
#         file.write("Iteration,Best Fitness,Average Fitness,Standard Deviation\n")
#         for i in range(len(value_function_on_iteration)):
#             file.write(
#                 f"{i + 1},{value_function_on_iteration[i]},{avg_fitness_on_iteration[i]},{std_dev_fitness_on_iteration[i]}\n")


# save_results_to_file('results/algorithm_results.csv', value_function_on_iteration, avg_on_iteration, std_on_iteration)
# draw_function_value_over_iterations(value_function_on_iteration)
# draw_function_value_over_iterations(fitness_value)
# plot_avg_fitness_over_iteration(avg_on_iteration)
# plot_std_dev_fitness_over_iteration(std_on_iteration)
#
# print(fitness_function_szwefel([118.43]))
