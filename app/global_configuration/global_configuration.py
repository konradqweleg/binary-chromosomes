class GlobalConfiguration:
    def __init__(self):
        self.logging_enabled = False

    def set_logging_enabled(self, value):
        self.logging_enabled = value

    def is_logging_enabled(self):
        return self.logging_enabled