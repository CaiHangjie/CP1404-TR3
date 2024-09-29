MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """
    The main function is to manage the scoring system.
Users can input the correct score and then print the result,
Display stars representing scores or exit the program.
    """
    score = get_score("Enter your score: ")
    print(MENU)
    choice = get_choice("Enter your choice: ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_score("Enter your score: ")
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = get_choice("Enter your choice: ").upper()

    print("Thank you!")


def get_choice(prompt):
    """
    Prompts the user to enter a choice from the menu.

    Args:
        prompt (str): The message to display for user input.

    Returns:
        str: The user's choice as a string.
    """
    choice = input(prompt)
    return choice


def get_score(prompt):
    """
    Prompts the user to enter a valid score between 0 and 100.

    Args:
        prompt (str): The message to display for user input.

    Returns:
        float: A valid score between 0 and 100.
    """
    score = float(input(prompt))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def check_score(score):
    """
    Evaluates the score and returns a performance rating.

    Args:
        score (float): A score between 0 and 100.

    Returns:
        str: The result based on the score:
             "Bad" for scores below 50,
             "Pass" for scores between 50 and 89,
             "Excellent" for scores 90 and above.
    """
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


def print_result(score):
    """
    Prints the result of the score evaluation.

    Args:
        score (float): The score to evaluate and print the result for.
    """
    result = check_score(score)
    print(f"Your result is {result}")


def show_stars(score):
    """
    Displays a row of stars corresponding to the score.

    Args:
        score (float): The score to represent with stars.
    """
    print("*" * int(score))


main()
