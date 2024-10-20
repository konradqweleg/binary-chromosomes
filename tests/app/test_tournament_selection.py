import unittest

from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator import BitLengthMatchToPrecision
from app.selection.tournament_selection import TournamentSelection


class TestTournamentSelection(unittest.TestCase):
    def setUp(self):
        self.percentage_to_select = 0.5
        self.lower_bounds = 0
        self.upper_bounds = 1
        self.precision = 0.01
        self.bit_length_calculator = BitLengthMatchToPrecision(self.precision, self.lower_bounds, self.upper_bounds, 1)
        self.selection_method = TournamentSelection(self.percentage_to_select,2)
        self.chromosomes = [
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 1, 0, 1, 1, 1]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 1, 1, 0, 0, 0]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [0, 1, 0, 1, 1, 1]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 1, 1, 0, 1, 0]),
        ]

    def test_selection_expected_size(self):
        fitness_scores = [-1, 5, -3, -4]
        new_chromosomes = self.selection_method.select(self.chromosomes, fitness_scores)

        self.assertEqual(2, len(new_chromosomes))
        self.assertIsInstance(new_chromosomes[0], BinaryChromosome)
        self.assertIsInstance(new_chromosomes[1], BinaryChromosome)


    def test_selection_for_minimization(self):
        self.selection_method = TournamentSelection(self.percentage_to_select,2)
        fitness_scores = [0, 1, -1, -2]
        selection_counts = {0: 0, 1: 0, 2: 0, 3: 0}

        for _ in range(1000):
            selected_chromosomes = self.selection_method.select(self.chromosomes, fitness_scores)
            for chromosome in selected_chromosomes:
                index = self.chromosomes.index(chromosome)
                selection_counts[index] += 1

        print("Selection counts: ", selection_counts)
        print("Counts with chromosome 1 info: ", selection_counts[0],str(self.chromosomes[0]))
        print("Counts with chromosome 2 info: ", selection_counts[1],str(self.chromosomes[1]))
        print("Counts with chromosome 3 info: ", selection_counts[2],str(self.chromosomes[2]))
        print("Counts with chromosome 4 info: ", selection_counts[3],str(self.chromosomes[3]))
        self.assertGreater(selection_counts[2], selection_counts[0])
        self.assertGreater(selection_counts[3], selection_counts[0])
        self.assertGreater(selection_counts[2], selection_counts[1])
        self.assertGreater(selection_counts[3], selection_counts[1])