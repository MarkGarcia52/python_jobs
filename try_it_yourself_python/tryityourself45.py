# Seeing the world
# Think of at least five in the world you'd like to visit

# Store the locations in the list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don't worry about printing the list neatly:
# just print it as a raw Python list

world = ['France', 'Colorado', 'Germany', 'Japan', 'Winsconsin']
print(world)

# Use sorted() method to print list alphabetically without modifying

print(sorted(world))

# Print the list to ensure it's still in original order

print(world)

# Reverse-alphabetical order

reversed_list = sorted(world, reverse=True)
print(reversed_list)

# Reverse() method twice to change it back to original since
# this method is permanent

print(world)
world.reverse()
print(world)
world.reverse()
print(world)

# Sort() list alphabetically, permanently

sorted_list = world.sort()
print(world)
sorted_list = world.sort(reverse=True)
print(world)