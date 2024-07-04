# Slicing a list
# You specify the index of the first and last elements
# You want to work with

# As with the range() function, Python stops one item before the second idex
# you specify
# To output the first three elements in a list, you would
# request indices 0 through 3, which would return elements 0, 1, and 2

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# This code prints a slice of the list
# The output retains the structure of the list, and includes
# the first three players in the list

# You can generate a subset of a list
# If you want the second, third, and fourth items in a list, you would start the slice at index 1
# and end it at 4

print(players[1:4])

# If you omit the first index in a slice,
# Python automatically starts your slice at the beginning of the list:

print(players[:4])

# Similar syntax works if you want to slice that includes the end of a list

print(players[2:])

# Recall negative index returns an elemtn a certain distance from teh end of a list;
# therefore, you can output any slice from the end of a list

print(players[-3:])

# Looping through a slice
# You can use a slice for loop if you want to loop through
# a subset of elements in a list
# We loop through the first three players and print their names as part of a 
# simple roster

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# When you're creating a game, you could add a player's final
# score to a list every time that player finishes playing
# You could then get a player's top three scores
# by sorting the list in decreasing order and taking a slice that includes
# just the first three scores

# When you're working with data you can use slices to process your data in chunks
# of a specific size

# Or when building a web application, you could use slices to display information
# in a series of pages with an appropriate amount of infomration on each page

# Copying a list
# You'll want to start an exisiting list and make an entirely new list
# based on the first one
# Let's explore how copying a list works and examine on esituation in which
# copying a list is useful

# To copy, you can make a slice that includes the entire original list by omitting
# the first index and the second index
# This tells python to make a slice that starts at the first item
# and ends with the last itme
