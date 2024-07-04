# Imagine an alien was just shot down in game.
# Create a variable called alien_color and assign it a value
# of 'green', 'yellow', or 'red'.


#if, elif, else
# Used if, and else

alien_color = ['red', 'green', 'yellow']

alien_color = 'red'
if alien_color == 'green':
    print("You've just earned 5 points!")
elif alien_color == 'red':
    print("You've just earned 10 points!")
else:
    print("You've just earend 15 points!")

# Determine someone's title based off of their age.

stage_life = 20
if stage_life < 2:
    print("You're a baby!")
elif stage_life >= 2 and stage_life < 4:
    print("You are a toddler")
elif stage_life >= 4 and stage_life < 13:
    print("You are a kid")
elif stage_life >= 13 and stage_life < 20:
    print("You are a teenager")
elif stage_life >= 20 and stage_life < 65:
    print("You are an adult")
else:
    print("You are an elder!")

# Make a list of favorite fruits, and then write a series of indpendent if statements
# That checks for certain fruits in your list

favorite_fruits = ['banana', 'grape', 'apple']
if 'banana' in favorite_fruits:
    print("You really like Bananas!")
if 'grape' in favorite_fruits:
    print("You really like Grapes!")
if 'apple' in favorite_fruits:
    print("You really like Apples!")
if 'tangarine' in favorite_fruits:
    print("You really like Tangarines!")