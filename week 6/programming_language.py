"""Estimate: 20 minutes.
 Actual: [30min].
 """


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """which returns True/False if the programming language is dynamically typed or not."""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, Appearing in {self.year}"