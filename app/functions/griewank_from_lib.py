import benchmark_functions as bf
from app.functions.function_to_calculate import FunctionToCalculate
class GriewankFromLib(FunctionToCalculate):
    def calculate(self, variables):
        n = len(variables)
        func = bf.Griewank(n_dimensions=n)
        return func(variables)















