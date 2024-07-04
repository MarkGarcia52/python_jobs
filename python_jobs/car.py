# You can use classes to represent many real-world situations
#   Once you write a class, you'll spedn most of your time working with 
#       instances created from that class

# One of the first tasks you'll want to do is modify the attributes associated
#   with a particular instance

# The Car Class

# Our class will store information on what kind of car we are working with

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #(1)

    def get_descriptive_name(self): 
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self): #(1)
        """Print statement showing cars mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        # self.odometer_reading = mileage
    
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('Subaru', 'Outback', '2024')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_new_car = Car ('Audi', 'A4', '2024')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(22) # (2) scroll to top
my_new_car.read_odometer()

my_new_car.read_odometer() #(1)

# We define a method get_descriptive_name
# So we can neatly print out the description of the vehicle into one string
# This will spare us from having to print each individual attribute


# Setting a default value for an Attribute

# When an instance is created, attributes can be defined without being passed
#   in as parameters
#       These attributes can e defined in the __init__() method, where they are
#           assigned a default value

# We can add odometer_reading that always starts with a value of 0 #(1)

# Modifying Attribute Values

# You can change an attribute's value in three ways:

# Change the value directly through an instance (1)
# Set the value through a  (2)
# Increment the value (add a certain amount to it) through a method (3)

# (1)

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# We use dot notation to acces the car's odometer_reading attribute, and set
# its value directly

# (2)

# Look up top in the Class Car

# The only modification to Car is the additiion of update_odometer()
# This method takes in a mileage value and assigns to self.odometer_reading
# Using the my_new_car instance, we call update_odometer() with 23
# as an argument 

# (3)

# To additional work every time the odometer reading is modified
# Lets add a little logi c to make sure no tires to roll it back 

# Look up top in the Class Car