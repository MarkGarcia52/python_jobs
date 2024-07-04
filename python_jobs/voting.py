# Simple if statements.

# if conditional_test
# do something

# Lets say we have a variable representing a person's age
# and we want to know if they are old enough to vote

age = 19
if age >= 19:
    print("\nYou may choose your person of interest!")
    print("\nHave you registered to vote yet?")

# Indented blocks are the same for if statements
# All indented lines after an if will be executed if the test passes
# The entire bock of indented lines will be ignored if test does not pass

age2 = 17
if age2 >= 19:
    print("\nYou may vote!")
else:
    print("\nYou are too young to vote.")
    print("\nRegister as soon as you're 18!")

