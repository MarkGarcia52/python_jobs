# Pizza toppings 

# Write a loop that prompts the  user to enter a series of pizza toppings
# until they enter a 'quit' value
# As they enter each topping, print a message saing you'll add that 
# topping to their pizza

#prompt = "Hello there, when you add a topping, I'll repeat it back: "
#prompt += "\nEnter 'quit' to exit the program:"

#message = ""
#while message != 'quit':
#        message = input(prompt)
#        print(f"Adding{message} to your pizza!")
#else:
#        print("Peace out! :)")

# A movie theater charges different ticket prices depending on person's age
# if a person is under the age of 3, the ticket is free

# if person is between 3 and 12, it's $10
# if person over 12, the ticket is $15

# Write a loop in which you ask users their age and tell them cost of ticket

active = True

while active:
    prompt = "Before you watch the movie, how old are you "
    prompt += "\nType 'quit' if you'd like to exit the program: "

    message = input(prompt)

    if message == 'quit':
        print("See you later!")
        break

    if message != 'quit':
        age = int(message)
        if age < 3:
            print("Your ticket is free!")
            active = False
        elif age <= 12:
            print("Your ticket is $10")
            active = False
        else:
            print("Your ticket is $15")
            active = False
    else:
        print("Please enter a numeric value.")




