# The while loop unlike to for block,
# runs as long as, or while, a certain condition is true

# The while loop in action

#current_number = 1
#while current_number <= 5:
#    print(current_number)
#    current_number += 1

# Using continue in a loop
# Rather than breaking the loop entirely without executing the rest of its code,
# you can use the 'continue' statement to return to the beginning of the loop,
# based on the result of a conditional test

# Consider a loop that counts from 1 to 10 but prints only the odd numbers in 
# that range

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# we set the current_number to 0 because 0 is less than 10, so Python
# enters the while loop, we increment the current number by 1,
# so current number is 1. 

# The if statment then checks the modulo of current_number and 2.
# if the modulo is 0 (which means current_number is divisible by 2), the
# continue statement tells python to ignore the rest of the loop and return
# to the beginning

# Continue is used so if the loop fails, it will recycle.
# The odd numbers output here because continue tells python to ignore the loop
# and continue to print the numbers even though they aren't divisible by 2
# and equal 0

# If you get rid of continue, python will acknowledge the numbers can be 
# divided by 2 and equal 0, meaning it will output even numbers

# if the current number is not divisible by 2, the rest of the loop is executed
# and python prints the current number

# Avoiding infinite loops

# Every while loop needs a way to stop running so it won't continue to run 
# forever

x = 1
while x <= 5:
    x += 1
    if x % 2 == 0:
        print(x)
# This will not run forever