"""
Module for performing sentiment analysis on preprocessed user input.
"""
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import nltk
nltk.download('vader_lexicon')


def analyze_sentiment(sentence: str) -> dict:
    """
    Analyze the sentiment of the preprocessed user input using VADER sentiment analysis.

    This function performs sentiment analysis on a given string and returns sentiment scores.
    It validates the input to ensure it meets specific requirements: must be a non-empty string
    containing at least one alphanumeric character and no emojis.

    Parameters
    ----------
    sentence : str
        The input string to analyze. Must be non-empty, contain at least one alphanumeric
        character, and cannot contain emojis.

    Returns
    -------
    dict
        A dictionary containing sentiment scores with keys:
        - 'neg': Negative sentiment score (float between 0 and 1)
        - 'neu': Neutral sentiment score (float between 0 and 1)
        - 'pos': Positive sentiment score (float between 0 and 1)
        - 'compound': Composite sentiment score (float between -1 and 1)

    Raises
    ------
    TypeError
        If the input is not a string.
    ValueError
        If the input is empty, contains only whitespace, lacks alphanumeric characters,
        or contains emojis.

    Examples
    --------
    >>> analyze_sentiment("I absolutely love Kpop")
    {'neg': 0.0, 'neu': 0.315, 'pos': 0.685, 'compound': 0.7844}
    """
    # These two checks are from prompt: "What other tests should I perform (use pytest) to ensure that my function performs as expected?"
    # Check for invalid type first
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")
    
    # Check for empty content
    if not sentence.strip():  # Using .strip() also catches "   "
        raise ValueError("Input sentence cannot be empty or whitespace only.")
    # From prompt: "From the edge case tests like special chars or emojis, can you write some checks in the sentiment_analysis.py file to raise errors, then edit the test_sentiment_analysis.py to instead check if the errors were raised?"
    # Check for at least one alphanumeric character (catches special chars only)
    if not re.search(r'[a-zA-Z0-9]', sentence):
        raise ValueError("Input must contain at least one alphanumeric character.")

    # Check for emojis (simplified regex for common emoji ranges)
    if re.search(r'[\U0001F000-\U0001F9FF]', sentence):
        raise ValueError("Input cannot contain emojis.")
    
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(sentence)
    return scores

