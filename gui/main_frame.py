import time
from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button, BooleanVar
from tkinter.ttk import Radiobutton


from app.models.configuration_genetic_algorithm import ConfigurationGeneticAlgorithm
from app.models.enums.cross_method import CrossoverMethod
from app.models.enums.function_to_calculate import FunctionToCalculate
from app.models.enums.mutation_method import MutationMethod
from app.models.enums.selection_method import SelectionMethod
from app.models.binary_chromosomes_configuration_data import BinaryChromosomesConfigurationData
from gui.input_validations.input_validations import InputValidations


class MainFrame:
    root = Tk()

    input_validations = InputValidations(root)

    def __init__(self):
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

    def initialization_frame(self):

        begin_of_the_range_label = Label(self.root, text="Begin of the range")
        begin_of_the_range_label.pack()
        self.begin_of_the_range_entry = Entry(self.root, validate='all', validatecommand=(self.input_validations.number_input_validation(), '%P'))
        self.begin_of_the_range_entry.pack()

        end_of_the_range_label = Label(self.root, text="End of the range")
        end_of_the_range_label.pack()
        self.end_of_the_range_entry = Entry(self.root, validate='all', validatecommand=(self.input_validations.number_input_validation(), '%P'))
        self.end_of_the_range_entry.pack()

        precision = Label(self.root, text="Precision")
        precision.pack()
        self.precision_entry = Entry(self.root)
        self.precision_entry.pack()

        population_label = Label(self.root, text="Population")
        population_label.pack()
        self.population_entry = Entry(self.root, validate='all', validatecommand=(self.input_validations.number_input_validation(), '%P'))
        self.population_entry.pack()

        epochs_label = Label(self.root, text="Epochs")
        epochs_label.pack()
        self.epochs_entry = Entry(self.root)
        self.epochs_entry.pack()


        num_variable = Label(self.root, text="Number of parameters")
        num_variable.pack()
        self.num_variable_entry = Entry(self.root)
        self.num_variable_entry.pack()

        elite_strategy_label = Label(self.root, text="Percentage elite strategy")
        elite_strategy_label.pack()
        self.elite_strategy_entry = Entry(self.root)
        self.elite_strategy_entry.pack()

        cross_probability_label = Label(self.root, text="Cross probability")
        cross_probability_label.pack()
        self.cross_probability_entry = Entry(self.root)
        self.cross_probability_entry.pack()

        mutation_probability_label = Label(self.root, text="Mutation probability")
        mutation_probability_label.pack()
        self.mutation_probability_entry = Entry(self.root)
        self.mutation_probability_entry.pack()


        inversion_probability_label = Label(self.root, text="Inversion probability")
        inversion_probability_label.pack()
        self.inversion_probability_entry = Entry(self.root)
        self.inversion_probability_entry.pack()

        selection_method_label = Label(self.root, text="Choose the selection method")
        selection_method_label.pack()
        self.selection_method_selected_option = StringVar(value=SelectionMethod.BEST_SELECTION.value)
        selection_method_enum_values = list(map(lambda selection_method: selection_method.value, SelectionMethod))
        self.selection_method_selected_option.trace("w", self._change_selection_method)
        selection_method_option_menu = OptionMenu(self.root, self.selection_method_selected_option, *selection_method_enum_values)
        selection_method_option_menu.pack()

        percentage_the_best_to_select_label = Label(self.root, text="Percentage the best to select")
        percentage_the_best_to_select_label.pack_forget()
        self.percentage_the_best_to_select_entry = Entry(self.root)
        self.percentage_the_best_to_select_entry.pack_forget()

        self.tournament_size_label = Label(self.root, text="Tournament size")
        self.tournament_size_label.pack_forget()
        self.tournament_size_entry = Entry(self.root, validate='all',
                                            validatecommand=(self.input_validations.number_input_validation(), '%P'))
        self.tournament_size_entry.pack_forget()

        roulette_wheel_selection_percentage_chromosomes_to_select_label = Label(self.root, text="Percentage the best to select")
        roulette_wheel_selection_percentage_chromosomes_to_select_label.pack_forget()
        self.roulette_wheel_selection_percentage_chromosomes_to_select_entry = Entry(self.root)
        self.roulette_wheel_selection_percentage_chromosomes_to_select_entry.pack_forget()

        cross_method_label = Label(self.root, text="Choose the cross method")
        cross_method_label.pack()
        self.cross_method_selected_option = StringVar(value=CrossoverMethod.ONE_POINT.value)
        self.cross_method_selected_option.trace("w", self._change_cross_method)
        cross_method_enum_values = list(map(lambda cross_method: cross_method.value, CrossoverMethod))
        cross_method_option_menu = OptionMenu(self.root, self.cross_method_selected_option, *cross_method_enum_values)
        cross_method_option_menu.pack()

        self.block_size_label = Label(self.root, text="Block size")
        self.block_size_label.pack_forget()
        self.block_size_entry = Entry(self.root, validate='all',
                                              validatecommand=(self.input_validations.number_input_validation(), '%P'))
        self.block_size_entry.pack_forget()

        self.probability_to_crossover_block_label = Label(self.root, text="Probability to crossover blocks")
        self.probability_to_crossover_block_label.pack_forget()
        self.probability_to_crossover_block_entry = Entry(self.root)
        self.probability_to_crossover_block_entry.pack_forget()

        self.probability_to_crossover_gene_label = Label(self.root, text="Probability to crossover gene")
        self.probability_to_crossover_gene_label.pack_forget()
        self.probability_to_crossover_gene_entry = Entry(self.root)
        self.probability_to_crossover_gene_entry.pack_forget()

        mutation_probability_label = Label(self.root, text="Choose the mutation method")
        mutation_probability_label.pack()
        self.mutation_probability_selected_option = StringVar(value=MutationMethod.ONE_POINT.value)
        mutation_method_enum_values = list(map(lambda mutation: mutation.value, MutationMethod))
        mutation_method_option_menu = OptionMenu(self.root, self.mutation_probability_selected_option, *mutation_method_enum_values)
        mutation_method_option_menu.pack()

        function_to_calculate_label = Label(self.root, text="Choose the function to calculation")
        function_to_calculate_label.pack()
        self.function_to_calculate_selected_option = StringVar(value=FunctionToCalculate.SZWEFEL.value)
        function_to_calculate_enum_values = list(map(lambda function_to_calculation: function_to_calculation.value, FunctionToCalculate))
        function_to_calculate_option_menu = OptionMenu(self.root, self.function_to_calculate_selected_option,
                                                 *function_to_calculate_enum_values)
        function_to_calculate_option_menu.pack()

        self.optimization_type = StringVar(value='minimization')
        minimalization_function = Radiobutton(self.root, text="Minimalization function", variable=self.optimization_type, value='minimization')
        minimalization_function.pack()
        maximization_function = Radiobutton(self.root, text="Maximization function", variable=self.optimization_type, value='maximization')
        maximization_function.pack()


        start_button = Button(self.root, text="Start", command=self.run_generic_algorithm)
        start_button.pack()

        self.root.geometry('500x1000')
        self.root.title('Binary Chromosomes')
        self.root.resizable(False, False)
        self.root.mainloop()
        print("Initializing Frame")

    def _change_cross_method(self, *args):
        self.block_size_label.pack_forget()
        self.block_size_entry.pack_forget()
        self.probability_to_crossover_block_label.pack_forget()
        self.probability_to_crossover_block_entry.pack_forget()
        self.probability_to_crossover_gene_label.pack_forget()
        self.probability_to_crossover_gene_entry.pack_forget()

        match CrossoverMethod(self.cross_method_selected_option.get()):
            case CrossoverMethod.GRANULAR_CROSSOVER:
                self.block_size_label.pack()
                self.block_size_entry.pack()
                self.probability_to_crossover_block_label.pack()
                self.probability_to_crossover_block_entry.pack()
            case CrossoverMethod.UNIFORM_CROSSOVER:
                self.probability_to_crossover_gene_label.pack()
                self.probability_to_crossover_gene_entry.pack()


    def _change_selection_method(self, *args):
        self.tournament_size_label.pack_forget()
        self.tournament_size_entry.pack_forget()
        match SelectionMethod(self.selection_method_selected_option.get()):
            case SelectionMethod.TOURNAMENT_SELECTION:
                self.tournament_size_label.pack()
                self.tournament_size_entry.pack()

    def _get_form_data(self):
        binary_chromosomes_configuration_data = BinaryChromosomesConfigurationData
        binary_chromosomes_configuration_data.mutation_method = MutationMethod(self.mutation_probability_selected_option.get())
        binary_chromosomes_configuration_data.cross_method = CrossoverMethod(self.cross_method_selected_option.get())
        binary_chromosomes_configuration_data.selection_method = SelectionMethod(self.selection_method_selected_option.get())
        binary_chromosomes_configuration_data.inversion_probability = self.inversion_probability_entry.get()
        binary_chromosomes_configuration_data.mutation_probability = self.mutation_probability_entry.get()
        binary_chromosomes_configuration_data.cross_probability = self.cross_probability_entry.get()
        binary_chromosomes_configuration_data.elite_strategy = self.elite_strategy_entry.get()
        binary_chromosomes_configuration_data.population = self.population_entry.get()
        binary_chromosomes_configuration_data.end_of_the_range = self.end_of_the_range_entry.get()
        binary_chromosomes_configuration_data.begin_of_the_range = self.begin_of_the_range_entry.get()
        binary_chromosomes_configuration_data.epochs = self.epochs_entry.get()
        binary_chromosomes_configuration_data.optimization_type = self.optimization_type
        binary_chromosomes_configuration_data.function_to_calculate = self.function_to_calculate_selected_option
        binary_chromosomes_configuration_data.percentage_the_best_to_select = self.percentage_the_best_to_select_entry.get()
        binary_chromosomes_configuration_data.roulette_wheel_selection_percentage_chromosomes_to_select =
        binary_chromosomes_configuration_data.block_size = self.block_size_entry.get()
        binary_chromosomes_configuration_data.probability_to_crossover_block = self.probability_to_crossover_block_entry.get()
        binary_chromosomes_configuration_data.tournament_size = self.tournament_size_entry.get()
        return binary_chromosomes_configuration_data

    def start(self):
        self.initialization_frame()

    def run_generic_algorithm(self):
        if not self.input_validations.check_if_required_fields_are_completed():
            configuration_data = self._get_form_data()
            configuration_generic_algorithm = ConfigurationGeneticAlgorithm()
            generic_algorithm = configuration_generic_algorithm.configuration(configuration_data)
            start_time = time.time()
            generic_algorithm.run()
            end_time = time.time()
            execution_time = end_time - start_time
            print(f'Execution time: {execution_time}')

fra = MainFrame()
fra.start()