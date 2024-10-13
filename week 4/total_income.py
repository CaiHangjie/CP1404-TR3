"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? ")) # Refactor the months variable to a better name.


    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Using f-string for input
        incomes.append(income)

    print_income_report(incomes, number_of_months)


def print_income_report(incomes, number_of_months):

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()