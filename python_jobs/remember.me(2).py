from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    content = path.read_text()
    username = json.loads(content)
    print(f"Hello and welcome back {username}")

else:
    content = input("Please enter your username: ")
    username = json.dumps(content)
    path.write_text(username)
    print(f"We will remember you for next time: {username}")