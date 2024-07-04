from name_function import get_formatted_name

def test_first_last_name(): #1
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin') #2
    assert formatted_name == 'Janis Joplin' #3

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'

#1 We first import the function that we want to test: get_formatted_name()
    # Then we define a test function in this case test_first_last_name()
    # This is longer b/c test needs to be in the first part, followed by an _
    # Any function that starts with test_ will be discovered by pytest

    # Test names should be longer and more descriptive than typical function names

#2 We'll call the function we are testing
    # Here we call get_formatted_name() with the arguments 'janis' 'joplin'
    # Just like we used when we ran names.py
    # We assign the return value of this function to formatted_name

#3 We make an assertion
    # An assertion is a claim about a condition
    # We're are claiming that the value of formatted_name should be 
    # 'Janis Joplin'

# We'll have pytest run this file for us