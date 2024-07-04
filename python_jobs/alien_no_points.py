# Using get() to access values

# Using keys in square brackets to retrive a value you're interested in
# from a ditionary might cause one potentional problem:
# if they key you ask for doesn't exist: you'll get an error

# The get() method requires a key as a first argument
# As a second optional argument, you can pass the value to be returned if the 
# key doesn't exist

alien_0 = {'color': 'green', 'speed': 'medium'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# If the key 'points' exists in the dictionary, you'll get the corresponding val
# ue. If it doesn't you get the default value
# In this case points doesn't exist so there is text.