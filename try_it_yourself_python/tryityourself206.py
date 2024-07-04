# Favorite number

#   Write a program that prompts for the user's favorite number
#   Use json.dumps() to store this number in a file

#   In a separate program that reads this value and prints
#   the message: "I know your favorite number is! It's: "

#   I'm just going to combine for the sake of quantity

from pathlib import Path
import json

path = Path('number.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's: {number}")

else:
    contents = input("Please enter your favorite number: ")
    number = json.dumps(contents)
    path.write_text(number)
    print("I'll remember that for next time :)")
