import opfunu
from opfunu.cec_based import F12014

from app.functions.function_to_calculate import FunctionToCalculate


class Cec2014F1(FunctionToCalculate):
    def calculate(self, variables):
        n = len(variables)
        func = F12014(ndim=n)
        return func.evaluate(variables)


#
# problem = opfunu.cec_based.F12014(ndim=10)
#
# # Wyświetlenie globalnej wartości minimum
# print("Globalne minimum (f_global):", problem.f_global)
#
# # Wyświetlenie globalnego punktu minimum
# print("Globalny punkt minimum (x_global):", problem.x_global)
#
# # Wyświetlenie zakresów dla zmiennych
# print("Zakresy dla zmiennych (bounds):", problem.bounds)

# import numpy as np
# from opfunu.cec_based.cec2014 import F12014, F52014
#
# func = F12014(ndim=10)
# # func.evaluate(func.create_solution())
# print(func.f_global)
# print(func.x_global)
# print(func.bounds)
# # #
# # x = np.ones(10)
# # print(func.evaluate(x))
#





# # Visualize opfunu function using method in object
# func.plot_2d(selected_dims=(2, 3), n_points=300, ct_cmap="viridis", ct_levels=30, ct_alpha=0.7,
#            fixed_strategy="mean", fixed_values=None, title="Contour map of the F1 CEC 2014 function",
#            x_label=None, y_label=None, figsize=(10, 8), filename="2d-f12010", exts=(".png", ".pdf"), verbose=True)
#
# func.plot_3d(selected_dims=(1, 6), n_points=500, ct_cmap="viridis", ct_levels=30, ct_alpha=0.7,
#            fixed_strategy="mean", fixed_values=None, title="3D visualization of the F1 CEC 2014 function",
#            x_label=None, y_label=None, figsize=(10, 8), filename="3d-f12010", exts=(".png", ".pdf"), verbose=True)


#
#
# xres = [-3.125, 46.875, -100.0, 96.875, 96.875, -100.0, 100.0, -40.625, 46.875, -21.875]
# print(func.is_succeed(xres))
# print(func.is_succeed(func.x_global))
#
# #Decoded values of the best chromosome: [-3.125, 46.875, -100.0, 96.875, 96.875, -100.0, 100.0, -40.625, 46.875, -21.875]
