from tkinter import  Entry

from app.models.enums.function_to_calculate import FunctionToCalculate


class InputValidations:
    def __init__(self, tk):
        self.tk = tk
        self.allowed_num_variable_to_cec_function =  [10, 20, 30, 50, 100]

    def validate_signed_number(self):
        return self.tk.register(self._is_digit_with_negative)

    def validate_number_input (self):
        return self.tk.register(self._is_digit)

    def validate_percentage_input (self):
        return self.tk.register(self.is_percentage)

    def is_percentage(self, input_value):
        if input_value == "":
            return True

        try:
            value = float(input_value)
            return 0 <= value <= 1
        except ValueError:
            return False

    def _is_digit(self, input_value):
        if str.isdigit(input_value) or input_value == "":
            return True
        else:
            return False

    def _is_digit_with_negative(self, input_value):
        if (input_value.startswith("-") and len(input_value)
                == 1 or input_value[1:].isdigit()):
            return True
        elif input_value.isdigit():
            return True
        elif input_value == "":
            return True
        else:
            return False

    def check_if_required_fields_are_completed(self):
        all_entry_fields = self._get_all_entry_fields()
        empty_fields = []
        for field in all_entry_fields:
            if field.get().strip() == "":
                empty_fields.append(field)
                field.config(highlightbackground="red", highlightcolor="red", highlightthickness=1)
            else:
                field.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)
        return empty_fields

    def end_range_is_less_than_start_range(self, end_range, start_range):
         if start_range > end_range:
             return False

         return True

    def validate_cec_2014_f1_function(self, function_to_calculate, num_variable):
        if (function_to_calculate == FunctionToCalculate.CEC_2014_F1 and
                num_variable in self.allowed_num_variable_to_cec_function):
            return True
        return False

    def _get_all_entry_fields(self):
        fields = []
        for widget in self.tk.winfo_children():
            if isinstance(widget, Entry) and widget.winfo_viewable():
                fields.append(widget)
        return fields