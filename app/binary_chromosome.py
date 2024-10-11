import random
from app.bit_length_calculator.bit_length_match_to_precision import BitLengthMatchToPrecision


def _calculate_max_values_for_variables(bit_lengths):
    """
    Oblicza maksymalne wartości dla każdej zmiennej.
    """
    return [(2 ** bit_len) - 1 for bit_len in bit_lengths]


class BinaryChromosome:

    def __init__(self, bit_length_calculator, lower_bounds, upper_bounds, precision, num_variables, chromosomes=None):
        """
        Inicjalizacja chromosomu binarnego dla wielu zmiennych.
        bit_length_calculator: obiekt obliczający minimalną liczbę bitów dla danej precyzji
        lower_bounds: lista dolnych granic dla każdej zmiennej
        upper_bounds: lista górnych granic dla każdej zmiennej
        precision: pożądana precyzja (taka sama dla wszystkich zmiennych)
        num_variables: określa ilu zmiennych jest funkcja
        chromosomes: opcjonalnie, lista chromosomów do skopiowania
        """
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.precision = precision
        self.num_variables = num_variables
        self.bit_length_calculator = bit_length_calculator

        self.bit_lengths = [self._calculate_bit_length(lb, ub, self.precision) for lb, ub in zip(lower_bounds, upper_bounds)]
        self.max_values = _calculate_max_values_for_variables(self.bit_lengths)

        if chromosomes is None:
            self.chromosomes = [self._random_chromosome(bit_len) for bit_len in self.bit_lengths]
        else:
            self.chromosomes = chromosomes

    def _calculate_bit_length(self, lower_bound, upper_bound, precision):
        """
        Oblicza minimalną liczbę bitów wymaganą do osiągnięcia danej precyzji dla jednej zmiennej.
        """
        bits_calculator = BitLengthMatchToPrecision()
        bits_calculator.set_precision(precision)
        bits_calculator.set_bounds(lower_bound, upper_bound)

        return bits_calculator.calculate_bit_length()

    def _random_chromosome(self, bit_length):
        """
        Generuje losowy chromosom (lista bitów) o zadanej długości bitowej.
        """
        return [random.choice([0, 1]) for _ in range(bit_length)]

    def decode(self):
        """
        Przekształca chromosom binarny na zestaw wartości rzeczywistych (dla każdej zmiennej).
        """
        real_values = []
        for i in range(self.num_variables):

            binary_str = ''.join(str(bit) for bit in self.chromosomes[i])
            decimal_value = int(binary_str, 2)

            real_value = self.lower_bounds[i] + (decimal_value / self.max_values[i]) * (
                    self.upper_bounds[i] - self.lower_bounds[i])

            real_values.append(real_value)

        return real_values

    def encode(self, real_values):
        """
        Koduje zestaw wartości rzeczywistych (dla każdej zmiennej) do postaci binarnej.
        """
        for i in range(self.num_variables):
            real_value = real_values[i]

            decimal_value = int(
                ((real_value - self.lower_bounds[i]) / (self.upper_bounds[i] - self.lower_bounds[i])) * self.max_values[
                    i])

            binary_str = format(decimal_value, f'0{self.bit_lengths[i]}b')
            self.chromosomes[i] = [int(bit) for bit in binary_str]

    def mutate(self, mutation_rate):
        """
        Mutacja chromosomu z podanym prawdopodobieństwem mutacji (mutation_rate).
        """
        for i in range(self.num_variables):
            for j in range(self.bit_lengths[i]):
                if random.random() < mutation_rate:
                    # Inwersja bitu
                    self.chromosomes[i][j] = 1 - self.chromosomes[i][j]

    def __str__(self):
        """
        Reprezentacja chromosomu jako ciąg bitów (dla każdej zmiennej).
        """
        return ' | '.join(''.join(map(str, chromosome)) for chromosome in self.chromosomes)

    @classmethod
    def copy_with_new_chromosomes(cls, other, new_chromosomes):
        """
        Tworzy kopię chromosomu z nowymi wartościami w chromosomes.
        """
        return cls(other.bit_length_calculator, other.lower_bounds, other.upper_bounds, other.precision, other.num_variables, new_chromosomes)