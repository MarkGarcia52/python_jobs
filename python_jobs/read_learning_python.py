from pathlib import Path

path = Path('text_files/learning_python.txt')
contents = path.read_text()
print(contents)

# Store the lines in a list and loop it over each line.

lines = contents.splitlines()
learning_python = ''
for line in lines:
    learning_python += line

print(len(learning_python))

