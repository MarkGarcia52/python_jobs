# A dictionary in a dictionary
# You can nest a dictionary inside another dictionary, but your code can get
# complicated quickly when you do

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'mark',
        'last': 'curie',
        'location': 'paris',
    },
    
}

for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
                                        
# We define a dictionary called users with two keys
# Each key has a user
# Values associated with that key are first, last, location

# Then we loop the users dictionary
# Python assigns each key to the variable username
# the dictionary associated with each username is assigned to variable 
# user_info

# Then we start to access the inner dictionary
# The variable user_info which contains the dictionary of user info.
# has three keys

# we use each key to generate nealty formatted text