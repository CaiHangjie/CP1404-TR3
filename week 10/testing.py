"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n) # Fix the space


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length # fix the word is as long or longer than the length passed in

def format_sentence(phrase):
    """
     Write and test a function to format a phrase as a sentence.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('There is a more beautiful parrot here')
    'There is a more beautiful parrot here.'
    """
    return phrase.capitalize() + "."

def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # Test default fuel value
    test_car_default = Car()
    assert test_car_default.fuel == 0, "Car does not set default fuel correctly"

    # Test custom fuel value
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly "

    # Test odometer
    assert test_car._odometer == 0, "Car does not set odometer correctly"


run_tests()

# Uncomment the following line and run the doctests
doctest.testmod()


