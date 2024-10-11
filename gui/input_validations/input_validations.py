class InputValidations:
    def __init__(self, tk):
        self.tk = tk

    def number_input_validation(self):
        return self.tk.register(self._is_digit)

    def _is_digit(self, input_value):
            if str.isdigit(input_value) or input_value == "":
                return True
            else:
                return False
