import random

MIN_SCORE = 0
MAX_SCORE = 100
PASS_MARK = 50
EXCELLENT_MARK = 90

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(R)andom score with result
(Q)uit"""


def main():
    """Main function to control the score menu system."""
    score = get_score("Enter score: ")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_score("Enter score: ")
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "R":
            random_score_with_result()
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you! ")


def get_score(prompt):
    """
    Prompts the user to enter a valid score between MIN_SCORE and MAX_SCORE.

    Args:
        prompt (str): The message to display for user input.

    Returns:
        float: A valid score between MIN_SCORE and MAX_SCORE.
    """
    score = float(input(prompt))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def check_score(score):
    """
    Determines the result based on the score.
    """
    if score < PASS_MARK:
        return "Bad"
    elif score < EXCELLENT_MARK:
        return "Pass"
    else:
        return "Excellent"


def print_result(score):
    """
    Prints the result based on the score.
    Args:
        score (float): The score to evaluate and print the result for.
    """
    result = check_score(score)
    print(f"Your result is: {result}")


def show_stars(score):
    """
    Prints stars corresponding to the score.
    Args:
        score (float): The score to represent with stars.
    """
    print("*" * int(score))


def random_score_with_result():
    """
    Generates a random score and prints
    """
    generated_score = random.randint(MIN_SCORE, MAX_SCORE)
    result = check_score(generated_score)
    print(f"Random score: {generated_score}, which is {result}")


main()
