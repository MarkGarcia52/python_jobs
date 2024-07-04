# Make a class called restaurant

# the init method should store two attributes
# restaurant_name and cuisine_type

# Make a method called open_resturant() that prints a message indicating
#   the restaurant is open

# print two attributes individually and call both methods

class Restaurants:
    """Create a restaurant class with attributes to describe it"""

    def __init__(describe_restaurant, restaurant_name, cuisine_type):
        """Initialize the attributes within method"""
        describe_restaurant.restaurant_name = restaurant_name
        describe_restaurant.cuisine_type = cuisine_type

    def open_restaurant(describe_restaurant):
        """The restaurant is open."""
        print(f"\n{describe_restaurant.restaurant_name} is now open!")

    def cuisine_restaurant(describe_restaurant):
        """The restaurant serves cuisine."""
        print(f"\nWe serve {describe_restaurant.cuisine_type}!\n")

    def login(self):
        """Create a login attempt starting from 0"""
        self.login_attemps = 0
    
    def increment_login_attemps(self, attempt):
        """Add each attempt after the first attempts"""
        self.login_attemps =+ attempt
        print(f"You have made {attempt} login attempts")

    def reset_login(self):
        """Completely reset all attempts"""
        self.login_attemps = 0
        print(f"Your login attempts have been reset to {self.login_attemps}")

    def show_login(self):
        """Show your login attempts"""
        print(f"You have made {self.login_attemps} login attempts, begin!")

description_place = Restaurants('Tonys Pizza', 'Alfredo')
description_place = Restaurants('Marcos', 'Cheesy Potatoes')
description_place.open_restaurant()
description_place.cuisine_restaurant()

description_place.login()
description_place.show_login()

description_place.increment_login_attemps(2)

description_place.reset_login()


# Make a class called User

# Create two attributes called first_name and last_name, and then create
#      several other attributes that are typically stored in user_profile

# describe_user
# This describes them

# greet_user
# This greets them

class User:
    """Class that creates user and greets them"""

    def __init__(user_profile, first_name, last_name):
        """Initiate the variables within the method"""
        user_profile.first_name = first_name
        user_profile.last_name = last_name
    
    def describe_user(user_profile):
        """This will describe the user with their first and last name"""
        print(f"\nYour first name is: {user_profile.first_name} "
              f"\nYour last name is: {user_profile.last_name}")
    
    def greet_user(user_profile):
        """This will greet the user."""
        print(f"\nHello {user_profile.first_name} {user_profile.last_name}!\n")

class Admin:
    """Admins are special"""

    def __init__(self, title, post, delete, ban):
        """Activate variables"""
        self.title = title
        self.post = post
        self.delete = delete
        self.ban = ban

    def title_show(self):
        """Greet the admin"""
        greetings = self.title
        return greetings

    def show(self):
        """Show all privileges"""
        print(f"\nHello {self.title}")
        print(f"\nYour privileges include: "
              f"{self.post}")
        print(f"\nYou can also {self.delete}")
        print(f"\nAnd {self.ban}")

my_information = User('Mark', 'Garcia')
brother_information = User('Gabe', 'Garcia')
mother_information = User('Jenene', 'Kathryn')

my_information.describe_user()
my_information.greet_user()

brother_information.describe_user()
brother_information.greet_user()

mother_information.describe_user()
mother_information.greet_user()

accomodations_admin = Admin('Admin', 'Creating posts', 'Delete posts',
                            'Ban users')
accomodations_admin.show()