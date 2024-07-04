# Using break to exit a loop
# To exit loop immediately without running any remaining code in the loop
# regardless of the rsults of any conditional test, use the break statement

# Break statement directs the flow of your program; you can use it to control
# which lines of coe that you want it to, when you want it to

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished)"

while True:
    city = input(prompt)

    if city == 'quit':
        break

    else:
        print(f"I'd love to go to {city.title()}!")