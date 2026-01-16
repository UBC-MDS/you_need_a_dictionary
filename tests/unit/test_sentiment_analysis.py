"""
Unit tests for the sentiment_analysis module.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import pytest
from you_need_a_dictionary.sentiment_analysis import analyze_sentiment


@pytest.fixture
def sample_sentences():
    """Fixture to provide sample sentences for sentiment analysis."""
    return {
        "positive": "I absolutely love Kpop",
        "negative": "I absolutely hate this terrible experience",
        "neutral": "The bag is on the table.",
        "mixed": "The food was delicious but the service was terrible.",
        "emoji": "I am so happy today! 😄",
        "special_chars": "@#$%^&*",
        "caps": "THIS IS AMAZING"
    }


def test_empty_string():
    """Test that an empty string raises an Exception."""
    with pytest.raises(ValueError, match="cannot be empty"):
        analyze_sentiment("")


# Below code based on prompt: What other tests should I perform (use pytest) to ensure that my function performs as expected?
def test_sentiment_values(sample_sentences):
    """Test that sentiment scores are returned for a positive sentence."""
    result = analyze_sentiment(sample_sentences["positive"])
    assert 'neg' in result
    assert 'neu' in result
    assert 'pos' in result
    assert 'compound' in result
    assert result['pos'] > result['neg']

def test_negative_sentiment(sample_sentences):
    """Test that a negative sentence results in a higher negative score."""
    result = analyze_sentiment(sample_sentences["negative"])
    assert result['neg'] > result['pos']
    assert result['compound'] < 0

def test_neutral_sentiment(sample_sentences):
    """Test that a neutral statement has a high neutral score."""
    result = analyze_sentiment(sample_sentences["neutral"])
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

# Additional edge cases based on prompt "What are some edge cases that I would need to test for now? Maybe expand on the fixture if needed."
def test_mixed_sentiment(sample_sentences):
    """Test that a sentence with mixed feelings has both pos and neg scores."""
    result = analyze_sentiment(sample_sentences["mixed"])
    assert result['pos'] > 0
    assert result['neg'] > 0


def test_emoji_sentiment(sample_sentences):
    """Test that inputting emojis raises a ValueError."""
    with pytest.raises(ValueError, match="Input cannot contain emojis"):
        analyze_sentiment(sample_sentences["emoji"])


def test_special_characters(sample_sentences):
    """Test that special characters only input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must contain at least one alphanumeric character"):
        analyze_sentiment(sample_sentences["special_chars"])


def test_caps_intensity(sample_sentences):
    """Test that all caps input is handled (usually indicates intensity)."""
    result = analyze_sentiment(sample_sentences["caps"])
    assert result['pos'] > 0
    assert result['compound'] > 0.5