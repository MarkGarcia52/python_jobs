import pizza

pizza.make_pizza(16, 'pepperonni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# When Python reads this file, the line import pizza tells Python to open 
#   the file pizza.py and copy all the functions from it into this program

# You don't actually see code copied over to the files, 
#   B/c Python copies the code behind the scenes, just before program run

# To call a function from an imported module, enter the name of the module
#   you imported, pizza, followed by the name of the function, make_pizza(),
#       separated by a (.)

# This code produces the same output if you didn't import the module

# Importing specific functions
#   Here's a general approach:
#       from module_name import function_name

# You can import as many functions as you want:
#   from module_name import function_0, function_1 etc

# From pizza import make_pizza()
#   This is what we would import if we only wanted the make_pizza function

# Using as to Give a function an Alias
#   If the name of the function you're importing might conflict with an 
#       exisiting name in your program, or if the function name is long,
#           you can use a short, unique alias

# Alias:
#   Alternate name similar to a nickname for the function
#       You'll give the function this special nickname when you import the 
#           function.

# Here we give make_pizza the alias mp()

from pizza import make_pizza as mp

mp(16, 'pepperonni')
mp(12, 'mushrooms', 'green peppers', 'chedda')

# General syntax for alias:
#   from module_name import function_name as fn

import pizza as p

# Import all modules

from pizza import *





























