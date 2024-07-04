# Looping an entire list 
# Looping allows you to take same actoin,
# or set of actions, with every item in a list

# Examples, in a game you may want to move every
# element on the screen at the same time

# In a list of numbers you might want to perform
# the same statistical operation on every element

# Perhaps you want to display each headline from a list
# of articles on a website

# you can use python's for loop
# Using for loops avoids redundancy and shortens the length

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
# It would be a singular print (magician for one at a time)

# It's one of the most common ways a computer automates 
# repitive tasks
# for magicians in magicians:
# tells python to retrieve the first value from the list magician
# and associate it with the variable magician
# then python reads the print() line

# Python prints the current value of magician, which is still 'alice'
# because this list contains more values, Pyton returns the first line of the loop
# print() line

# python prints the current value of magician again, which is now' 'david'
# python repeats the loop with the next value in the list

# Doing more work within a loop
# Lets print a message to each magician
# \n puts a space after each line of text

    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you everyone. That was a great magic show!")

# Forgetting to indent
# always indent the line after the for statement in a loop
# Forgetting to indent additional lines
# Python only cares about the for loop being indented not the print call
# But it will produce a logical error
# It's valid code but it doesn't produce the correct output

# If you accidently indent code that should run after a loop has finished, 
# that code will be repeated once for each item in the list
# There are also colon errors, python will assume its the start of code and 
# give you a traceback error

