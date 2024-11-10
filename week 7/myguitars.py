from guitar import Guitar
import csv


def load_guitars(filename):
    """Read data from guitars.comsv and create a list of Guitar objects"""
    guitars = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    """Save a list of Guitar """
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for guitar in guitars:
            csv_writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    filename = 'guitars.csv'
    """Load a saved guitar from a CSV file"""
    guitars = load_guitars(filename)

    # Display all loaded guitars
    print("These are all lmy guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

    # Sort guitars , sorted list
    guitars.sort(key=lambda guitar: guitar.year)
    print("\nGuitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)

    # Add new guitars
    print("\nInput new guitars :")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")

    # Save all guitars
    save_guitars(filename, guitars)
    print("\nAll guitars have been saved.")


main()
