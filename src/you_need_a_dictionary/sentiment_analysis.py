"""
Module for performing sentiment analysis on preprocessed user input.
"""
from nltk.sentiment import SentimentIntensityAnalyzer

import re
import nltk
nltk.download('vader_lexicon')


def analyze_sentiment(sentence: str) -> dict:
    """
    Analyze the sentiment of the preprocessed user input.

    Parameters
    ----------
    sentence : str
        The input string to analyze.

    Returns
    ----------
    dict
        The sentiment analysis result.
        - neg : Negative sentiment score on a scale fro 0 to 1 (1 being the most negative)
        - neu: Neutral sentiment score on a scale fro 0 to 1 (1 being the most neutral)
        - pos: Positive sentiment score on a scale fro 0 to 1 (1 being the most positive)
        - compound: Compound sentiment (How positive or negative the input text is overall) 
        on a scale from -1 to 1 (-1 being most negative, 1 being most positive)
        
    Examples
    ----------
    >>> analyze_sentiment("I absolutely love Kpop")
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

