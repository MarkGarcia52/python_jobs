# Modifying a list in a function

# When you pass a list to a function, the function can modify the list
#   Any changes made to the list inside the function's body are permanent,
#       allowing you to work efficiently even when you're dealing with large
#           amounts of data

# Consider company making 3D printed models of designs that users submit
#   Desings that need to be printed are stored in a list, and after being
#       printed they're moved to a separate list
#           The following code does this without using functions

# Start with some desings that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each desing, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# As long as desigds remains unprinted_designs, the while loop simluates 
#   printing each desing by removing a design from the end of the list
#       storing it in current_design, and displaying a message that the current
#           desingn is being printed

# Preventing a function from modifying a list
#   Say that you start with a list of unprinted designs and wiret a function
#       to move them to a list of completed models

# You may decide even though you've printed all the designs, you want to keep
#   the original list of unprinted desings for your records

# Because the list is empty after the move

# You can send a copy of a list to a function like this:
# function_name(list_name[:])

# So if you wanted to keep unprinted_designs in both parameters,
# print_models(unprinted_designs[:], completed)

# Display all completed models
print("\nThe following models have been printed.")
for completed_model in completed_models:
    print(completed_model)