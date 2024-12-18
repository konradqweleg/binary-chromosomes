import os
import time
from pathlib import Path
from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button, Toplevel
from tkinter.ttk import Radiobutton
import shutil
import numpy as np

from app.configuration.configuration_genetic_algorithm import ConfigurationGeneticAlgorithm
from app.models.enums.cross_method import CrossoverMethod
from app.models.enums.function_to_calculate import FunctionToCalculate
from app.models.enums.mutation_method import MutationMethod
from app.models.enums.selection_method import SelectionMethod
from app.configuration.binary_chromosomes_configuration_data import BinaryChromosomesConfigurationData
from gui.image_explorer import ImageExplorer
from gui.input_validations.input_validations import InputValidations
import matplotlib.pyplot as plt


class MainFrame:
    root = Tk()

    input_validations = InputValidations(root)

    def __init__(self):
        self.validations_label = None
        self.tournament_size_label = None
        self.probability_to_crossover_gene_label = None
        self.probability_to_crossover_block_label = None
        self.block_size_label = None
        self.tournament_size_entry = None
        self.probability_to_crossover_gene_entry = None
        self.probability_to_crossover_block_entry = None
        self.block_size_entry = None
        self.roulette_wheel_selection_percentage_chromosomes_to_select_entry = None
        self.percentage_the_best_to_select_entry = None
        self.optimization_type = None
        self.function_to_calculate_selected_option = None
        self.num_variable_entry = None
        self.precision_entry = None
        self.mutation_probability_selected_option = None
        self.cross_method_selected_option = None
        self.selection_method_selected_option = None
        self.inversion_probability_entry = None
        self.mutation_probability_entry = None
        self.cross_probability_entry = None
        self.elite_strategy_entry = None
        self.population_entry = None
        self.end_of_the_range_entry = None
        self.begin_of_the_range_entry = None
        self.epochs_entry = None
        self.image_folder_number = 0

    def initialization_frame(self):

        begin_of_the_range_label = Label(self.root, text="Begin of the range")
        begin_of_the_range_label.grid(padx=3, pady=3, row=0, column=0, sticky='w')
        self.begin_of_the_range_entry = Entry(self.root, validate="key",
                                              validatecommand=(self.input_validations.validate_signed_number(), "%P"))
        self.begin_of_the_range_entry.grid(padx=3, pady=3, row=0, column=1)
        self.begin_of_the_range_entry.insert(0, "-500")

        end_of_the_range_label = Label(self.root, text="End of the range")
        end_of_the_range_label.grid(padx=3, pady=3, row=1, column=0, sticky='w')
        self.end_of_the_range_entry = Entry(self.root, validate="key",
                                              validatecommand=(self.input_validations.validate_signed_number(), "%P"))


        self.end_of_the_range_entry.grid(padx=3, pady=3, row=1, column=1)
        self.end_of_the_range_entry.insert(0, "500")

        precision = Label(self.root, text="Precision")
        precision.grid(padx=3, pady=3, row=2, column=0, sticky='w')
        self.precision_entry = Entry(self.root, validate="all",
                                              validatecommand=(self.input_validations.validate_percentage_input(), "%P"))
        self.precision_entry.grid(padx=3, pady=3, row=2, column=1)
        self.precision_entry.insert(0, "0.0001")

        population_label = Label(self.root, text="Population")
        population_label.grid(padx=3, pady=3, row=3, column=0, sticky='w')
        self.population_entry = Entry(self.root, validate='key',
                                      validatecommand=(self.input_validations.validate_number_input(), '%P'))
        self.population_entry.grid(padx=3, pady=3, row=3, column=1)
        self.population_entry.insert(0, "15")

        epochs_label = Label(self.root, text="Epochs")
        epochs_label.grid(padx=3, pady=3, row=4, column=0, sticky='w')
        self.epochs_entry = Entry(self.root, validate="key",
                                              validatecommand=(self.input_validations.validate_number_input(), "%P"))
        self.epochs_entry.grid(padx=3, pady=3, row=4, column=1)
        self.epochs_entry.insert(0, "1000")

        num_variable = Label(self.root, text="Number of parameters")
        num_variable.grid(padx=3, pady=3, row=5, column=0, sticky='w')
        self.num_variable_entry = Entry(self.root, validate='key',
                                      validatecommand=(self.input_validations.validate_number_input(), '%P'))
        self.num_variable_entry.grid(padx=3, pady=3, row=5, column=1)
        self.num_variable_entry.insert(0, "3")

        elite_strategy_label = Label(self.root, text="Percentage elite strategy")
        elite_strategy_label.grid(padx=3, pady=3, row=6, column=0, sticky='w')
        self.elite_strategy_entry = Entry(self.root, validate="all",
                                              validatecommand=(self.input_validations.validate_percentage_input(), "%P"))
        self.elite_strategy_entry.grid(padx=3, pady=3, row=6, column=1)
        self.elite_strategy_entry.insert(0, "0.15")

        cross_probability_label = Label(self.root, text="Cross probability")
        cross_probability_label.grid(padx=3, pady=3, row=7, column=0, sticky='w')
        self.cross_probability_entry = Entry(self.root, validate="all",
                                              validatecommand=(self.input_validations.validate_percentage_input(), "%P"))
        self.cross_probability_entry.grid(padx=3, pady=3, row=7, column=1)
        self.cross_probability_entry.insert(0, "0.5")

        mutation_probability_label = Label(self.root, text="Mutation probability")
        mutation_probability_label.grid(padx=3, pady=3, row=8, column=0, sticky='w')
        self.mutation_probability_entry = Entry(self.root, validate="all",
                                              validatecommand=(self.input_validations.validate_percentage_input(), "%P"))
        self.mutation_probability_entry.grid(padx=3, pady=3, row=8, column=1)
        self.mutation_probability_entry.insert(0, "0.01")

        inversion_probability_label = Label(self.root, text="Inversion probability")
        inversion_probability_label.grid(padx=3, pady=3, row=9, column=0, sticky='w')
        self.inversion_probability_entry = Entry(self.root, validate="all",
                                              validatecommand=(self.input_validations.validate_percentage_input(), "%P"))
        self.inversion_probability_entry.grid(padx=3, pady=3, row=9, column=1)
        self.inversion_probability_entry.insert(0, "0.05")

        selection_method_label = Label(self.root, text="Choose the selection method")
        selection_method_label.grid(padx=3, pady=3, row=10, column=0, sticky='w')
        self.selection_method_selected_option = StringVar(value=SelectionMethod.BEST_SELECTION.value)
        selection_method_enum_values = list(map(lambda selection_method: selection_method.value, SelectionMethod))
        self.selection_method_selected_option.trace("w", self._change_selection_method)
        selection_method_option_menu = OptionMenu(self.root, self.selection_method_selected_option,
                                                  *selection_method_enum_values)
        selection_method_option_menu.grid(padx=3, pady=3, row=10, column=1)

        percentage_the_best_to_select_label = Label(self.root, text="Percentage the best to select")
        percentage_the_best_to_select_label.grid(padx=3, pady=3, row=11, column=0, sticky='w')
        self.percentage_the_best_to_select_entry = Entry(self.root)
        self.percentage_the_best_to_select_entry.grid(padx=3, pady=3, row=11, column=1)
        self.percentage_the_best_to_select_entry.insert(0, "0.20")

        self.tournament_size_label = Label(self.root, text="Tournament size")
        self.tournament_size_label.grid_forget()
        self.tournament_size_entry = Entry(self.root, validate='key',
                                           validatecommand=(self.input_validations.validate_number_input(), '%P'))
        self.tournament_size_entry.grid_forget()
        self.tournament_size_entry.insert(0, "3")


        cross_method_label = Label(self.root, text="Choose the cross method")
        cross_method_label.grid(padx=3, pady=3, row=14, column=0, sticky='w')
        self.cross_method_selected_option = StringVar(value=CrossoverMethod.ONE_POINT.value)
        self.cross_method_selected_option.trace("w", self._change_cross_method)
        cross_method_enum_values = list(map(lambda cross_method: cross_method.value, CrossoverMethod))
        cross_method_option_menu = OptionMenu(self.root, self.cross_method_selected_option, *cross_method_enum_values)
        cross_method_option_menu.grid(padx=3, pady=3, row=14, column=1)

        self.block_size_label = Label(self.root, text="Block size")
        self.block_size_label.grid_forget()
        self.block_size_entry = Entry(self.root, validate='key',
                                      validatecommand=(self.input_validations.validate_number_input(), '%P'))
        self.block_size_entry.grid_forget()
        self.block_size_entry.insert(0, "2")

        self.probability_to_crossover_block_label = Label(self.root, text="Probability to crossover blocks")
        self.probability_to_crossover_block_label.grid_forget()
        self.probability_to_crossover_block_entry = Entry(self.root, validate="all",
                                              validatecommand=(self.input_validations.validate_percentage_input(), "%P"))
        self.probability_to_crossover_block_entry.grid_forget()
        self.probability_to_crossover_block_entry.insert(0, "0.5")

        self.probability_to_crossover_gene_label = Label(self.root, text="Probability to crossover gene")
        self.probability_to_crossover_gene_label.grid_forget()
        self.probability_to_crossover_gene_entry = Entry(self.root, validate="all",
                                              validatecommand=(self.input_validations.validate_percentage_input(), "%P"))
        self.probability_to_crossover_gene_entry.grid_forget()
        self.probability_to_crossover_gene_entry.insert(0, "0.5")

        mutation_probability_label = Label(self.root, text="Choose the mutation method")
        mutation_probability_label.grid(padx=3, pady=3, row=18, column=0, sticky='w')
        self.mutation_probability_selected_option = StringVar(value=MutationMethod.ONE_POINT.value)
        mutation_method_enum_values = list(map(lambda mutation: mutation.value, MutationMethod))
        mutation_method_option_menu = OptionMenu(self.root, self.mutation_probability_selected_option,
                                                 *mutation_method_enum_values)
        mutation_method_option_menu.grid(padx=3, pady=3, row=18, column=1)

        function_to_calculate_label = Label(self.root, text="Choose the function to calculation")
        function_to_calculate_label.grid(padx=3, pady=3, row=19, column=0, sticky='w')
        self.function_to_calculate_selected_option = StringVar(value=FunctionToCalculate.SCHWEFEL.value)
        function_to_calculate_enum_values = list(
            map(lambda function_to_calculation: function_to_calculation.value, FunctionToCalculate))
        function_to_calculate_option_menu = OptionMenu(self.root, self.function_to_calculate_selected_option,
                                                       *function_to_calculate_enum_values)
        function_to_calculate_option_menu.grid(padx=3, pady=3, row=19, column=1)

        self.optimization_type = StringVar(value='minimization')
        minimalization_function = Radiobutton(self.root, text="Minimalization function",
                                              variable=self.optimization_type, value='minimization')
        minimalization_function.grid(padx=3, pady=3, row=20, column=0, sticky='w')
        maximization_function = Radiobutton(self.root, text="Maximization function", variable=self.optimization_type,
                                            value='maximization')
        maximization_function.grid(padx=3, pady=3, row=20, column=1)

        start_button = Button(self.root, text="Start", command=self.run_generic_algorithm)
        start_button.grid(padx=3, pady=3, row=21, column=0, columnspan=2)

        self.validations_label = Label(self.root)
        self.validations_label.grid_forget()

        self.root.geometry('370x580')
        self.root.title('Binary Chromosomes')
        self.root.resizable(False, False)
        self.root.mainloop()

    def _change_cross_method(self, *args):
        self.block_size_label.grid_forget()
        self.block_size_entry.grid_forget()
        self.probability_to_crossover_block_label.grid_forget()
        self.probability_to_crossover_block_entry.grid_forget()
        self.probability_to_crossover_gene_label.grid_forget()
        self.probability_to_crossover_gene_entry.grid_forget()

        match CrossoverMethod(self.cross_method_selected_option.get()):
            case CrossoverMethod.GRANULAR_CROSSOVER:
                self.block_size_label.grid(padx=3, pady=3, row=15, column=0, sticky='w')
                self.block_size_entry.grid(padx=3, pady=3, row=15, column=1)
                self.probability_to_crossover_block_label.grid(padx=3, pady=3, row=16, column=0, sticky='w')
                self.probability_to_crossover_block_entry.grid(padx=3, pady=3, row=16, column=1)
            case CrossoverMethod.UNIFORM_CROSSOVER:
                self.probability_to_crossover_gene_label.grid(padx=3, pady=3, row=17, column=0, sticky='w')
                self.probability_to_crossover_gene_entry.grid(padx=3, pady=3, row=17, column=1)


    def _change_selection_method(self, *args):
        self.tournament_size_label.grid_forget()
        self.tournament_size_entry.grid_forget()
        match SelectionMethod(self.selection_method_selected_option.get()):
            case SelectionMethod.TOURNAMENT_SELECTION:
                self.tournament_size_label.grid(padx=3, pady=3, row=12, column=0, sticky='w')
                self.tournament_size_entry.grid(padx=3, pady=3, row=12, column=1)

    def _get_form_data(self):
        binary_chromosomes_configuration_data = BinaryChromosomesConfigurationData
        binary_chromosomes_configuration_data.mutation_method = MutationMethod(self.mutation_probability_selected_option.get())
        binary_chromosomes_configuration_data.cross_method = CrossoverMethod(self.cross_method_selected_option.get())
        binary_chromosomes_configuration_data.selection_method = SelectionMethod(self.selection_method_selected_option.get())
        binary_chromosomes_configuration_data.inversion_probability = float(self.inversion_probability_entry.get())
        binary_chromosomes_configuration_data.mutation_probability = float(self.mutation_probability_entry.get())
        binary_chromosomes_configuration_data.cross_probability = float(self.cross_probability_entry.get())
        binary_chromosomes_configuration_data.elite_strategy = float(self.elite_strategy_entry.get())
        binary_chromosomes_configuration_data.population = int(self.population_entry.get())
        binary_chromosomes_configuration_data.end_of_the_range = int(self.end_of_the_range_entry.get())
        binary_chromosomes_configuration_data.begin_of_the_range = int(self.begin_of_the_range_entry.get())
        binary_chromosomes_configuration_data.epochs = int(self.epochs_entry.get())
        binary_chromosomes_configuration_data.optimization_type = self.optimization_type.get()
        binary_chromosomes_configuration_data.function_to_calculate = FunctionToCalculate(self.function_to_calculate_selected_option.get())
        binary_chromosomes_configuration_data.percentage_the_best_to_select = float(self.percentage_the_best_to_select_entry.get())
        binary_chromosomes_configuration_data.block_size = int(self.block_size_entry.get())
        binary_chromosomes_configuration_data.probability_to_crossover_block = float(self.probability_to_crossover_block_entry.get())
        binary_chromosomes_configuration_data.tournament_size = int(self.tournament_size_entry.get())
        binary_chromosomes_configuration_data.precision = float(self.precision_entry.get())
        binary_chromosomes_configuration_data.num_variable = int(self.num_variable_entry.get())
        binary_chromosomes_configuration_data.probability_to_crossover_gene = float(self.probability_to_crossover_gene_entry.get())
        return binary_chromosomes_configuration_data

    def start(self):
        self.initialization_frame()

    def validate_fields(self, configuration_data):
        if not self.input_validations.end_range_is_less_than_start_range(
                configuration_data.end_of_the_range, configuration_data.begin_of_the_range):
            self.validations_label.config(text="Start range must be less then end range", fg="red")
            self.validations_label.grid(padx=3, pady=3, row=22, column=0, columnspan=2)
            return False
        elif not self.input_validations.validate_cec_2014_f1_function(
                configuration_data.function_to_calculate, configuration_data.num_variable):
            self.validations_label.config(text="F12014 problem is only supported ndim in [10, 20, 30, 50, 100]!",
                                          fg="red")
            self.validations_label.grid(padx=3, pady=3, row=22, column=0, columnspan=2)
            return False
        else:
            self.validations_label.config(text="")
            self.validations_label.grid_forget()
            return True

    def save_parameters_to_file(self):
        parameters_file_path = Path(f'results/{self.image_folder_number}/parameters.txt')

        with parameters_file_path.open('w') as file:
            file.write(f"Mutation Method: {self.mutation_probability_selected_option.get()}\n")
            file.write(f"Crossover Method: {self.cross_method_selected_option.get()}\n")
            file.write(f"Selection Method: {self.selection_method_selected_option.get()}\n")
            file.write(f"Inversion Probability: {self.inversion_probability_entry.get()}\n")
            file.write(f"Mutation Probability: {self.mutation_probability_entry.get()}\n")
            file.write(f"Crossover Probability: {self.cross_probability_entry.get()}\n")
            file.write(f"Elite Strategy: {self.elite_strategy_entry.get()}\n")
            file.write(f"Population: {self.population_entry.get()}\n")
            file.write(f"End of the Range: {self.end_of_the_range_entry.get()}\n")
            file.write(f"Begin of the Range: {self.begin_of_the_range_entry.get()}\n")
            file.write(f"Epochs: {self.epochs_entry.get()}\n")
            file.write(f"Optimization Type: {self.optimization_type.get()}\n")
            file.write(f"Function to Calculate: {self.function_to_calculate_selected_option.get()}\n")
            file.write(f"Percentage of the Best to Select: {self.percentage_the_best_to_select_entry.get()}\n")
            file.write(f"Block Size: {self.block_size_entry.get()}\n")
            file.write(f"Probability to Crossover Block: {self.probability_to_crossover_block_entry.get()}\n")
            file.write(f"Tournament Size: {self.tournament_size_entry.get()}\n")
            file.write(f"Precision: {self.precision_entry.get()}\n")
            file.write(f"Number of Variables: {self.num_variable_entry.get()}\n")
            file.write(f"Probability to Crossover Gene: {self.probability_to_crossover_gene_entry.get()}\n")

    def run_generic_algorithm(self):
        configuration_data = self._get_form_data()
        if (not self.input_validations.check_if_required_fields_are_completed() and
                self.validate_fields(configuration_data)):

            configuration_genetic_algorithm = ConfigurationGeneticAlgorithm()
            genetic_algorithm = configuration_genetic_algorithm.configuration(configuration_data)
            (fitness_value, value_function_on_iteration, avg_on_iteration,
             std_on_iteration, best_fitness, best_chromosome_value,time_calculation) = genetic_algorithm.run()

            folder_path = f'results/{self.image_folder_number}'
            os.makedirs(folder_path, exist_ok=True)


            self.save_results_to_file('algorithm_results.csv', value_function_on_iteration, avg_on_iteration, std_on_iteration)
            self.draw_function_value_over_iterations(value_function_on_iteration)

            last_value = value_function_on_iteration[-1]
            self.plot_avg_fitness_over_iteration(avg_on_iteration)
            self.plot_std_dev_fitness_over_iteration(std_on_iteration)
            self.save_parameters_to_file()
            self.save_final_results_to_file(time_calculation, best_chromosome_value, last_value,(self.image_folder_number))
            self.image_folder_number += 1
            self.open_new_window(time_calculation, best_chromosome_value, last_value,(self.image_folder_number-1))

    def save_final_results_to_file(self, time_calculation, best_chromosome_value, last_value, image_folder_number):
        file_path = Path(f'results/{image_folder_number}/final_results.txt')

        with file_path.open('w') as file:
            file.write(f'Time Calculation: {time_calculation}\n')
            file.write(f'Best Chromosome Value: {best_chromosome_value}\n')
            file.write(f'Last Value: {last_value}\n')





    def downsample_data(self, data, max_points=500):
        if len(data) > max_points:
            indices = np.linspace(0, len(data) - 1, max_points, dtype=int)
            return [data[i] for i in indices], indices
        return data, np.arange(len(data))

    def draw_function_value_over_iterations(self, value_function_on_iteration):
        min_values_per_iteration, indices = self.downsample_data(value_function_on_iteration)

        plt.figure(figsize=(10, 6))
        plt.plot(indices, min_values_per_iteration)
        plt.xlabel('Iteration')
        plt.ylabel('Fitness Value')
        plt.title('Fitness Value Over Iterations')
        plt.grid(True)
        plt.savefig(f'results/{self.image_folder_number}/fitness_value_over_iterations.png')
        plt.savefig('results/fitness_value_over_iterations.png')

        #plt.show()

    def plot_avg_fitness_over_iteration(self, avg_fitness_on_iteration):
        avg_fitness_on_iteration, indices = self.downsample_data(avg_fitness_on_iteration)

        plt.figure(figsize=(10, 6))
        plt.plot(indices, avg_fitness_on_iteration, label='Average Fitness Value')
        plt.xlabel('Iteration')
        plt.ylabel('Fitness Value')
        plt.title('Average Fitness Value Over Iterations')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'results/{self.image_folder_number}/avg_fitness_over_iterations.png')
        plt.savefig('results/avg_fitness_over_iterations.png')
        #plt.show()

    def plot_std_dev_fitness_over_iteration(self, std_dev_fitness_on_iteration):
        std_dev_fitness_on_iteration, indices = self.downsample_data(std_dev_fitness_on_iteration)

        plt.figure(figsize=(10, 6))
        plt.plot(indices, std_dev_fitness_on_iteration, label='Standard Deviation of Fitness Value')
        plt.xlabel('Iteration')
        plt.ylabel('Fitness Value')
        plt.title('Standard Deviation of Fitness Value Over Iterations')
        plt.legend()
        plt.grid(True)
        folder_path = f'results/{self.image_folder_number}'
        os.makedirs(folder_path, exist_ok=True)
        plt.savefig(f'results/{self.image_folder_number}/std_dev_fitness_over_iterations.png')
        plt.savefig('results/std_dev_fitness_over_iterations.png')
       # plt.show()

    def save_results_to_file(self, filename, value_function_on_iteration, avg_fitness_on_iteration,
                             std_dev_fitness_on_iteration):

        with open(f'results/{self.image_folder_number}/{filename}', 'w') as file:
            file.write("Iteration,Best Fitness,Average Fitness,Standard Deviation\n")
            for i in range(len(value_function_on_iteration)):
                file.write(
                    f"{i + 1},{value_function_on_iteration[i]},{avg_fitness_on_iteration[i]},{std_dev_fitness_on_iteration[i]}\n")




    def open_new_window(self, result_time, best_chromosome_value,last_value,number_runs_program):
        new_window = Toplevel(self.root)
        ImageExplorer(new_window, result_time, best_chromosome_value,last_value,number_runs_program)

fra = MainFrame()
fra.start()