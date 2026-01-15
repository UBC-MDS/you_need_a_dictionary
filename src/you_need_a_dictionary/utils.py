"""
Helper to find the highest score among pos, neg, and neu
returned from analyze_sentiment.

Author: Godsgift Braimah
Date: 2026-01-15
"""

def sentiment_specifics(sentiment_dict: dict) -> tuple:
    """
    Find the highest score among pos, neg, and neu.
    
    Parameters
    ----------
    sentiment_dict : dict
        The dictionary returned from analyze_sentiment function.
    
    Returns
    -------
    tuple: (sentiment_type, score)
    Example: ('Positive', 0.85)
    """
    specifics = {
        'Positive': sentiment_dict.get('pos', 0),
        'Negative': sentiment_dict.get('neg', 0),
        'Neutral': sentiment_dict.get('neu', 0)
    }
    
    max_type = max(specifics, key=specifics.get)
    max_score = specifics[max_type]
    
    return max_type, max_score