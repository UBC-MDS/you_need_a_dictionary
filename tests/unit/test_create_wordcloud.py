"""
Tests for the create_wordcloud() function in wordcloud module.

The create_wordcloud() is used to create a wordcloud of synonyms and/or antonyms for a given word.

Test categories:
1. Normal cases - Normal inputs
2. Edge cases - ...
3. Error cases - Invalid inputs

Run tests with: pytest tests/test_create_features.py -v
"""

import os
import pytest
import matplotlib.pyplot as plt
import sys
import re
from you_need_a_dictionary.wordcloud import create_wordcloud

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

# Test cases were found using the following ChatGPT prompt: 
# Hi, here is the docstring for my function <insert create_wordcloud() docstring>, 
# can you help me find some test cases that I can use. 
# I would like 2 normal cases, a couple edge cases and a couple error cases. 

# ----------------------------------------------------------------------------- #
# Normal case test data
# ----------------------------------------------------------------------------- #

# Synonym wordcloud for a common noun
@pytest.fixture 
def normal_case_syn():
    word = "car"
    sentence = "The car is on the road"
    type = "synonym"
    return word, sentence, type

# Antonym wordcloud for an adjective
@pytest.fixture 
def normal_case_ant():
    word = "happy"
    sentence = "I am happy with the results"
    type = "antonym"
    return word, sentence, type
    

# ----------------------------------------------------------------------------- #
# Edge case test data
# ----------------------------------------------------------------------------- #

# Case 1 : word with no antonyms
# Expected behaviour : returns a string explaining no antonyms exist
@pytest.fixture
def edge_case_1():
    word = "table"
    sentence = "The table is made of wood"
    type = "antonym"
    return word, sentence, type



# Case 2 : word with no antonyms when both wordclouds are asked for
# Expected behaviour : returns just the synonym wordcloud
@pytest.fixture
def edge_case_2(): 
    word = "car"
    sentence = "The car is parked outside"
    type = "both"
    return word, sentence, type

# ----------------------------------------------------------------------------- #
# Error handling test data 
# ----------------------------------------------------------------------------- #

# Case 1 : word is not a string
# Expected behaviour : Should raise TypeError
@pytest.fixture
def error_case_1(): 
    word = 123
    sentence = "The car is on the road"
    type = "synonym"
    return word, sentence, type


# Case 2 : sentence is not a string
# Expected behaviour : Should raise a TypeError
@pytest.fixture
def error_case_2(): 
    word = "car"
    sentence = 42
    type = "synonym"
    return word, sentence, type


# Case 3 : type is not a string
# Expected behaviour : Should raise a TypeError
@pytest.fixture
def error_case_3(): 
    word = "car"
    sentence = "The car is on the road"
    type = 5
    return word, sentence, type

# Case 4 : type is not one of the correct options 
# Expected behaviour : Should raise a NameError
@pytest.fixture
def error_case_4():  
    word = "car"
    sentence = "The car is on the road"
    type = "syn"
    return word, sentence, type



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





