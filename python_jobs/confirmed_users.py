# Using a loop with lists and dictionaries

# We've worked with one piece of user information at a time.

# We receive user input, and then printed response due to that condition.
# A for loop is effective for looping through a list, but you shouldn't modify a list inside a for loop
# b/c Python will have trouble keeping track of the items in the list
# A while loop with lists and dicitonaries allows you to collect, store, and organize
# lots of inputito examine a report on later

# Moving items from one list to another
# Consider a list of newly registered by unverified users of a website# After we verify these users
# how can we move them to a separate list of confirmed users?

# Start with users to be verified,
#   and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#   Move each verified user  into a list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print(f"\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# We begin with an empty list of confirmed users, and filled in unconfirmed users
#   The while loop runs as long as the list unconfirmed_users is not empty
#       Again the pop method() was used to remove unconfirmed users from the top
#           Candance name was the first removed



