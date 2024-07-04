from pathlib import Path

contents = "I love programming!\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"


path = Path('text_files/programming.txt')
path.write_text(contents)

# It's literally writing to the text files. That's pretty sweet.