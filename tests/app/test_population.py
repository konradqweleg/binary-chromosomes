import unittest
from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator.bit_length_match_to_precision import BitLengthMatchToPrecision
from app.population import Population


class TestPopulation(unittest.TestCase):

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

    def test_population_initialization(self):
        self.assertEqual(len(self.population.get_chromosomes()), self.population_size)
        for chromosome in self.population.get_chromosomes():
            self.assertIsInstance(chromosome, BinaryChromosome)

    def test_length_of_population(self):
        self.assertEqual(len(self.population.get_chromosomes()), self.population_size)

    def test_evaluate(self):
        def dummy_fitness_function(decoded_values):
            return sum(decoded_values)

        evaluations = self.population.evaluate(dummy_fitness_function)
        self.assertEqual(len(evaluations), self.population_size)
        for evaluation in evaluations:
            self.assertIsInstance(evaluation, float)

    def test_str(self):
        population_str = str(self.population)
        self.assertTrue(isinstance(population_str, str))
        self.assertTrue(population_str.startswith("Chromosom:"))


if __name__ == '__main__':
    unittest.main()
