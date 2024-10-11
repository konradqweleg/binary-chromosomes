from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator import BitLengthMatchToPrecision



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