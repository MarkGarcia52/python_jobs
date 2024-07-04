# You can create almost any set of numbers you want to using the range()
# function
# Consider how you might make a list of the first 10 square numbers
# In python, two asteriks (**) represents exponents

squares = []
for value in range(1, 11):
    square = value ** 2 #1
    squares.append(square) #2
print(squares)

#1 Inside the loop, the current value is raised to the second power
# and assigned to the variable square
#2 Each new value of square is then appended to the list of squares
# then the list of square is printed

# To write this code more concisely, omit the temporary variable square
# and append each new value directly to the list

squares.append(value**2) #This is what you would replace #1 and #2 with ^^^^^^
print(square)

# A few python functions are helpful when working with lists of numbers
# You can easily find the minimum, maximum, and sum of a list of numbers:
# in terminal

#>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]
#>>> min(digits)
#0
#>>> max(digits)
#9
#>>> sum(digits)
#45
