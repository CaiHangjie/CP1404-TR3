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
        """Determine if the guitar is over 50 years old"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Write code for the (less than) method so that it compares Guitars by year."""
        return self.year < other.year