# from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()
# print(contents)

# from pathlib import Path

# path = Path('text_files/pi_digits.txt')
# contents = path.read_text()
# print(contents)

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#    pi_string += line

# print(f"pi_string[:52]...")
# print(len(pi_string))

from pathlib import Path

path = Path('text_files/pi_digits.txt')
content = path.read_text()
print(content)

lines = content.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# I need the resources for the 1st million at https://ehmatthes.github.io/pcc_3e