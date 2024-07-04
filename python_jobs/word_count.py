# Working with multiple files

# Let's add more books to analyze

from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents: path.read_text(endoing='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approx. number of words in a file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('text_files/alice.txt')
count_words(path)

# Nowe we can write a short loop to count the words in any text we want

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt'
             'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)