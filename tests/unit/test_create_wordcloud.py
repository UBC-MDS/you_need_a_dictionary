"""
Tests for the create_wordcloud() and similarity_score() functions in wordcloud module.

The function create_wordcloud() is used to create a wordcloud of synonyms and/or antonyms for a given word.
The function similarity_score() is used to find the similarity strength between two words using nltk path_similarity().

Test categories:
1. Normal cases - Normal inputs
2. Edge cases - No antonyms 
3. Error cases - Invalid inputs


"""


import pytest
import you_need_a_dictionary as ynd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from nltk.corpus import wordnet as wn
from you_need_a_dictionary.wordcloud_utils import similarity_score


# Test cases were found using the following ChatGPT prompt: 
# Hi, here is the docstring for my function <insert create_wordcloud() docstring>, 
# can you help me find some test cases that I can use. 
# I would like 2 normal cases, a couple edge cases and a couple error cases. 

# ----------------------------------------------------------------------------- #
# Normal case test data                                                         #
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
# Edge case test data                                                           #
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

# Case 3 : word that is not in Wordnet 
# Expected behaviour : returns a string explaining that the word is not in Wordnet
@pytest.fixture
def edge_case_3(): 
    word = "and"
    sentence = "The car is parked outside and inside."
    type = "both"
    return word, sentence, type


# ----------------------------------------------------------------------------- #
# Error handling test data                                                      #
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
# create_wordcloud() – normal cases                                             #
# ----------------------------------------------------------------------------- #

def test_create_wordcloud_normal_1(normal_case_syn):
    """ Tests to ensure create_wordcloud function works as expected."""
    word, sentence, type = normal_case_syn
    results = ynd.create_wordcloud(word,sentence,type)
    # Verify return type 
    assert isinstance(results, plt.Figure)


def test_create_wordcloud_normal_2(normal_case_ant):
    """ Tests to ensure create_wordcloud function works as expected."""
    word, sentence, type = normal_case_ant
    results = ynd.create_wordcloud(word,sentence,type)

    # Verify return type 
    assert isinstance(results, plt.Figure)

def test_create_wordcloud_normal_3(normal_case_both):
    """ Tests to ensure create_wordcloud function works as expected."""
    word, sentence, type = normal_case_both
    results = ynd.create_wordcloud(word,sentence,type)

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

# ----------------------------------------------------------------------------- #
# create_wordcloud() – edge cases                                               #
# ----------------------------------------------------------------------------- #

def test_create_wordcloud_edge(edge_case_1,edge_case_2,edge_case_3):
    """ Tests to ensure create_wordcloud function works correctly when the word has no antonym when type = 'antonym' and type = 'both'."""

    # No antonym and type = 'antonym' - returns a string explaining no antonyms exist
    word, sentence, type = edge_case_1
    result_ant = ynd.create_wordcloud(word, sentence, type)
    expected = "You can try again with another word, try another meaning or get the synonym wordcloud."
    assert result_ant == expected
    
    # No antonym and type = 'both' - returns just the synonym wordcloud
    word, sentence, type = edge_case_2
    result_both = ynd.create_wordcloud(word, sentence, type)
    assert isinstance(result_both, plt.Figure)

    # The word is not in the Wordnet - returns a string explaining that the word is not in Wordnet
    word, sentence, type = edge_case_3
    results = ynd.create_wordcloud(word, sentence, type)
    expected = f"The word '{word}' is not in the nltk Wordnet."
    assert results == expected

# ----------------------------------------------------------------------------- #
# create_wordcloud() – error cases                                              #
# ----------------------------------------------------------------------------- #

def test_create_wordcloud_error(error_case_1, error_case_2, error_case_3, error_case_4):
    """ Tests to ensure create_wordcloud function validates inputs correctly and raises appropriate errors."""
    # Test 1 - word is not a string
    with pytest.raises(TypeError, match="word argument must be a string."):
        word, sentence, type = error_case_1
        ynd.create_wordcloud(word, sentence, type)

    # Test 2 - sentence is not a string
    with pytest.raises(TypeError, match="sentence argument must be a string."):
        word, sentence, type = error_case_2
        ynd.create_wordcloud(word, sentence, type)

    # Test 3 - type is not a string
    with pytest.raises(TypeError, match="type argument must be a string."):
        word, sentence, type = error_case_3
        ynd.create_wordcloud(word, sentence, type)

    # Test 4 - type is not one of the correct options
    with pytest.raises(NameError, match="type argument must be a either synonym, antonym or both."):
        word, sentence, type = error_case_4
        ynd.create_wordcloud(word, sentence, type)

