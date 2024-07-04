# when one number is divisible by another number, the remainder is 0
# so the modulo operator always returns 0
# You can use this to determine whether a number is even or odd

number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")