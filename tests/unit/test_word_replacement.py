"""
Unit tests for the word_replacement function in you_need_a_dictionary module.
Author: Godsgift Braimah
Date: 2026-01-15
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import pytest
from you_need_a_dictionary.word_replacement import word_replacement

def test_word_replacement():
    """
    Test 1: Test that word_replacement base case works as expected.
    """
    sentence = "MDS is so fun"
    target_word = "fun"
    replacement_word = "intense"
    
    result = word_replacement(sentence, target_word, replacement_word)
    
    assert result['New Sentence'] == "MDS is so intense"
    assert isinstance(result, dict)

def test_word_replacement_punctuation_preservation():
    """
    Test 2: Punctuation Handling.
    Ensures that punctuation is NOT removed during replacement.
    """
    sentence = "I love Vancouver! MDS is so fun."
    target = "fun"
    replacement = "okay"
    
    result = word_replacement(sentence, target, replacement)
    expected =  "I love Vancouver! MDS is so okay."
    assert result['New Sentence'] == expected
    
def test_word_replacement_multiple_occurrences():
    """
    Test 3: Edge Case.
    Ensures all instances of the word are replaced.
    """
    sentence = "Today is a bad day, really bad day."
    target = "bad"
    replacement = "good"
    
    result = word_replacement(sentence, target, replacement)
    
    expected ="Today is a good day, really good day."
    assert result['New Sentence'] == expected
    
def test_replace_specific_occurrence_first():
    """
    Test 4: Occurrence case replacing only the FIRST instance.
    """
    sentence = "Today is a bad day, really bad day."
    target = "bad"
    replacement = "good"

    result = word_replacement(sentence, target, replacement, occurrence=1)
    
    assert result['New Sentence'] == "Today is a good day, really bad day."
    
def test_word_replacement_type_error():
    """
    Test 5: Exception Handling (TypeError).
    Tests if the function raises TypeError when integers are passed.
    """
    with pytest.raises(TypeError):
        word_replacement(123, "fun", "bad")

def test_word_replacement_value_error():
    """
    Test 6: Exception Handling (ValueError).
    Tests if the function raises ValueError when target word is missing.
    """
    sentence = "MDS Quiz week is upon us"
    target = "month" 
    replacement = "day"
    
    with pytest.raises(ValueError):
        word_replacement(sentence, target, replacement)
