# Exceptions to manage errors

# Exceptions are handled with try-except blocks
# These ask Py to do something, but it also tells Python what do if an 
# exception is raised

# Handling the ZeroDivisionError Exception

# print(5/0)

# Python creates a traceback

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# If the code in the try block works, PYthon skips over the except blocks
    # If the code in the try block causes an error, PYthon loos for an except
        # block whose error matches the one that was raised, and runs the code
            # in that block.

# Using exceptions to prevent crashes

print("Give me two numbers and I'll divide them")
print("Enter a 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break

    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can divide by 0")
    else:
        print(answer)

# The Else Block

# The only code that should go in a try block is code that might
    # cause an excpetion to be raised

