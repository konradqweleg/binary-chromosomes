import random
import math
from app.bit_length_calculator.bit_length_match_to_precision import BitLengthMatchToPrecision


def _calculate_max_values_for_variables(bit_lengths):
    """
    Oblicza maksymalne wartości dla każdej zmiennej.
    """
    return [(2 ** bit_len) - 1 for bit_len in bit_lengths]


class BinaryChromosome:

    def __init__(self, bit_length_calculator, lower_bounds, upper_bounds, precision, num_variables):
        """
        Inicjalizacja chromosomu binarnego dla wielu zmiennych.
        bit_length_calculator: obiekt obliczający minimalną liczbę bitów dla danej precyzji
        lower_bounds: lista dolnych granic dla każdej zmiennej
        upper_bounds: lista górnych granic dla każdej zmiennej
        precision: pożądana precyzja (taka sama dla wszystkich zmiennych)
        num_variables: określa ilu zmiennych jest funkcja
        """
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.precision = precision
        self.num_variables = num_variables
        self.bit_length_calculator = bit_length_calculator

        self.bit_lengths = [self._calculate_bit_length(lb, ub, self.precision) for lb, ub in zip(lower_bounds, upper_bounds)]
        self.max_values = _calculate_max_values_for_variables(self.bit_lengths)

        self.chromosomes = [self._random_chromosome(bit_len) for bit_len in self.bit_lengths]

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


class Population:
    def __init__(self, population_size, lower_bounds, upper_bounds, precision):
        """
        Inicjalizacja populacji chromosomów dla wielu zmiennych.

        population_size: liczba chromosomów w populacji
        lower_bounds: lista dolnych granic dla każdej zmiennej
        upper_bounds: lista górnych granic dla każdej zmiennej
        precision: pożądana precyzja dla chromosomów
        """
        self.population_size = population_size
        self.chromosomes = [
            BinaryChromosome(BitLengthMatchToPrecision(),lower_bounds, upper_bounds, precision, 1) for _ in range(population_size)
        ]

    def evaluate(self, fitness_function):
        """
        Ocena populacji na podstawie podanej funkcji celu (fitness_function).
        Zwraca listę ocen dla każdego chromosomu.
        """
        result = [fitness_function(chromosome.decode()) for chromosome in self.chromosomes]
        return result

    def __str__(self):
        """
        Reprezentacja populacji chromosomów.
        """
        return '\n'.join([str(chromosome) for chromosome in self.chromosomes])


def fitness_function(variables):
    print("aa" + str(variables) + str(sum([x * x + 5 for x in variables])))

    # return 10 * len(variables) + sum([x**2 - 10 * math.cos(2 * math.pi * x) for x in variables])
    # return  sum([x*x + 5 for x in variables])
    return sum([x * x + 5 for x in variables])


#

# lower_bounds = [-10]  # Dolne granice dla dwóch zmiennych
# upper_bounds = [10]    # Górne granice dla dwóch zmiennych
# precision = 0.000001  # Dokładność do czterech miejsc po przecinku
#

# chromosome = BinaryChromosome(lower_bounds, upper_bounds, precision,1)
# print("Chromosom:", chromosome)
# print("Zdekodowane wartości:", chromosome.decode())
#

# population_size = 5  # Liczba chromosomów w populacji
# population = Population(population_size, lower_bounds, upper_bounds, precision)
# print("\nPopulacja chromosomów:")
# print(population)
#

# fitness_scores = population.evaluate(fitness_function)
# print("\nOceny funkcji celu dla populacji:")
# print(fitness_scores)
#

# chromosome.mutate(mutation_rate=0.1)
# print("\nChromosom po mutacji:", chromosome)
lower_bounds = [-10]
upper_bounds = [10]
precision = 0.000001

random.seed(42)

chromosome = BinaryChromosome(BitLengthMatchToPrecision(),lower_bounds, upper_bounds, precision, 1)
print("Początkowy chromosom:", chromosome)
print("Zdekodowane wartości:", chromosome.decode())

population_size = 5
population = Population(population_size, lower_bounds, upper_bounds, precision)
print("\nPoczątkowa populacja chromosomów:")
print(population)

num_iterations = 100

best_fitness = float('inf')
best_chromosome = None
import copy

for iteration in range(num_iterations):
    print(f"\nIteracja {iteration + 1}/{num_iterations}")

    # Ocena populacji
    fitness_scores = population.evaluate(fitness_function)
    print("Oceny funkcji celu dla populacji:", fitness_scores)
    print("Wartośći zdekodowane:", [chromosome.decode() for chromosome in population.chromosomes])

    for i, score in enumerate(fitness_scores):
        if score < best_fitness:
            print("Znaleziono lepszy wynik:", score)
            print("Zdekodowane wartości:->", population.chromosomes[i].decode())
            best_fitness = score
            best_chromosome = copy.deepcopy(population.chromosomes[i])

    # Krzyżowanie z % szans
    for chromo in population.chromosomes:
        chromo.mutate(mutation_rate=0.05)
        print("Zdekodowane wartości:", chromo.decode())

    print("Populacja po mutacji:")
    print(population)

print("\nNajlepszy wynik po iteracjach:")
print("Funkcja celu:", best_fitness)
print("Najlepszy chromosom:", best_chromosome)
print("Zdekodowane wartości najlepszego chromosomu:", best_chromosome.decode())
print(fitness_function(best_chromosome.decode()))

res = -10 + (1647962) * (20) / (pow(2, 25) - 1)
print(res)
