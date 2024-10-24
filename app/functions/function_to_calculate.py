from abc import ABC, abstractmethod

class FunctionToCalculate(ABC):
    @abstractmethod
    def calculate(self, variables):
        """
                Calculate the value of the function for the given variables.

                Parameters:
                variables (list): List of variables for which the function should be calculated.
        """
        pass
