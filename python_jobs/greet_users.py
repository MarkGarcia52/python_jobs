# You'll find it useful to pass a list to a function, whether it's a list
#   of names, numbers, or more complex objects, such as dictionaries
#       When you pass a list to a function, the function gets direct
#           access to the contents of the list. Lets use functions
#               to make working with lists more efficient

# Say we have a list of users we want to print a greeting to each

# This sends a list of names to a function called greet_users(), which greets
#   each person in the list individually

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# We define greet_users() so it expects a list of names, which is assigned to 
# the parameter names

# The function loops through the list it receives and prints a greeting to each
#   user. Outside of the function, we define a list of users and then pass
#       the list of usernames to greet_users() in the function call