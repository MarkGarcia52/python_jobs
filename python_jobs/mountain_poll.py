# Filling a dictionary with user input
#   You can prompt for as muc hinput as you need in each pass through a while loop

# Let's make a polling program in which each pass through the loop prompts
#   for the participant's name and reponse

# We'll store the data and connect this information with the particular user

responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the responses in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n----Polling Results----")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# First define an empty dictionary (responses) and sets a flag
#   (polling_active) to indicate that polling is active
#       As long as polling_active is True, Python will run code in the while loop

# Users are prompted with name, and favorite mountain
#   That information is tored in the responses dictioanry, and the user is asked
#       To keep polling or not

# If yes, the poll will get running and loop again to re-ask the same questions
