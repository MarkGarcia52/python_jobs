from pathlib import Path

username = Path('text_files/username.txt')

data = ""

active = True

while active:
    user_input = input("Enter your name: ")

    if user_input == 'quit':
        active = False
        break

    data += f"{user_input}\n"

with username.open("a") as f:
    f.write_text(data)

# Failed attempt

