PASSWORD_LENGTH_THRESHOLD = 6


def main():
    """
    Function: Obtain password, verify length, and print asterisk as feedback.
    Prompt the user to enter the minimum password length or use the default threshold.
    """
    password = get_password()
    min_length = int(input(
        f"Enter password minimum length (press Enter to use {PASSWORD_LENGTH_THRESHOLD}): ") or PASSWORD_LENGTH_THRESHOLD)

    while len(password) < min_length:
        print("Non Conformance")
        password = get_password()

    print("*" * len(password))


def get_password():
    """
    Prompts the user to input a password and validates that it is not empty.
    Returns: Require user to enter a valid password
    """
    while True:
        password = input("Enter your password: ").strip()
        if password:
            return password
        else:
            print("Password cannot .Please try again.")


main()
