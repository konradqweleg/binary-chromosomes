from tkinter import  Entry


class InputValidations:
    def __init__(self, tk):
        self.tk = tk

    def number_input_validation(self):
        return self.tk.register(self._is_digit)

    def _is_digit(self, input_value):
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

    def _get_all_entry_fields(self):
        fields = []
        for widget in self.tk.winfo_children():
            if isinstance(widget, Entry) and widget.winfo_viewable():
                fields.append(widget)
        return fields