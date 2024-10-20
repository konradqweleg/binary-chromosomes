import random
import unittest

from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator import BitLengthMatchToPrecision
from app.crossover_method.uniform_crossover import UniformCrossover


class TestUniformCrossover(unittest.TestCase):

    def setUp(self):
        self.probability_to_crossover = 0.7
        self.probability_to_crossover_gene = 0.5
        self.two_point_crossover = UniformCrossover(self.probability_to_crossover, self.probability_to_crossover_gene)

        self.lower_bounds = 0
        self.upper_bounds = 1
        self.precision = 0.1
        self.bit_length_calculator = BitLengthMatchToPrecision(self.precision, self.lower_bounds, self.upper_bounds, 1)
        self.chromosomes_to_crossover = [
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [0, 1, 0, 1]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 0, 1, 0]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [0, 0, 1, 1]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 1, 0, 0])
        ]
        self.expected_new_population_size = 4


    def test_crossover_expected_size(self):
        new_chromosomes = self.two_point_crossover.crossover(self.chromosomes_to_crossover, self.expected_new_population_size)

        self.assertEqual(len(new_chromosomes), self.expected_new_population_size)
        self.assertIsInstance(new_chromosomes[0], BinaryChromosome)
        self.assertIsInstance(new_chromosomes[1], BinaryChromosome)
        self.assertIsInstance(new_chromosomes[2], BinaryChromosome)
        self.assertIsInstance(new_chromosomes[3], BinaryChromosome)


    def test_crossover(self):
        random.seed(0)
        new_chromosomes = self.two_point_crossover.crossover(self.chromosomes_to_crossover, self.expected_new_population_size)

        self.assertEqual(len(new_chromosomes), self.expected_new_population_size)
        self.assertEqual(new_chromosomes[0].chromosome_data, [1, 0, 0, 0])
        self.assertEqual(new_chromosomes[1].chromosome_data, [1, 1, 1, 0])
        self.assertEqual(new_chromosomes[2].chromosome_data, [1, 1, 1, 0])
        self.assertEqual(new_chromosomes[3].chromosome_data, [1, 0, 0, 0])