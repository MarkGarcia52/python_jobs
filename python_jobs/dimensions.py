# Lists work well for storing collections of items
# that can change throughout the life of a program

# The ability to modify lists is important when you're working with 
# a list of users on a website or a list of characters in a game

# Sometimes you'll want to create a list of items that cannot change
# Tupels allow you to do just that

# Values that cannot not change are immutable
# An immutable list is called a tuple

# Defining a tuple

# A tuple looks like a list except you use parentheses instead of square brackets
# Once you define the tuple, you can access individual elements by
# using each item's idex, just as you would for a list

# Example, if we have a rectangle that should be a certain size, 
# We can ensure that its size doesn't change by putting the dimensions into 
# a tuple

dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# We can't alter this or we'll get a syntax

# Looping through all values in a tuple
# You can loop over all the values in a tuple using for

#for dimension in dimensions:
    #print(dimension)

# Although you can't modify a tuple
# you can assign a new value to a variable that
# represents a tuple

# Example, if we wanted to change
# the dimensions of this rectangle, we could redefine the entire tuple

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# When compared with lists, tuples are data strucutures
# Use them when you want to store a set of values that should not
# be changed through-out the life of a program




