# Make several dictionaries
# Each represents a different pet (dictionary)
# Include the kind of animal, the owners name
# Store these in list called pets

pets = {
    'jocko': {
    'type': 'laborador',
    'owner': 'mark'
    },

    'oscar': {
    'type': 'chorkie',
    'owner': 'gabe'
    }
}

for pet, pet_info in pets.items():
    print(f"\nPet Name: {pet.title()}")
    type_dog = pet_info['type']
    owner_name = pet_info['owner']

    print(f"{pet.title()} is {owner_name.title()}'s dog.")
    print(f"He's a {type_dog.title()}!")

# Favorite Places
# Think of three places to use as keys 
# and store one to three fav places for each person

# Loop dictionary and print each person's name with favorite places!

favorite_places = {
    'mark': {
    'city': 'ny',
    'mountains': 'colorado',
    'overseas': 'japan'
    },

    'gabe' : {
    'city': 'rhode island',
    'mountains': 'north dakota',
    'overseas': 'germany'
    }
    
}

for name, locations_items in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:") 

    city_item = locations_items['city']
    moutain_item = locations_items['mountains']
    overseas_item = locations_items['overseas']

    print(f"{city_item.title()}")
    print(f"{moutain_item.title()}")
    print(f"{overseas_item.title()}")
    
# Dictionary with two people's 3 favorite numbers

favorite_numbers = {
    'mark': {
    'ranked one': 52,
    'ranked two': 7,
    'ranked three': 9

    },
    'gabe': {
    'ranked one': 50,
    'ranked two': 6, 
    'ranked three': 90
    }
}

for name, number_values in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")

    ranked_one = number_values['ranked one']
    ranked_two = number_values['ranked two']
    ranked_three = number_values['ranked three']

    print(f"\t{ranked_one}")
    print(f"\t{ranked_two}")
    print(f"\t{ranked_three}")
    