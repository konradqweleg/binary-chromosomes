import unittest
from app.bit_length_calculator import BitLengthMatchToPrecision
from app.population import Population
from app.selection.best_selection import BestSelection


def fitness_function(variables):
    return sum([x * x + 5 for x in variables])


class TestBestSelection(unittest.TestCase):

    def setUp(self):
        self.lower_bounds = -10
        self.upper_bounds = 10
        self.precision = 0.000001
        self.population_size = 5
        self.num_variables = 1

        self.bit_length_calculator = BitLengthMatchToPrecision(self.precision, self.lower_bounds, self.upper_bounds,
                                                               self.num_variables)
        self.population = Population(self.bit_length_calculator, self.population_size, self.lower_bounds,
                                     self.upper_bounds, self.num_variables)
        self.selection_algorithm = BestSelection(0.4)

    def test_select(self):
        chromosomes = self.population.get_chromosomes()
        fitness_scores = self.population.evaluate(fitness_function)
        selected_chromosomes = self.selection_algorithm.select(chromosomes, fitness_scores)

        self.assertEqual(len(selected_chromosomes), int(self.population_size * 0.4))
        for chromosome in selected_chromosomes:
            self.assertIn(chromosome, chromosomes)

    def test_is_selected_the_bests_chromosomes(self):
        chromosomes = self.population.get_chromosomes()
        fitness_scores = self.population.evaluate(fitness_function)
        selected_chromosomes = self.selection_algorithm.select(chromosomes, fitness_scores, optimization_type='minimization')

        number_of_best_chromosomes = int(len(chromosomes) * 0.4)

        best_chromosomes = sorted(chromosomes, key=lambda x: fitness_function(x.decode()))[:number_of_best_chromosomes]

        for best_chromosome in best_chromosomes:
            self.assertIn(best_chromosome, selected_chromosomes, )


if __name__ == '__main__':
    unittest.main()
