# Make a list called sandwich_orders and fill it with the names of various sandwiches
# Then make an empty list called finished_sandwiches

# Loop through the list of snawich orders and print a message for each order
# such as I made your tuna sandwich
# As each sandwich is made, move it to finished sandwhich

# After all sandwiches have been made, print a message listing each sandwich that was made

sandwich_orders = ['turkey', 'chicken', 'vegan', 'turkey', 'brisket', 'beef', 'chicken', 
                   'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

message = "Unfortunately we are out of Pastrami!\n"
print(message)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:

    current_sandwich = sandwich_orders.pop()

    print(f"You would like a: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("----Poll Results for each sandwich order----")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
    active = False

# No Pastrami
#   Using the list sandwich_orders from last exercise, make sure
#       the sandwich 'pastrami' appears in the list three times
#           Add code near the beginning of your program to print

# A message saying the deli has ran out of pastrami and then use a while
#   loop to remove all occurrences of 'pastrami' from sandwich_orders

# Dream Vacation
#   Write a program that polls users about their dream vacation
#       Write a prompt similar to if you could visit one place in the world,
#           Where would you go?

# Include a block of code that prints the results of the poll

responses = {}

polling_active = True

while polling_active:
    name = input("What's your name? ")
    response = input("What is your dream vacation? ")

    # Store the responses.
    responses[name] = response

    # Repeat input.
    repeat = input("Would you like to continue the poll (yes/no)")
    if repeat == 'no':
        polling_active = False

print("---Polling Results---")
for name, response in responses.items():
    print(f"{name} would like to travel to: {response}")


# Brand of tv

responses = {}

polling_active = True

while polling_active:
    name = input("What's your Name: ")
    response = input("What brand of tv do you wish to buy: ")

    responses[name] = response

    repeat = input("Would you like to continue this poll (yes/no): ")
    if repeat == 'no':
        polling_active = False

print("---TV Polling Results---")
for name, response in responses.items():
    print(f"{name} would like a {response} TV for Christmas")