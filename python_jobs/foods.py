# We want to make a separate list of foods that a friends likes
# This friend likes everything in our list so far, so we can create
# their list by copying theirs

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are")
print(friends_foods)


