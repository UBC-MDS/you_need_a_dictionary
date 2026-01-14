"""
A test module that tests the wordcloud function.
"""
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

import pytest
import matplotlib.pyplot as plt
from you_need_a_dictionary.wordcloud import create_wordcloud

@pytest.fixture 
def normal_case():
    with open('tests/unit/normal_case.txt', 'r') as f: 
        content = f.read()
    return content

@pytest.fixture 
def error_case():
    with open('tests/unit/error_case.txt', 'r') as f: 
        content = f.read()
    return content

def test_create_wordcloud(normal_case):
    """ Tests to ensure create_wordcloud function works as expected."""
    results = create_wordcloud('blue',normal_case)

    # Verify return type 
    assert isinstance(results, plt.Figure)


def test_error_cases(normal_case,error_case):
    """ Tests to ensure create_wordcloud function validates inputs correctly and raises appropriate errors."""
    results = create_wordcloud('door',normal_case)

    # Word not in wordnet
    with pytest.raises(LookupError):
        create_wordcloud('because', error_case)

    # Wrong input type 
    
    with pytest.raises(TypeError):
        create_wordcloud(12, error_case) # word argument not a string
    
    with pytest.raises(TypeError):
        create_wordcloud('blue', 12) # sentence argument not a string

    with pytest.raises(TypeError):
        create_wordcloud('blue', normal_case, 12) # type argument not a string

    
    # Wrong input for type argument
    with pytest.raises(NameError):
        create_wordcloud('blue', normal_case, 'random')

