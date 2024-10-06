"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the numerator or denominator entered by the user is not a valid integer, a ValueError occurs.
For example, there may be errors when entering letters or decimals.

2. When will a ZeroDivisionError occur?
When the user inputs 0 as the denominator, a ZeroDivisionError occurs. Because dividing by zero is an invalid operation.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
I can try.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:  # Check if the denominator is zero
        print("Cannot divide by zero!")  # If it is zero, print a prompt message
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")