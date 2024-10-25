import math

from app.functions.function_to_calculate import FunctionToCalculate
class SzwefelCustomImpl(FunctionToCalculate):
    def calculate(self, variables):
        # Global Minimum:
        # Function Value: 2.545567497236334e-5
        # Coordinates: [420.9687, 420.9687]
        # This means that the global minimum of the Schwefel function is achieved at the point (420.9687, 420.9687)
        # with a function value close to zero, which is the theoretical minimum of the function.

        # Local Minimum:
        # Function Value: 118.43836006957031
        # Coordinates: [-302.5249351839932, 420.9687467475071]

        n = len(variables)
        sum_term = 0.0

        for x in variables:
            sum_term += x * math.sin(math.sqrt(abs(x)))

        return 418.9829 * n - sum_term