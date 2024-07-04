# Checking whether a Value is Not in a List
# It's importantt o know if a value does not appear in a list
# You can use keyword not in this situation

# Consider a list of banned users

banned_users = ["andrew", "carolina", "david"]
user = "andrew"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish!")

# Boolean Expressions

# Just another name for a conditional test
# Boolean value is either true or false
# Just like the value of a conditional expression after it has been evaluated

# Are often used to keep track of certain conditions, such
# as whether a game is running or whether a user can edit certain
# content on a website:

game_active = True
can_edit = False
