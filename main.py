from app.bit_length_calculator import BitLengthMatchToPrecision
from app.population import Population
from app.selection.best_selection import BestSelection


def fitness_function(variables):
    return sum([x * x + 5 for x in variables])

lower_bounds = -10
upper_bounds = 10
precision = 0.000001
population_size = 5
num_variables = 1

bit_length_calculator = BitLengthMatchToPrecision(precision, lower_bounds, upper_bounds, num_variables)
population = Population(bit_length_calculator, population_size, lower_bounds, upper_bounds, num_variables)
        
        
selecttion_algorithm = BestSelection(0.4)
selected_chromosomes = selecttion_algorithm.select(population.get_chromosomes(), population.evaluate(fitness_function))
print(str(selected_chromosomes[0]))