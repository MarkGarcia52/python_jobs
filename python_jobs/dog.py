# Object-oriented programming is one of the most effective approaches to
#   writing software. In object-oriented programming you write classes that 
#       represent real-world things and situations, and you create objects
#           based on these classes.

# When you write a class you define the general behavior that a whoel category
#   of objects can have.

# Making an object from a class is called instantiation
#   and you work with instances in a class

# We'll store classes in modules and import classes written by other
#   programmers into my program files

# Creating and using Classes

# You can model almost anything using classes
#   Lets write a simple class, dog, that represtns a dog

# This class will tel lPython how to make an object representing a dog

#   Each instance created from the Dog class will store a name and an age, 
#       and we'll give each dog the ability to sit() and roll_over():

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# We first define a class Dog

# By convention, capitalized names refer to classes in Python
#   There are no parenthesis in the class definition b/c we're creating this
#       this class from scratch

# _Init()_ method
#   A function that's part of a class is a method
#       Everything about a function applies to methods as well
#           The way we'll call methods is different from previous

# _init()_ method is a special method Python runs automatically whenever we
#   create a new instance based on the Dog class
#       This method has two leading underscores and two trailing underscores
#           A convention that helps prevent Python's default method names from
#               conflicting with method names.


# We definied init with 3 parameters: self, name, and age
#   The self parameter is required in the method definition, and 
#       it must come first, before the other parameters

# It must be included b/c when Python calls this method later (to create
#   an instance of dog) the method call with automatically pass the self 
#       argument

# Every method call associated with self will automatically pass the self 
#   argument, which is a reference to the instance itself; it gives the 
#       individual instance access to the attributes and methods in the class

# Whenever we want to make an instance from the Dog class, we'll provide
#   values for only the last two parameters, name and age


# The two variables defined in the body of the _init()_ method each have 
#   prefix self. Any variable prefixed with self is available to every
#       method in the class, and we'll also be able to access these variables
#           through any instance created from the class

# self.name = name takes the value associated with the parameter name and
#   assigns it to the varibale name, which is then attached to the instance
#       being created

# Variables that are accesible through instances like this are called attributes
#   For now sit() and roll_over() don't do much

# They simply print a message

# If this class was part of a computer game, these methods would contain code
#   to make an animated dog to sit and roll over.

#   If this class was written to control a robot, these methods would direct 
#       movements that cast a robotic dog to sit and roll over


# Making an instance from a class

# Think of a class as a set of instructions to make an instance
#   The dog class is a set of instructions that tells Python how to make 
#       an individual instance representing specific dogs

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.") #(1)
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}") #(30)
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()

# When Python reads this line, it calls the _init_() method in Dog
#   within the arguments 'Willie' and 6

# The _init_() method creates an instance representing this particular dog and
#   sets the name and age attributes using the values provided
#       Python then returns an instance representing this dog

# We assign this instance to the variable my_dog

# To access attributes of an instance, you use dot notation

# We access the value of my_dog's attribute name (1)

# Calling Methods

# After we create an instance from the class Dog, we can use dot notation to
#   recall any method defined in Dog. Let's make our dog sit and roll over


my_dog.sit()
my_dog.roll_over()

# When python reads this
#   It looks for the method sit() in the class Dog and runs that code

# Creating multiple instances (30)


