# Handling the FileNotFoundError Exception


# One common issue when working with files is handling
    # missing files. The file you're looking for might be
        # in a different location or may not exist at all

# Let's try to read a file that doesn't exist

from pathlib import Path

#path = Path('alice.txt')
#try:
    #content = path.read_text(encoding='utf-8')
#except FileNotFoundError:
    #print(f"Sorry, the file {path} does not exist.")
#else:
    # Count the approx. number of words in the file.
    #words = content.split()
    #num_words = len(words)
    #print(f"The file {path} has about {num_words} words.")

# It's often best to start at the beginning of a traceback

# Analyzing Text

# Using len() on the list gives us a good approximation of the number of words in the original text

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
        pass # Now when fileerrornotfound is raised, the code in the excpet block runs,
    #   but nothing happens. NOt raceback is introduced, no ouput in response, but no 
    #   indication the file was not found
    else:
    # Count the approx. number of words in the file.
        words = content.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
             'little_woman.txt']
for filename in filenames:
    path = Path(filenames)
    count_words(path)

# the name of the files are stored as simple strings. Each string is converted to 
    # A Path object, before the call to count_words()

# Failing Silently


