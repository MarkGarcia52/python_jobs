# Write a function that accepts two parameters:
# A city name and country name

# The function should return a single string City, Country

# Store the function in a module called city_function.py

def get_formatted_city_country(city, country):
    """Generate a neatly formatted city, country"""
    full_city_country = f"{city} {country}"
    return full_city_country.title()