# Saving and Reading User-generated data

# Saving data with json is useful when you're working with user-generated
    # b/c if you don't store your user's information somehow, you'll lost it
        # when the program stops running

# Let's look at an example 

from pathlib import Path
import json

def greet_user():
    """Greet user by name"""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Hello and welcome back {username}")
    else:
        contents = input("Please enter your name: ")
        username = json.dumps(username)
        path.write_text(username)
        print(f"We will remember you for next time {username}")

greet_user()