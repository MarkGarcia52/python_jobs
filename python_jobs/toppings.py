# If someone requests a two topping pizza
# you'll need to be sure to include both toppings on their pizza

#requested_toppings = ['mushrooms','extra cheese']

#if 'mushrooms' in requested_toppings:
    #print("Adding Mushrooms")
#if 'extra cheese' in requested_toppings:
    #print("Adding Extra Cheese")
#if 'pepperonni' in requested_toppings:
    #print("Adding Pepperonni")

#Print("\nFinishing up your pizza now!")

# Because every condition is evaluated in this test, both
# mushrooms and extra cheese are added to the pizza

# if elif, the tests would not stop running after only one test passes

# Python doesn't run any tests beyong the first test that passes
# the if-elif-else chain

# In summary, if you want one block of code use elif
# If you want more than one, use a series of independent if statements

# You can do some good work combining if statements with lists
# You can wathc for special values that need to be treated differently
# You can manage changing conditions, such as availability
# of certain items in a restaurant throughout a shift

# Checking for special items

# Using a loop to announce each topping

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers': #(1)
        print(f"Sorry, but we are out of green peppers right now.") #(1)
    else: #(1)
        print(f"Adding {requested_topping} to your order!")

print("\nFinished making your pizza!")

# But what if the pizzera runs out of green peppers? (1)

# It's conducive to check to see if the list is empty first. (2)

request_toppins = []

if request_toppins:
    for request_toppin in request_toppins:
        print(f"Adding {request_toppin}")
    print("Finsihed making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")

# Using multiple lists

# People will ask for just about anything.
# Especially when it comes to pizza toppings
# Unusual toppings request

available_toppings = ['mushrooms', 'olives', 'green pepppers',
                    'pepperonni', 'pineapple', 'extra cheese']

requested_tops = ['mushrooms', 'french fries', 'extra cheese']

for requested_top in requested_tops:
    if requested_top in available_toppings:
        print(f"Adding {requested_top}")
    else:
        print(f"Sorry, we don't have {requested_top}.")

print("\nFinished making your pizza!")
