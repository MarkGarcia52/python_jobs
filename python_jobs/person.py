# Returning a dictionary
# A function can return any kind of value you need it to, including more 
#   complicated data structures like lists and dictionaries

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# The function build_person takes in a first and last name, and puts these 
#   values into a dictionary
#       The value of first is stored with teh key 'first' and last with key
#           'last'.

# Then the entire dictionary representing the person is returned
#   The return value is printed with the original two pieces of textual
#       information now stored in a dictionary

# This allows you to store a person's age as well

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# We added a new optional parameter age to the function definition and assign
#   the parameter the special value None, which is used when a variable has
#       no specific value assigned to it

# You can think of None as a placeholder value
#   In conditional tests, none evaluates to be False
#       If the function called includes a value for age, that value is stored
#           in dictionary. This function always stores a person's name,
#               but it can be modified o store any other info. you want about
#                   person

# Using a function with a while Loop
#   You can use functions with all the Python structures you've learned about
#       so far

# Greeting people using first and last name

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit the program)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")

# If we want to put a quit option in there