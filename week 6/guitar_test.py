from guitar import Guitar


def test_guitar_features():
    """Test Guitar class methods"""
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    second_guitar = Guitar("Another Guitar", 2013, 6666.66)

    print("Gibson L-5 CES get_age() - Expected 100. Got", first_guitar.get_age())
    print("Another Guitar get_age() - Expected 9. Got", second_guitar.get_age())

    print("Gibson L-5 CES is_vintage() - Expected True. Got", first_guitar.is_vintage())
    print("Another Guitar is_vintage() - Expected False. Got", second_guitar.is_vintage())


test_guitar_features()