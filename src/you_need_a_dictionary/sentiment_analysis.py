"""
Module for performing sentiment analysis on preprocessed user input.
"""
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(sentence: str) -> str:
    """
    Analyze the sentiment of the preprocessed user input.

    Args:
        sentence (str): The input string to analyze.

    Returns:
        str: The sentiment analysis result.
        
    Examples:
        >>> analyze_sentiment("I absolutely love Kpop")
    """
    if not sentence:
        raise Exception("Input sentence is empty.")
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(sentence)
    return scores
