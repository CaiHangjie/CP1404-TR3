# Part 1: Write code that asks the user for their name"
user_name = input("Enter yours name: ")
out_file = open('name.txt', 'w')
out_file.write(user_name)
out_file.close()

# Part 2: Write code that opens "name.txt" and reads
in_file = open('name.txt', 'r')
in_file.read().strip()
in_file.close()

print("Hi Bob!")

# Part 3: Create a text file called numbers.txt and save
with open('numbers.txt', 'w') as out_file:
    out_file.write("17\n")
    out_file.write("42\n")
    out_file.write("400\n")

with open('numbers.txt', 'r') as in_file:
    number1 = int(in_file.readline().strip())
    number2 = int(in_file.readline().strip())

result = number1 + number2
print(result)

# Part 4: Prints the total for all lines
with open('numbers.txt', 'r') as in_file:
    total = 0
    for line in in_file:
        total += int(line.strip())

print(f"The total is: {total}")
