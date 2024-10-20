"""
Word Occurrences
Estimate: 35 minutes
Actual:   45 minutes
"""
def main():
    email_to_user = {}

    email_input = input("Email: ").strip()
    while email_input:
        inferred_name = infer_name_from_email(email_input)

        response = input(f"Is your name {inferred_name}? (Y/n) ").strip().lower()
        if response == 'y' or response == '':
            email_to_user[inferred_name] = email_input
        else:
            inferred_name = input("Name: ").strip().title()
            email_to_user[inferred_name] = email_input

        email_input = input("Email: ").strip()


    for name, email in email_to_user.items():
        print(f"{name} ({email})")


def infer_name_from_email(email):
    prefix = email.split('@')[0]
    name_parts = prefix.split('.')
    formatted_name = " ".join(part.title() for part in name_parts)
    return formatted_name


main()
