# Make a list of five or more usernames, including the name 'admin'
# Imagine you are writing code that will print a greeting to each user after 
# they log into a website
# Loop through the list, and print a greeting to each user

# If the username is 'admin', printa  special greeting, such Hello admin,
# would you like a status report?
# If anyone else, write "Hello Jaden, thank you for logging in again."

user_names = ['admin', 'jaden', 'candies', 'vans','joemama']
for user_name in user_names:
    if user_name != 'admin':
        print(f"Hello {user_name.title()}"
              " and welcome back, thanks for logging in!")
    else:
        print(f"Hello {user_name.title()}, would you like a status report?")
else:
    print("We need to find some users!") # this works when list is empty

# Checking usernames, no copycats
# Ensure everyone has a unique username

current_users = ['Josh', 'John', 'Kendrick', 'Lamar', 'Jocko']
new_users = ['Josh', 'John', 'Oscar', 'Bear', 'Peyton']

# Convert all elements to lowercase for case-sensitive comparison
current_users_lower = [user.lower() for user in current_users]
new_users_lower = [user.lower() for user in new_users]

for new_user_lower in new_users_lower:
    if new_user_lower in current_users_lower:
        print(f"{new_user_lower.title()}, has already been taken.")
    else:
        print(f"Hello and welcome {new_user_lower.title()}!")

# Ordinal numbers indicate their position in a list, such as 1st and 2nd
# Most ordinal numbers end in th, except 1, 2, 3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number < 2:
        print(f"{number}st place!")
    elif number < 3:
        print(f"{number}nd place!")
    elif number < 4:
        print(f"{number}rd place!")
    else:
        print(f"{number}th place!")

    








