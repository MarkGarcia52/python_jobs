bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# This isn't the output I want the user to see. We need to learn how to access individual items in a list

print(bicycles[0])

# You can make it more presentable by adding a title() method.

print(bicycles[0].title())

# Index position starts at 0, not 1
# To access say the second item, and fourth item in the list,
# you need to represent there index with a 0 and a 3

print(bicycles[0])
print(bicycles[3])

# If you ask python for an index of -1,
# It will return the last item in the list
# This technique exists for other values as well -2 is second to last and so on.

print(bicycles[-1])

# Pulling the first bicycle from the list and componsing a message using a value.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)