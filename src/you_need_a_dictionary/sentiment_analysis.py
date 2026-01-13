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
        preprocessed_input (str): The preprocessed input from the user.

    Returns:
        str: The sentiment analysis result.
    """

    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(sentence)
    return scores

sentence = "NLTK is a powerful tool, but sometimes complex."
result = analyze_sentiment(sentence)
print(result)
