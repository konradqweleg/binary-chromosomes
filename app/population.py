from app.binary_chromosome import BinaryChromosome


class Population:
    def __init__(self, binary_length_calculator, population_size, lower_bounds, upper_bounds, num_variables):
        """
        Inicjalizacja populacji chromosomów dla wielu zmiennych.

        population_size: liczba chromosomów w populacji
        lower_bounds: dolna granica dla każdej zmiennej
        upper_bounds: górna granica dla każdej zmiennej
        """
        self.population_size = population_size
        self._chromosomes = [
            BinaryChromosome(binary_length_calculator, lower_bounds, upper_bounds, num_variables) for _ in
            range(population_size)
        ]

    def get_chromosomes(self):
        """
        Zwraca listę chromosomów w populacji.
        """
        return self._chromosomes

    def evaluate(self, fitness_function):
        """
        Ocena populacji na podstawie podanej funkcji celu (fitness_function).
        Zwraca listę ocen dla każdego chromosomu.
        """
        result = [fitness_function(chromosome.decode()) for chromosome in self._chromosomes]
        return result

    def __str__(self):
        """
        Reprezentacja populacji chromosomów.
        """
        return '\n'.join([str(chromosome) for chromosome in self._chromosomes])
