# Removing all instances of specific values from a list
#   We used remove() to remove a specific value from a list
#       This worked b/c the value we were interested in appeared once
#           But what if you want to remove all instances of the value?

# You want 'cat' removed in all instances

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# While will loop through the list until each instance of 'cat' is removed

# Passing arguments

# Can have multiple parameters, a funciton call may need multiple arguments
#   You can pass arguments to your functions in a number of ways
#       You can use positional arguments which need to be in the same order the parameters were written
#           Keyword arguments, where each argument consists of a variable name and a value;
#               and lists and dictionaries of values

pets = {}

program_active = True

while program_active:
    answer = input("\nWhat's your favorite dog? ")
    name = input("\nWhat's your name? ")
    quit = input("Would you like to continue (yes/no)? ")

    pets[name] = answer

    if quit == 'no':
        program_active = False

else:
    print("---Poll Results---")
    for name, answer in pets.items():
        print(f" {name} your favorite dog is a {answer}\n")

# Tried program again *=^

# Positional arguments

# When you call a function Python must match each argumnet in hte funciton call with a parameter,
#   in the function definition

# The simplest way to do this is based on the order of the arguments provided
#   Values matched up this way are called positional arguments

def describe_pet(animal_type, pet_name='dog'): #1
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')
describe_pet('willie') #1 deleted 'dog',

# This displays both sets of arguments with respective parameters : animal_type and pet_name

# Keyword Arguments
# Name-value pair that you pass to a function
#   You directly associate the name and the value within the argument
#       There's 0 confusion whatsoever
#           They clarify the role of each value in the function call

describe_pet(animal_type='hamster', pet_name='harry')

# Default values
# When writing a functoin, you can define a default valuefor each parameter
#   If an argument for a paramter is provided in the function call, Python uses the argument
#       value. If not, it uses the parameter, you can exclue the corresponding argument you'd usually write in the
#           function call
#               Using default values can simplify your function calls and clarify hte ways your functions are used

#1 ^^^^

