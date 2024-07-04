from city_function import get_formatted_city_country

def test_city_country():
    """Does city 'santiago' and country 'chile' work?"""
    formatted_city_country = get_formatted_city_country('santiago', 'chile')
    assert formatted_city_country == 'Santiago Chile'