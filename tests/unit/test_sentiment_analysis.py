import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import pytest
from you_need_a_dictionary.sentiment_analysis import analyze_sentiment

def test_empty_string():
    """Test that an empty string raises an Exception."""
    with pytest.raises(ValueError, match="cannot be empty"):
        analyze_sentiment("")


# Below code based on prompt: What other tests should I perform (use pytest) to ensure that my function performs as expected?
def test_sentiment_values():
    """Test that sentiment scores are returned for a positive sentence."""
    result = analyze_sentiment("I absolutely love Kpop")
    assert 'neg' in result
    assert 'neu' in result
    assert 'pos' in result
    assert 'compound' in result
    assert result['pos'] > result['neg']

def test_negative_sentiment():
    """Test that a negative sentence results in a higher negative score."""
    result = analyze_sentiment("I absolutely hate this terrible experience")
    assert result['neg'] > result['pos']
    assert result['compound'] < 0

def test_neutral_sentiment():
    """Test that a neutral statement has a high neutral score."""
    result = analyze_sentiment("The bag is on the table.")
    assert result['neu'] > 0.5
    assert abs(result['compound']) < 0.1

def test_exception_message():
    """Test that the exception message is correct for empty input."""
    with pytest.raises(Exception, match="Input sentence cannot be empty or whitespace only."):
        analyze_sentiment("")

def test_return_type():
    """Ensure the function returns a dictionary."""
    result = analyze_sentiment("Hello world")
    assert isinstance(result, dict)

def test_whitespace_input():
    """Check behavior for whitespace-only strings."""
    with pytest.raises(ValueError, match="cannot be empty"):
        analyze_sentiment("     ")

    
# Additional test for invalid input type from prompt "What other tests should I perform (use pytest) to ensure that my function performs as expected?"
def test_invalid_type():
    """Test that a non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string."):
        analyze_sentiment(123)
        analyze_sentiment(None)