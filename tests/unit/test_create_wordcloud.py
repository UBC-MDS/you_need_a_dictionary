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
import nltk
from nltk.corpus import wordnet as wn
import sys
import re
from you_need_a_dictionary.wordcloud import create_wordcloud,similarity_score

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

# Antonym and synonym wordcloud for an adjective
@pytest.fixture 
def normal_case_both():
    word = "cold"
    sentence = "It's officially winter, the air outside is cold."
    type = "both"
    return word, sentence, type

# Synonym and antonym similarity scores  
@pytest.fixture 
def normal_case_scores():
    basis = wn.synset('car.n.01')
    lemmas = {wn.lemma('door.n.01.door'), wn.lemma('cat.n.01.cat'), wn.lemma('wheel.n.01.wheel'), wn.lemma('car.n.01.automobile')}
    return basis, lemmas
    

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

# ----------------------------------------------------------------------------- #
# create_wordcloud() – normal cases                                              #
# ----------------------------------------------------------------------------- #

def test_create_wordcloud_normal_1(normal_case_syn):
    """ Tests to ensure create_wordcloud function works as expected."""
    word, sentence, type = normal_case_syn
    results = create_wordcloud(word,sentence,type)
    # Verify return type 
    assert isinstance(results, plt.Figure)


def test_create_wordcloud_normal_2(normal_case_ant):
    """ Tests to ensure create_wordcloud function works as expected."""
    word, sentence, type = normal_case_ant
    results = create_wordcloud(word,sentence,type)

    # Verify return type 
    assert isinstance(results, plt.Figure)

def test_create_wordcloud_normal_3(normal_case_both):
    """ Tests to ensure create_wordcloud function works as expected."""
    word, sentence, type = normal_case_both
    results = create_wordcloud(word,sentence,type)

    # Verify return type
    assert isinstance(results, tuple)

    # There should be 2 figures returned
    assert len(results) == 2
    assert all(isinstance(fig, plt.Figure) for fig in results)

# Since create_wordcloud just outputs a wordcloud it is hard to test.
# Instead we can test that similarity_score outputs works as expected.
def test_similarity_score_normal(normal_case_scores):
    """ Tests to ensure similarity_score function works as expected."""
    basis, lemmas = normal_case_scores
    results = similarity_score(basis, lemmas)

    expected = {'door': 0.08333333333333333, 'wheel': 0.09090909090909091, 'cat': 0.05555555555555555, 'automobile': 1.0}

    assert results == expected

