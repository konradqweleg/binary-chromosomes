# from app.bit_length_calculator import BitLengthMatchToPrecision
# from app.crossover_method.one_point_crossover import OnePointCrossover
# from app.mutation.bit_flip_mutation import BitFlipMutation
# from app.population import Population
# from app.selection.best_selection import BestSelection
#
#
#
# def fitness_function(variables):
#     return sum([x * x + 5 for x in variables])
#
# lower_bounds = -10
# upper_bounds = 10
# precision = 0.000001
# population_size = 20
# num_variables = 1
#
# bit_length_calculator = BitLengthMatchToPrecision(precision, lower_bounds, upper_bounds, num_variables)
# population = Population(bit_length_calculator, population_size, lower_bounds, upper_bounds, num_variables)
#
# # selecttion_algorithm = BestSelection(0.50)
# # selected_chromosomes = selecttion_algorithm.select(population.get_chromosomes(), population.evaluate(fitness_function))
# # print(str(selected_chromosomes[0]))
#
# # cross_algorithm = OnePointCrossover(0.5)
# # print(cross_algorithm.crossover(selected_chromosomes, population_size))
#
# mutation = BitFlipMutation(0.1)
# result = mutation.mutate(population.get_chromosomes())
#
# print(population.get_chromosomes()[0].chromosome_data)
# print(result[0].chromosome_data)
#
#
# print(population.get_chromosomes()[1].chromosome_data)
# print(result[1].chromosome_data)
#
#
# print(population.get_chromosomes()[2].chromosome_data)
# print(result[2].chromosome_data)

import benchmark_functions as bf

func = bf.Schwefel(n_dimensions=2)

for x  in func.minima():
    print(x)
print(func.suggested_bounds())


func2 = bf.Griewank(n_dimensions=2)
for x  in func2.minima():
    print(x)
print(func2.suggested_bounds())