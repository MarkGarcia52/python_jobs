from pathlib import Path
import json

path = Path('json_files/numbers.json') #1
contents = path.read_text() #2
numbers = json.loads(contents) #3

print(numbers)

#1 We make sure to read the same file we wrote to
#2 Since the data file is just a text file with specific formatting,
    # we can read it with the read_text()method

#3 We then pass the contents of the file to json.loads()
    # This function takes in a JSON-formatted string and returns a Python
        # object (in this case, a list), which we assign numbers

# Finally we print the numbers found in the json file

