# Write a function that accepts a list of items a person wants on a sandwich

# The function should have one parameters that collects as many items as 
#   possible.

# It should print a summary of the sandwich that's being ordered 
#   Call the function three times, using a different number of arguments
#       each time

def sandwich_order (*inside_sam):
    """Print a sandwich order"""
    print(f"Making your sandwich with: {inside_sam}")

sandwich_order('turkey', 'cheese', 'ham')

# User profile
#   Start with a copy of user_profile from page 148

#   Build a profile of yourself by calling build_profile(), using
#       your first and last names and three other key -value pairs to describe
#           you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('mark', 'garcia',
                             university='toledo',
                             year= 'sophomore',
                             field= 'IS')

print(user_profile)

# Cars 
#   Write a function that stores information about a car in a dictionary
#       The function should always receive a manufacturer and model name
#           It should htne accept an arbitrary number of keyword arguments

def cars(manufacturer, color, tow_package, **traits):
    """Output manufacturer and model name from dictionary"""
    traits['color'] = color
    traits['towing'] = tow_package
    traits[manufacturer] = manufacturer
    return traits

all_traits = cars('subaru',
              color='blue',
              tow_package='Yes')

print(all_traits)

