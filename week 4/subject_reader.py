"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)  # Append the list [subject, lecturer, number of students] to data


    input_file.close()
    return data  # Return the list of lists


def display_subject_details(data):
    for subject in data:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


main()