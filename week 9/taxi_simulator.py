from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """main program"""
    available_taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    total_cost = 0
    selected_taxi = None

    print("Let's drive!")
    while True:
        user_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
        print(f"Bill to date: ${total_cost:.2f}")
        if user_choice == 'q':
            print(f"Total trip cost: ${total_cost:.2f}")
            print("Taxis are now:")
            display_taxis(available_taxis)
            break
        elif user_choice == 'c':
            selected_taxi = choose_taxi(available_taxis)
        elif user_choice == 'd':
            if selected_taxi:
                trip_cost = drive_taxi(selected_taxi)
                total_cost += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")


def display_taxis(taxis):
    """Display all available taxis"""
    print("Taxis available:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def choose_taxi(taxis):
    """Select a taxi from the list"""
    display_taxis(taxis)
    try:
        taxi_index = int(input("Choose taxi: "))
        if 0 <= taxi_index < len(taxis):
            return taxis[taxi_index]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


def drive_taxi(taxi):
    """Drive the selected taxi and return the fare cost."""
    try:
        distance = float(input("Drive how far? "))
        if distance <= 0:
            print("Distance must be greater than zero.")
            return 0
        taxi.drive(distance)
        fare = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid input")
        return 0


main()
