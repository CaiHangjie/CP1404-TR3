"""Estimate: 30 minutes.
Actual: [40min]."""


class Guitar:
    """Represent a Guitar object with name, year, and cost."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """String representation."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Current year"""
        year_value = 2024
        return year_value - self.year

    def is_vintage(self):
        return self.get_age() >= 50