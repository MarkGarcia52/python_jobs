# Because you can't control the order in which your users
# provide their data, your lists may be created in an 
# unpredictable order
# Sometimes you'll want to preserve the original order of your list
# and other times you'll want to change the original order
# Python provides a number of ways to organize your lists, depending on the situation

# Sort() method makes it easy to sort a list
# Say we have a list of cars and want to change the order
# of the list to store them alphabetically
# lets assume all values are lowercase

#cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort()
#print(cars)

# We can never revert to the original order
# You can also sort this list in rever-alphabetical order
# by passing reverse=True to the sort() method

#cars.sort(reverse=True)
#print(cars)

# Again the order is permanently changed

# Sorting a list temporarily with the sorted() function
# To maintain the original order of a list but present it in a sorted order,
# you can use the sorted() function
# This lets you display your list in a particular order, but doesn't affect
# The actual order of your list

#print("Here is the original list:")
#print(cars)

#print("\nHere is the sorted list:")
#print(sorted(cars))

#print("\nHere is the original list again:")
#print(cars)

# Notice the list still exists in its original order.
# The sorted() function can also acept a reverse=True argument
# If you want to display a list in reverese-alphabetical order

# If we originally stored the list of cars in chronological order according to when
# we owned them, we could easily rearrange the list into reverse-chronological
# order

#cars.sort()
#print(cars)

#cars.reverse()
#print(cars)

# Finding the length of a list
# You can quickly find the length of a list by uing the 
# len() function
# You can quickly find the length of a list using the len() function
# The list in this example has four items, so its length is 4
# Use the terminal

# You'll find len() useful when you need to identify the number of aliens
# that still need to be shot down in a game
# determine the amount of data you have to manage in a visualization
# or figure our the number of registered users on a website, among other tasks

# ---------------------------------------------------------------------------------------

# If Statements.

# Involves examining a set of conditions and deciding which action to take
# based on those conditions
# Python's if statement allows you to examine the current state
# of a program and repsond appropriately to that state

# One value should be printed in all upper case
# This code loops through a list of car names and looks
# for value bmw. Whenever the value is 'bmw',  it's printed in upper
# case instead of title case

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional tests.

# Expression that can be evaluated as True or False

# Python uses true false values to decide whether the code in an 
# if statement should be executed

# Checking for equality (terminal)
# "==" checks whether the value of car is'bmw' by using a double equal sign

# equality operator returns True if the values on the left
# and right side of the operator match, and False if they don't

# Testing is case sensitive in the terminal 
# Make sure it's exactly what you state before you check

# car = 'Audi'
# car.lower() = 'audi
# True

# Websites enfore certain rules for the data that users enter in a manner
# similar to this. 
# Ensures everyone has a unique username

# Checking for inequality
# When you want to determine whether two values are not equal,
# you can use the inequality operator (!=)
# If the person did not order anchovies

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

