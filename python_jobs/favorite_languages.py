favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language.title()}")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# You could use the same syntax for anyone in the dictionary

# Looping through all the keys from the dictionary favorite languages

for name in favorite_languages.keys():
    print(name.title())

# and assign them one at a time to the variable name

# This loop tells Python to pull all the keys from the dictionary
# favorite_languages and assign them on eat a time to the variable name
# The output shows each name one at a time

# Looping through the keys is a default behavior in python
# so there is no need to add .keys()

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\n{name.title()}, I see you love {language}")

# You can use the keys() method to find out if a particular person was polled.
# This time, let's find out if Erin took the poll

if 'erin' not in favorite_languages.keys():
    print("Erin, please take your poll!")

# Looping through a dictionary returns the items in the same order they
# were inserted
# Sometimes, you'll want to loop through a dictionary in a different order

# One way to do this is to sort the keys as they're returned in teh for loop
# You can use the sorted() function to get a copy of the keys in order

for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary

# If you are primarily interested in values that a dictionary contains,
# you can use the values() method to return a sequence of values without any 
# keys

print("The following languages have been mentioned")
for language in favorite_languages.values():
    print(language.title())

# Again, the for statement assigns values to the variable language

# This approach pulls all values from teh dictionary without checking for
# repeats

# This might work with a small number of values but in a poll with a large 
# number of people, it would result in a very reptitive list

# a set() is a collection in which each item is unique

print("The following language have been mentioned.")
for language in set(favorite_languages.values()):
    print(language.title())

# When you wrap set() around a collection of values that contains duplicates
# python identifies the unique items in the collection and builds a 
# set from those items. Here we use set() to pull out the unique languages in
# favorite_languages.values()

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah' : ['c'],
    'edward' : ['rust', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")



