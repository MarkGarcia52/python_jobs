# Many reasons why you should store numbers
# You'll need to keep track of positions of each character
# in a game, and you might want
# to keep track of a player's high score as well

# In data visualization, you'll almost always
# work with sets of numbers, such as temperatures, distances
# population sizes, or latitude and longtitude values, among other
# types of numerical sets

# lists are ideal for storing sets of numbers, and Python provides a variety 
# of tools to help you work efficeintly with lists of numbers

# Using the range() function
# this function makes it easier to generate a series of numbers
# you can use the range() function to print a series such as this:

for value in range(1, 6):


# in this example the range only print from 1-4
# this is a result of the off by one behavior in programming

# range() causes python to start counting at the first value you give it,
# and it stops when it reaches the second value you provide
# the output never contains the end value, which would have been 5

    print(value)

# You can also pass range() only one argument, and it will start the sequence of numbers at 0
# Example range(6) would return the numbers from 0 through 5

# Using range() to make a list of numbers
# If you want to make a list of numbers, you can convert the results of range()
# directly into a list using the list() function
# When you wrap list() around call to the range() function, the output will be a list of numbers

numbers = list(range(1, 6))
print(numbers)