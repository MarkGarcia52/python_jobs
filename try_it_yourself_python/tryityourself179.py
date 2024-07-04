# Imported Restaurant

# Using your latest Restaurant Class, sotre it in a module
# Make a separate file that imports Restaurant

# Make an instance and call one of the methods to show that import statement is working
# properly

from tryityourself173 import IceCreamStand

name = IceCreamStand('Jones Ice Cream')
print(name.title_icecreamstand())

# Imported admin

from tryityourself173 import Admin

message = Admin('Hello Admin.', 'ban, and add users', 'Hello Users!')
print(message.greet_admin())
print(message.admin_privileges())
 
