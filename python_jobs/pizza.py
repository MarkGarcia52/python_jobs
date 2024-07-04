# A list in a dictionary

# Rather than putting a dictionary inside a list, it's sometimes useful to put
# a list inside a diciotnary

# consider how you might describe a pizza that someone is ordering

# If you were to use only a list, all you could really store
# is the list of the pizza's toppings

# With a dictionary, a list of toppings can be just one aspect of the pizza you
# describing

# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


# Passing an arbitrary number of arguments

# Sometimes you won't know, ahead of time how many arguments a function
#   needs to accept. Fortunately, Python allows a function to collect an arbi
#       trary number of arguments from the calling statement

# For example, consider a function that builds a pizza
#   It needs to accept a number of toppings, but you can't know ahead of time
#       how many toppings a person will want. The function in the following
#           example has one parameter *toppings, but this parameter
#               collects as many arguments as the calling line provides:

def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperonni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# * in the parameter name tells Python to make a tuple called toppings, 
#   containing all the values this function receives
#       The print() call in the funiction produces output showing that Python
#           can handle a function call with one value and a call with three
#               values. It treats the different calls similarly.

# Now we can replace the print() call with a loop that runs through the list of 
#   toppings and describes the pizza being ordered:

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('mushrooms')
make_pizza('sausage', 'pineapple', 'bacon')

# Making positional and arbitrary arguments
# If you want a function to accept several different kinds of arguments, the
#   parameter that accepts an arbitrary number of arguments must be placed last
#       in the function definintion. Key word arguments first, and
#           collects any remaining arguments after

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza that with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

# Storing your functions in Modules
#   One advantage of functions is the way they separate blocks of code
#       from your main program.
#           When you use descriptive names for your functions, your programs
#               become much easier to follow.

# You can store functions in a separate file called a module and then importing
#   that module into your main program

# An import statement tells python to make the code in a module available
#   in the currently running program file.

# Let's make a module that contains the function make_pizza()
#   To make this module, we'll remove everything from the fill pizza.py except
#       the function make_pizza()

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}- pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")