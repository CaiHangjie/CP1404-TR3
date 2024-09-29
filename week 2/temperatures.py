MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """
    The main function of converting between Celsius and Fahrenheit is displayed
And prompt the user to input and execute the code according to the selection.
    """
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    celsius (float): The temperature in Celsius.
    Returns:
        float: The temperature in Fahrenheit.
    """
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    fahrenheit (float): The temperature in Fahrenheit.
    Returns:
        float: The temperature in Celsius.
    """
    return 5 / 9 * (fahrenheit - 32)


main()
