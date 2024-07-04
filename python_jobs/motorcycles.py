# Say we have a list of motorcycles and the first item is 'honda'
# To change an element, use the name of the list followed by the index of the element,
# you want to change, and then provide the new valueyou want that item to have.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Appending Elements to a list
# When you append an item to a list, the new element is added to the end of the list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# The append() method maes it easy to build lists dynamically
# You can start with an empty list and then add items to the list,
# using the append() series

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yahama')
motorcycles2.append('suzuki')
print(motorcycles2)

# To put users in control, start by defining an empty list that,
# will hold user's values, then append each new value added to the list

motorcycles3 = ['honda', 'yamaha', 'suzuki']
motorcycles3.insert(0, 'ducati')
print(motorcycles3)

# You'll want to remove an item or set from a list
# When a player shoots an alien down from the sky, 
# you'll most likely wnat to remove it from the list of active aliens.
# Or when a user decides to cancel their account on web application,
# you'll want to remove that user from the list of active users.
# You can do this when you know the items index.

motorcycles4 = ['honda', 'yahama', 'suzuki']
print(motorcycles4)

del motorcycles4[0]
print(motorcycles4)

# Removing an item using the pop() method.
# You'll want to use the value of an item after you remove it from a list.
# You might want to get the x and y position of an alien that was shot down,
# so you can draw an explosion at that position
# You might want to remove a user from a list of active members and then add
# them to the inactive list of members

# pop() removes the last item in a list, but it lets you work with that 
# item after removing it
# pop comes from thinking of a list as a stack of items and popping one item off
# the top of the stack.

motorcycles5 = ['honda', 'yahama', 'suzuki']
print(motorcycles5)

popped_motorcycle5 = motorcycles5.pop()
print(motorcycles5)
print(popped_motorcycle5)

# The output shows that the value 'suzuki' was removed from the end
# of the list and is now assigned to the variable popped_motorcycle5:

# Why might the pop() be useful?
# Imagine that the motorcycles in the list are stored in order, according to
# when we owned them
# In this case, we can use the pop() method to print a statement about
# the last motorcycle we bought

last_motorcycle = motorcycles5.pop()
print(f"The last motorcycle I owned was a {last_motorcycle.title()}")

# Using the pop() method to remove an item from any position in a list
# by including the index
# Remember when you use this method, the item you work with,
# is no longer stored in the list

first_owned = motorcycles5.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# If you're unsure whehter to use the del statement or the pop() method,
# here's a simple way to decide: 
# When you wasnt to delete an item from a list and not use it in any way
# use the del statement
# if you want to use an item as you remove it,
# use the pop() method

# Removing an item by value
# Sometimes you don't the position of the value you want to remove
# from a list
# If you only know the vlaue of the item you want to remove,
# you can use the remove() method

motorcycles6 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles6)

motorcycles6.remove('ducati')
print(motorcycles6)

# You can also use this method remove()
# and come up with a reason of why you removed it

motorcycles7 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles7)

ducati_expensive = 'ducati'
motorcycles7.remove(ducati_expensive)
print(motorcycles7)
print(f"\nA {ducati_expensive.title()} is too expensive for me")

# Index Errors when working with lists
# Python can't find your index requested
# Keep in mind, if you want to access the last item in your list
# the index is -1

print(motorcycles[-1])

