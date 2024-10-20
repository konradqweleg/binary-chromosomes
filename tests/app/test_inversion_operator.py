import unittest
import random

from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator import BitLengthMatchToPrecision
from app.other_operations.inversion_operator import InversionOperator


class TestInversionMutation(unittest.TestCase):

    def setUp(self):
        self.lower_bounds = 0
        self.upper_bounds = 1
        self.precision = 0.1
        self.bit_length_calculator = BitLengthMatchToPrecision(self.precision, self.lower_bounds, self.upper_bounds, 1)


        self.chromosomes = [
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1,
                             [random.randint(0, 1) for _ in range(100)])
            for _ in range(1000)
        ]

        self.mutation = InversionOperator(0.5)

    def test_inversion_occurs(self):
        mutated_count = 0
        unchanged_count = 0

        new_chromosomes = self.mutation.apply(self.chromosomes)
        how_many_bit_differences = 0

        for original, mutated in zip(self.chromosomes, new_chromosomes):
            bit_differences = sum(
                1 for o_bit, m_bit in zip(original.chromosome_data, mutated.chromosome_data) if o_bit != m_bit)


            if bit_differences > 0:
                mutated_count += 1
                original_part = original.chromosome_data
                mutated_part = mutated.chromosome_data
                print(f"original_part: {original_part}, mutated_part: {mutated_part}")


                start = next(i for i in range(len(original_part)) if original_part[i] != mutated_part[i])
                end = next(i for i in range(len(original_part) - 1, -1, -1) if original_part[i] != mutated_part[i])


                original_segment = original_part[start:end + 1]
                mutated_segment = mutated_part[start:end + 1]

                if original_segment != list(reversed(mutated_segment)):
                    self.fail(f"Inversion does not match inversion logic: {original_part} -> {mutated_part}")


            elif bit_differences == 0:
                unchanged_count += 1
            else:
                self.fail(f"Unexpected number of bits mutated: {bit_differences} in chromosome: {original.chromosome_data} -> {mutated.chromosome_data}")


        print(f"how_many_bit_differences: {how_many_bit_differences}")
        self.assertAlmostEqual(mutated_count / 1000, 0.5, delta=0.1)
        self.assertAlmostEqual(unchanged_count / 1000, 0.5, delta=0.1)

    def test_no_mutation_if_probability_zero(self):

        no_mutation = InversionOperator(0.0)
        new_chromosomes = no_mutation.apply(self.chromosomes)


        for original, mutated in zip(self.chromosomes, new_chromosomes):
            self.assertEqual(original.chromosome_data, mutated.chromosome_data)

    def test_all_mutations_if_probability_one(self):
        full_mutation = InversionOperator(1.0)
        new_chromosomes = full_mutation.apply(self.chromosomes)

        mutated_count = 0

        for original, mutated in zip(self.chromosomes, new_chromosomes):
            bit_differences = sum(
                1 for o_bit, m_bit in zip(original.chromosome_data, mutated.chromosome_data) if o_bit != m_bit
            )

            if bit_differences > 0:
                mutated_count += 1


        percentage_mutated = mutated_count / len(self.chromosomes)
        print(f"percentage_mutated: {percentage_mutated}")
        self.assertGreaterEqual(percentage_mutated, 0.85,
                                f"Only {percentage_mutated * 100:.2f}% of chromosomes were mutated.")


if __name__ == '__main__':
    unittest.main()
