from abc import ABC, abstractmethod


class CrossoverMethod(ABC):
    @abstractmethod
    def crossover(self, chromosome_to_crossover, expected_new_population_size):
        """
                Performs crossover between chromosomes.

                Parameters:
                chromosome_to_crossover (list): List of chromosomes to crossover.
                expected_new_population_size (int): Expected size of the new population.
                Returns:
                list: Crossed-over elements
        """
        pass
