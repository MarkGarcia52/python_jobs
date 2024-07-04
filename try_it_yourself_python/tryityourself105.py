# Make a dictionary containing three major rivers and the country each
# river is in

rivers = {
    'Egypt': 'Nile',
    'Colombia': 'Amazon',
    'United States': 'Mississippi River'
    }

# Use a loop to print a sentence about each river,
# 'The Nile runs through Egypt'

for country, river in rivers.items():
    print(f"The {river.title()} is located in {country.title()}")

# Use a loop to print the name of each river included in the dictionary
# Use a loop to print the name of each coutnry included in the dictionary

# Use the code in favorite_languages
# Make a list of people who should take the favorite languages poll

# Include some names that are already in the dictionary and some that are not
# Loop through the lsit of pople who should take the poll

# If they have already taken it, print a message thanking them
# If not, invite them to take the poll

favorite_languages = {
    'Mark': 'Python',
    'Antonio': 'Java',
    'Anderson': 'C++',
    }
for name in favorite_languages.keys():
    print(f"Thank you {name.title()} for taking the poll!")

if 'Erik' not in favorite_languages.keys():
    print(f"Hello Erik can you please take the poll!")
