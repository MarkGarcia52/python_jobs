# Dictionaries

# Connect pieces of related information
# Modify that information
# Can store lots of information

# Simple dictionary
# Stores information about particular alien

# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# Working with dictionaries

# A dictionary is a collection of key-value pairs

# Each key  is connected to a value, this can be a number, a string, a list
# or even another dictionary

# You can use any object that you can create in Python as a value in a
# dictionary

# its wrapped in braces ({})
# a key-value pair is alien_0 = {'color': 'green'}

# To get the value associated with that key
# you print(alien_0['color'])

# Now you can access either the color or the point value of alien_0
# If a player shoots down this alien, you can loop up how many points they
# should earn using code like this:

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# Add new key-value pairs
# Dictionaries are dynamic structures, and you can add new key-value pairs
# to a dicitonary at this time

# To add a new key-value pair, you would give the name of the dictionary
# followed by new key in square brackets, along with the new value

# Let's add two new pieces of information to the alien_0 dictionary
# The aliens x- and y- coordinates at any time

# This will help us display the alien at a particular position on the screen
# Let's place the alien on the left edge of the start upper-left edge of screen
# by setting the x-cooridinate to 0 and 25 pixels from top

# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# you will see elements in the same order they were added to the dictionary

# Starting with an empty dictionary
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# Modifying values in a dictionary

alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}")
alien_0 = {"color": "yellow"}
print(f"The alien is now {alien_0['color']}")

# For a more intersting example, let's track the position of an alien
# that can move at different speeds
# We'll store a value representing the alien's current speed and then
# use it to determine how far to the right the alien should move

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old poisition plus the increment
alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing key value pairs
# When you no longer need a piece of information that's stored in a dictionary
# You can use the del statement to completely remove a key-value pair
# All del needs is the name of the dictionary and the key that you want to
# remove

alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

# Nesting

# Somtimess you'll want to store multiple dictionaries in a list, or a list
# of items as a vlaue in a dictionary

# A list of dictionaries

# The alien_0 dictionary contains a variety of information about one alien.
# but it has no room to store information about a secon alien

# How can you manage a fleet of aliens?
# Each alien becomes a dictionary

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# A more realistic example would involve more than three aliens with code that
# automatically generates each alien
# You can use range to do this for you

# Make an empty list for storing aliens.

aliens = []

# Make 30 green aliens.
for alien_number in range(30):  # 1
    new_alien = {"color": "green", "points": 5, "speed": "slow"}  # 2
    aliens.append(new_alien)  # 3

# Show the first 5 aliens
for alien in aliens[:5]:  # 4
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# 1 Begins with an empty list to hold all of the aliens that will be created.
# The range() function...

# 2 ...Returns a series of numbers, which just tells python how many times we
# want the loop to repeat. Each time the loop runs, we create a new alien..

# 3 and then append each new alien to the list of aliens

# 4 We use a slice to print the first five aliens

# And finally we print the length of the list to prove we've actually generated
# a full fleet of aliens

# Imagine that one aspect of a game has some aliens changing color
# and moving faster as the game progresses
# When its time to change color of the aliens, we could do this:

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

    # You could expand this using elif, turning yellow aliens into red, fast aliens
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["color"] = "fast"
        alien["points"] = 15


# Show the first five aliens
for alien in aliens[:5]:  # 4
    print(alien)
print("...")

# You could expand this using elif, turning yellow aliens into red, fast aliens
