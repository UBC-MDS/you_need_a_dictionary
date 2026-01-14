"""
A test module that tests the wordcloud function.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import matplotlib.pyplot as plt
from src.you_need_a_dictionary.wordcloud import create_wordcloud
import pytest

@pytest.fixture 
def normal_case():
    with open('tests/normal_case.txt', 'r') as f: 
        content = f.read()
    return content

@pytest.fixture 
def error_case():
    with open('tests/error_case.txt', 'r') as f: 
        content = f.read()
    return content

def test_create_wordcloud(normal_case):
    """ Tests to ensure create_wordcloud function works as expected."""
    results = create_wordcloud('blue',normal_case)

    # Verify return type 
    assert isinstance(results, plt.Figure)


def test_error_cases():
     """ Tests to ensure create_wordcloud function validates inputs correctly and raises appropriate errors."""
    results = create_wordcloud('door')

    # Word not in wordnet
    with pytest.raises(LookupError):
        create_wordcloud('because', error_case)

    # Input not a string
    with pytest.raises(TypeError):
        create_wordcloud('12', error_case)
    
    # Wrong input for type argument
    with pytest.raises(NameError):
        create_wordcloud('blue', normal_case, 'random')

