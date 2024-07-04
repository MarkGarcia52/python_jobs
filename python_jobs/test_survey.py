import pytest
from survey import AnonymousSurvey

@pytest.fixture #1
def language_survey(): #2
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey): #3
    """Test that a single response is stored properly."""
# gone
    language_survey.store_responses('English') #4
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey): #5
    """Test that three individual respones are stored properly."""
# gone
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_responses(response) #6

    for response in responses:
        assert response in language_survey.responses

# 1
    # We apply the @pytest.fixture decorator to the new function

# 2
    # language_survey
    # This function bulids an AnonymousSurvey object and returns the new survey
        
# 3 & # 5
    # Both changed parameters
    # Now each test function now has a parameter called language_survey
    # When a parameter in a test function matches the name of a function
    # with the pytest decorator, the fixture will be run automatically
    # and return value will be passed to the test function