# Any statement that tells the user to enter should work.

#name = input("Please enter your name:")
#print(f"Hello, {name}!")

# Sometimes you'll want to write a prompt that's longer than one line
# You might want to tell the user why you're asking for certain input

# You can assign your prompt to a variable and pass that variable to the input() function
# This allows you to build your prompt over several lines, then write a clear input()

#prompt = "If you share your name, we can personlize the messages you see."
#prompt += "\nWhat is your first name?"

#name = input(prompt)
#print(f"Hello, {name}!")

# Using int() to accept numerical input

# When you use the input() function, Python interprets everything the user enters as a string
# >>> age = input("How old are you?")
#How old are you?21
#>>> age >= 18
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: '>=' not supported between instances of 'str' and 'int'

# When you try to use the iunput to do a numerical comparison
# Python produces an error b/c it can't compare a string to an integer:
# The string 21 that's assigned to age can't be compared to numerical
# value 18

# We can resolve this bu using the int() function, which converts input string to a numerical
# value

#>>> age = input("How old are you?")
#How old are you?21
#>>> age = int(age)
#>>> age >= 18
#True

# Defining a function

# Here's a simple function named gree_user() that prints greeting

#def greet_user():
#    "Display a simple greeting. """
#    print("Hello!")

#greet_user()

# Def informs python that I'm using a function
#   first line uses this key word which tells Python that you're defining a function

# This is the function definition, which tells Python the name of the function and
#   if applicable, what kind of information the funciton needs to do its job

# The parenthesis holds the information
#   The name of the funciton is greet_user(), and it needs no information to do its job
#       so its parenthesis are empty

# The definition ends in a colon

# Any indented lines that follow def: make up the body of the function
# The text on the second line is comment called a docstring, which describes
#   what the function does. When Python generates documentation for the functions in a program
#       it looks for a string immediately after the functions definition
#           These strings are usually enclosed in triple quotes, which lets you write multiple lines

# The print("Hello") is the only actual line of code in the body of the function

# when you want to use this function, you have to call it
#   A function call tells python to execute the code in the function
#       To call a function, you write the name of the function, followed by necessary info in parenthesis
#           Since no information is needed, we just use empty ()


# Passing information to a function
#   If you modify the function greet_user() it can greet the user by name

# By replacing () with (username) you allow the function to accept any value of username you specify
#   The function now expects you to provide a value for username you specify

def greet_user(username):
    "Greeting the user. """
    print(f"Hello {username.title()}!")

greet_user('Mark')

# Argument and parameters
#   The variable username is an example of a parameter
#       A piece of information that functions needs to do its job
#           'mark' in greet_user('mark') is an argument 

# An argument is a piece of information that's passed from a function call to a
#   function

# When we call a function, we place the value we want the function to work with in parenthesis
#   In this case, the argument 'mark' was passed to the function greet_user(), and the value
#       was assigned to the parameter username