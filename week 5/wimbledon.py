"""
Word Occurrences
Estimate: 40 minutes
Actual:   50 minutes
"""

import csv

def main():
    player_wins = {}
    winning_countries = set()

    filename = "wimbledon.csv"
    extract_wimbledon_data(filename, player_wins, winning_countries)

    show_player_wins(player_wins)
    list_countries(winning_countries)


def extract_wimbledon_data(filename, player_wins, winning_countries):
    with open(filename, "r", encoding="utf-8-sig") as file:
        csv_data = csv.reader(file)
        next(csv_data)

        for record in csv_data:
            player_name = record[2]
            country_name = record[1]

            player_wins[player_name] = player_wins.get(player_name, 0) + 1

            winning_countries.add(country_name)


def show_player_wins(player_wins):
    print("Wimbledon Champions:")
    for player, wins in player_wins.items():
        print(f"{player}: {wins}")


def list_countries(winning_countries):
    """Display the countries that have had Wimbledon champions."""
    print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
    sorted_countries = sorted(winning_countries)  # Sort the set into a list
    print(", ".join(sorted_countries))


main()
