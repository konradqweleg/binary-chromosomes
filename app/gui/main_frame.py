from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Button

from app.models.enums.cross_method import CrossMethod
from app.models.enums.mutation_method import MutationMethod
from app.models.enums.selection_method import SelectionMethod
from app.models.binary_chromosomes_configuration_data import BinaryChromosomesConfigurationData
from app.gui.input_validations.input_validations import InputValidations


class MainFrame:

    def __init__(self):
        self.mutation_probability_default_option = None
        self.cross_method_default_option = None
        self.selection_method_default_option = None
        self.inversion_probability_entry = None
        self.mutation_probability_entry = None
        self.cross_probability_entry = None
        self.elite_strategy_entry = None
        self.number_of_bits_entry = None
        self.population_entry = None
        self.end_of_the_range_entry = None
        self.begin_of_the_range_entry = None
        self.epochs_entry = None

    def initialization_frame(self):
        root = Tk()

        input_validations = InputValidations(root)

        begin_of_the_range_label = Label(root, text="Begin of the range")
        begin_of_the_range_label.pack()
        self.begin_of_the_range_entry = Entry(root, validate='all', validatecommand=(input_validations.number_input_validation(), '%P'))
        self.begin_of_the_range_entry.pack()

        end_of_the_range_label = Label(root, text="End of the range")
        end_of_the_range_label.pack()
        self.end_of_the_range_entry = Entry(root, validate='all', validatecommand=(input_validations.number_input_validation(), '%P'))
        self.end_of_the_range_entry.pack()

        population_label = Label(root, text="Population")
        population_label.pack()
        self.population_entry = Entry(root, validate='all', validatecommand=(input_validations.number_input_validation(), '%P'))
        self.population_entry.pack()

        number_of_bits_label = Label(root, text="Number of bits")
        number_of_bits_label.pack()
        self.number_of_bits_entry = Entry(root, validate='all', validatecommand=(input_validations.number_input_validation(), '%P'))
        self.number_of_bits_entry.pack()

        epochs_label = Label(root, text="Epochs")
        epochs_label.pack()
        self.epochs_entry = Entry(root)
        self.epochs_entry.pack()

        elite_strategy_label = Label(root, text="Elite strategy")
        elite_strategy_label.pack()
        self.elite_strategy_entry = Entry(root)
        self.elite_strategy_entry.pack()

        cross_probability_label = Label(root, text="Cross probability")
        cross_probability_label.pack()
        self.cross_probability_entry = Entry(root)
        self.cross_probability_entry.pack()

        mutation_probability_label = Label(root, text="Mutation probability")
        mutation_probability_label.pack()
        self.mutation_probability_entry = Entry(root)
        self.mutation_probability_entry.pack()

        inversion_probability_label = Label(root, text="Inversion probability")
        inversion_probability_label.pack()
        self.inversion_probability_entry = Entry(root)
        self.inversion_probability_entry.pack()

        selection_method_label = Label(root, text="Choose the selection method")
        selection_method_label.pack()
        self.selection_method_default_option = StringVar(value=SelectionMethod.RANK_SELECTION.value)
        selection_method_enum_values = list(map(lambda selection_method: selection_method.value, SelectionMethod))
        selection_method_option_menu = OptionMenu(root, self.selection_method_default_option, *selection_method_enum_values)
        selection_method_option_menu.pack()

        cross_method_label = Label(root, text="Choose the cross method")
        cross_method_label.pack()
        self.cross_method_default_option = StringVar(value=CrossMethod.ONE_POINT.value)
        cross_method_enum_values = list(map(lambda cross_method: cross_method.value, CrossMethod))
        cross_method_option_menu = OptionMenu(root, self.cross_method_default_option, *cross_method_enum_values)
        cross_method_option_menu.pack()

        mutation_probability_label = Label(root, text="Choose the mutation method")
        mutation_probability_label.pack()
        self.mutation_probability_default_option = StringVar(value=MutationMethod.ONE_POINT.value)
        mutation_method_enum_values = list(map(lambda mutation: mutation.value, MutationMethod))
        mutation_method_option_menu = OptionMenu(root, self.mutation_probability_default_option, *mutation_method_enum_values)
        mutation_method_option_menu.pack()

        start_button = Button(root, text="Start")
        start_button.pack()

        root.geometry('500x550')
        root.title('Binary Chromosomes')
        root.resizable(False, False)
        root.mainloop()
        print("Initializing Frame")


    def get_form_data(self):
        binary_chromosomes_configuration_data = BinaryChromosomesConfigurationData
        binary_chromosomes_configuration_data.mutation_method = MutationMethod(self.mutation_probability_default_option.get())
        binary_chromosomes_configuration_data.cross_method = CrossMethod(self.cross_method_default_option.get())
        binary_chromosomes_configuration_data.selection_method = SelectionMethod(self.selection_method_default_option.get())
        binary_chromosomes_configuration_data.inversion_probability = self.inversion_probability_entry.get()
        binary_chromosomes_configuration_data.mutation_probability = self.mutation_probability_entry.get()
        binary_chromosomes_configuration_data.cross_probability = self.cross_probability_entry.get()
        binary_chromosomes_configuration_data.elite_strategy = self.elite_strategy_entry.get()
        binary_chromosomes_configuration_data.number_of_bits = self.number_of_bits_entry.get()
        binary_chromosomes_configuration_data.population = self.population_entry.get()
        binary_chromosomes_configuration_data.end_of_the_range = self.end_of_the_range_entry.get()
        binary_chromosomes_configuration_data.begin_of_the_range = self.begin_of_the_range_entry.get()
        binary_chromosomes_configuration_data.epochs = self.epochs_entry.get()
        return binary_chromosomes_configuration_data

    def start(self):
        self.initialization_frame()
