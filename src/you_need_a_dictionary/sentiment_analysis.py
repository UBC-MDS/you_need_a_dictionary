"""
Module for performing sentiment analysis on preprocessed user input.
"""
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(sentence: str) -> dict:
    """
    Analyze the sentiment of the preprocessed user input.

    Args:
        sentence (str): The input string to analyze.

    Returns:
        dict: The sentiment analysis result.
        
    Examples:
        >>> analyze_sentiment("I absolutely love Kpop")
    """
    # These two checks are from prompt: "What other tests should I perform (use pytest) to ensure that my function performs as expected?"
    # Check for invalid type first
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")
        
    # Check for empty content
    if not sentence.strip():  # Using .strip() also catches "   "
        raise ValueError("Input sentence cannot be empty or whitespace only.")
        
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(sentence)
    return scores
