# Using arbitrary Keyword arguments
#   Sometimes you'll want to accept an arbitrary numer of arguments, but you
#       won't know ahead of time what kind of information will be passed to the
#           function. In this case, you can write functions that accept
#               as many key-value pairs as the calling statement provides

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field= 'physics')

print(user_profile)

# The definition build_profile expects a first and last name, 
#   and then it allows the user to pass in as many name-value pairs as they want
#       The double asteriks before the parameter **user_info cause Python to 
#           create a dictionary called user_info containing all the extra
#               name-value pairs the user_info just as you would for any 
#                   dictionary

# In the body build_profile(), we add the first and last names to the
#   user_info dictionary b/c we'll always receive these two pieces of 
#       information from the user, and they haven't been placed into the 
#           dictionary yet

# Then we return the user_info dictionary to the function call line