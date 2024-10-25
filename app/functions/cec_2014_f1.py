from opfunu.cec_based import F12014

from app.functions.function_to_calculate import FunctionToCalculate


class Cec2014F1(FunctionToCalculate):
    def calculate(self, variables):
        n = len(variables)
        func = F12014(ndim=n)
        return func.evaluate(variables)
#import numpy as np
#$from opfunu.cec_based.cec2014 import F12014

# func = F12014(ndim=10)
# func.evaluate(func.create_solution())
# print(func.f_global)
#
# x = np.ones(10)
# print(func.evaluate(x))
# print(func.x_global)
# print(func.bounds)
#
#
# xres = [-3.125, 46.875, -100.0, 96.875, 96.875, -100.0, 100.0, -40.625, 46.875, -21.875]
# print(func.is_succeed(xres))
# print(func.is_succeed(func.x_global))
#
# #Decoded values of the best chromosome: [-3.125, 46.875, -100.0, 96.875, 96.875, -100.0, 100.0, -40.625, 46.875, -21.875]
