from abc import ABC, abstractmethod


class CrossoverMethod(ABC):
    @abstractmethod
    def crossover(self, chromosome_to_crossover, expected_new_population_size):
        """
                Wykonuje krzyżowanie między chromosomami.

                Parametry:
                chromosome_to_crossover (list): Lista chromosomów do skrzyżowania.


                Zwraca:
                list: skrzyzowane elementy
        """
        pass
