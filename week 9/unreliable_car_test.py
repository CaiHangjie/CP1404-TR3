from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    # Create a test vehicle with 80% fuel and 30% reliability
    my_car = UnreliableCar("Unreliable Test Car", 80, 30)

    # First attempt at driving
    print("Attempting to drive 80km:")
    distance_driven = my_car.drive(80)
    print(f"Distance driven: {distance_driven}km")
    print(my_car)

    # Second attempt at driving
    print("\nAttempting to drive 30km:")
    distance_driven = my_car.drive(30)
    print(f"Distance driven: {distance_driven}km")
    print(my_car)


main()
