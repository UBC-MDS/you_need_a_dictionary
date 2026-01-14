
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import pytest
from you_need_a_dictionary.word_replacement import word_replacement

def test_word_replacement():
    """
    Test that word_replacement works as expected.
    """
    sentence = "I love Vancouver! MDS is so fun."
    target_word = "fun"
    replacement_word = "intense"
    
    new_function_sentence = word_replacement(sentence, target_word, replacement_word)['New Sentence']
    expected_new_sentence = "I love Vancouver MDS is so intense"
    
    assert new_function_sentence == expected_new_sentence, f"Expected {expected_new_sentence} but got {new_function_sentence}"

