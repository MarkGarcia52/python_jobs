# Checks if a person is under the age of 4
# Checks if person is under the age of 18
# If both fail, person pays $40, which means they are above both ages
# 4 and 18.

age = 4
if age < 4:
    print("\nYour admission cost is $0")
elif age < 18:
    print("\nYour admission cost is $25")
else:
    print("\nYour admission cost is $40")

# Rather than printing the admission price within the if-elif-else block,
# it would be more concise to set just the price inside the if-elif-else chain
# and have a single print() call that runs after the chain has been evaluated


if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

# Using multiple elif blocks

# You can use as many as you'd like.
# The amusement park were to implement a discount for seniors,
# you could add one more conditional test to the code to determine whether someone 
# qualifies for the senior discount

#elif age <65:
    #price = 40

# 
