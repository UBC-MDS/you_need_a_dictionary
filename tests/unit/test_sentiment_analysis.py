"""
Unit tests for the sentiment_analysis module.
"""

import pytest
import you_need_a_dictionary as ynd


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
        ynd.analyze_sentiment("")


# Below code based on prompt: What other tests should I perform (use pytest) to ensure that my function performs as expected?
def test_sentiment_values(sample_sentences):
    """Test that sentiment scores are returned for a positive sentence."""
    result = ynd.analyze_sentiment(sample_sentences["positive"])
    assert 'neg' in result
    assert 'neu' in result
    assert 'pos' in result
    assert 'compound' in result
    assert result['pos'] > result['neg']

def test_negative_sentiment(sample_sentences):
    """Test that a negative sentence results in a higher negative score."""
    result = ynd.analyze_sentiment(sample_sentences["negative"])
    assert result['neg'] > result['pos']
    assert result['compound'] < 0

def test_neutral_sentiment(sample_sentences):
    """Test that a neutral statement has a high neutral score."""
    result = ynd.analyze_sentiment(sample_sentences["neutral"])
    assert result['neu'] > 0.5
    assert abs(result['compound']) < 0.1

def test_exception_message():
    """Test that the exception message is correct for empty input."""
    with pytest.raises(Exception, match="Input sentence cannot be empty or whitespace only."):
        ynd.analyze_sentiment("")

def test_return_type():
    """Ensure the function returns a dictionary."""
    result = ynd.analyze_sentiment("Hello world")
    assert isinstance(result, dict)

def test_whitespace_input():
    """Check behavior for whitespace-only strings."""
    with pytest.raises(ValueError, match="cannot be empty"):
        ynd.analyze_sentiment("     ")

    
# Additional test for invalid input type from prompt "What other tests should I perform (use pytest) to ensure that my function performs as expected?"
def test_invalid_type():
    """Test that a non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string."):
        ynd.analyze_sentiment(123)
        ynd.analyze_sentiment(None)

# Additional edge cases based on prompt "What are some edge cases that I would need to test for now? Maybe expand on the fixture if needed."
def test_mixed_sentiment(sample_sentences):
    """Test that a sentence with mixed feelings has both pos and neg scores."""
    result = ynd.analyze_sentiment(sample_sentences["mixed"])
    assert result['pos'] > 0
    assert result['neg'] > 0


def test_emoji_sentiment(sample_sentences):
    """Test that inputting emojis raises a ValueError."""
    with pytest.raises(ValueError, match="Input cannot contain emojis"):
        ynd.analyze_sentiment(sample_sentences["emoji"])


def test_special_characters(sample_sentences):
    """Test that special characters only input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must contain at least one alphanumeric character"):
        ynd.analyze_sentiment(sample_sentences["special_chars"])


def test_caps_intensity(sample_sentences):
    """Test that all caps input is handled (usually indicates intensity)."""
    result = ynd.analyze_sentiment(sample_sentences["caps"])
    assert result['pos'] > 0
    assert result['compound'] > 0.5


# If you could add two impactful unit tests in addition to the tests in test_sentiment_analysis.py,
# what would they be? Apply coding best practices and look for edge cases as well.
def test_sentiment_scores_within_valid_ranges():
    """Test that all sentiment scores are within their valid ranges (invariant check)."""
    test_inputs = [
        "I love this!",
        "This is terrible",
        "The item is blue.",
        "AMAZING!!!",
        "not good but not bad either"
    ]
    
    for sentence in test_inputs:
        result = ynd.analyze_sentiment(sentence)
        
        # pos, neu, neg should each be in [0, 1]
        assert 0 <= result['pos'] <= 1, f"pos score {result['pos']} out of range for: {sentence}"
        assert 0 <= result['neu'] <= 1, f"neu score {result['neu']} out of range for: {sentence}"
        assert 0 <= result['neg'] <= 1, f"neg score {result['neg']} out of range for: {sentence}"
        
        # compound should be in [-1, 1]
        assert -1 <= result['compound'] <= 1, f"compound score {result['compound']} out of range for: {sentence}"
        
        # Sum of pos, neu, neg should be approximately 1.0 (allowing for floating point precision)
        total = result['pos'] + result['neu'] + result['neg']
        assert abs(total - 1.0) < 0.01, f"Scores don't sum to 1.0 for: {sentence}"


def test_sentiment_analysis_reproducibility():
    """Test that sentiment analysis is deterministic (same input always produces same output)."""
    test_sentence = "The product is amazing but customer service was disappointing."
    
    # Call the function multiple times with the same input
    result1 = ynd.analyze_sentiment(test_sentence)
    result2 = ynd.analyze_sentiment(test_sentence)
    result3 = ynd.analyze_sentiment(test_sentence)
    
    # All results should be identical
    assert result1 == result2, "First and second calls returned different results"
    assert result2 == result3, "Second and third calls returned different results"
    
    # Verify the dictionary structure is consistent
    assert set(result1.keys()) == {'neg', 'neu', 'pos', 'compound'}