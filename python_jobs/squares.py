# List comprehensions
# The approach described earlier for generating the list squares
# consisted of using three or four lines of code

# A list comprehension allows you to generate this same list in just
# one line of code
# A list comprehension combines the for loop and the creation
# of new elements into one line, and automatically
# appends() each new element

# List comprehensions are not always presented to beginners
# But they're included here

squares = [value**2 for value in range (1, 11)]
print(squares)

# Begin to use this syntax beginning by using a name for the list,
# such as squares

# Next, you want to open a set of square brackets and define
# the expression for the values you want to store in the lsit
# Expression here is value**2, which rasises the value to the second power
# Then write a loop to generate the numbers you want to feed into the expression
# close the square brackets

# Use a loop to print numbers 1-20

for number in range(1, 21):
    print(number)

# Make a list of the number from one to one million, and then 
# use a for loop to print the numbers


