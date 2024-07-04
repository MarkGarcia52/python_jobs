# Addition:

# When you try to convert input to int, you'll get a ValueError

# Write a program that prompts for two numbers.
    # Add them together and print the result.
        # Catch the value error message
            # Test your program by entering two numbers and then
                # By enetering some text instead of a number.

print("Give me two numbers to add")
print("Enter 'q' to quit.")

while True:
    first_number = input(f"Enter your first number: ")
    if first_number == 'q':
        break

    second_number = input("Enter your second number: ")
    if second_number == 'q':
        break

    try:
        result_addition = int(first_number) + int(second_number)

    except ValueError:
        print("Please enter an integer")

    else:
        print(result_addition)

# Division Calculator

# Wrap code from Exercise 10-6 in a while loop so the user can continue
# entering numbers, even if they make a mistake and enter text instead
# of a number

print("Give me two numbers and I'll divide them")
print("Enter a 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break

    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("You can't enter letters.")
        pass

    else:
        if first_number and second_number == int():
            print(answer)

# Cats and Dogs

# Write a program that tries to read these files and print the contents
#   of the file to the screen

# wrap code in try-except block to catch the FileNotFound error, and print message
# if it is missing

from pathlib import Path

def read_text(file_path):
    """Read the the contents inside text files"""
    try:
        content = file_path.read_text(encoding='utf-8')
        print(content)
    except FileNotFoundError:
        print(f"Sorry, the file {file_path} doesn't exist.")
    
directory_path = Path('text_files')
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    file_path = directory_path / filename
    read_text(file_path)


    


