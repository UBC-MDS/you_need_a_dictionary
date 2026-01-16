"""
Replaces target word and computes sentiment score.

This script initializes the function for word substitution.
It ensures users can make comparisons based off word impact.

Author: Godsgift Braimah
Date: 2026-01-08
"""

##################################################
# Import statements
##################################################
import re
import sys
import os
from you_need_a_dictionary.sentiment_analysis import analyze_sentiment
from you_need_a_dictionary.utils import sentiment_specifics


def word_replacement(sentence : str, target_word : str, replacement_word : str, occurrence: int = None) -> dict:
    """
    Substitutes a target word in a sentence with a replacement word and calculates 
    the new sentiment score.

    This function identifies all occurrences of a specified target word within 
    the input sentence:
    - Can replace ALL occurrences of the target word,
    - Or replace a SPECIFIC occurrence if specified.
    The function then performs sentiment analysis on the newly modified sentence. This allows 
    users to quantifiably measure how specific vocabulary choices impact the 
    emotional tone of their text.

    Parameters
    ----------
    sentence : str
        The original input sentence or text to be analyzed.
    target_word : str
        The specific word within the sentence that needs to be replaced.
    replacement_word : str
        The new word that will substitute the target_word.
    occurrence : int, optional
        If provided, only the nth occurrence of the target_word will be replaced. 
        Defaults to None, and all occurrences will be replaced.

    Returns
    -------
    dict
        A dictionary containing the results of the simulation with the keys:
        - 'New Sentence' (str): The modified sentence after replacement.
        - 'Previous Sentiment Type' (str): The type of sentiment obtained from the 
            previous sentence(Positive/Neutral/Negative).
        - 'Previous Sentiment Score' (float): The sentiment score of the original sentence.
        - 'New Sentiment Type' (str): The type of sentiment obtained from the new sentence.
        - 'New Sentiment Score' (float): The sentiment score of the new sentence.

    Raises
    ------
    ValueError
        If the `target_word` is not present in the input `sentence`.
    TypeError
        If `sentence`, `target_word`, or `replacement_word` are not strings.
    """
    if not isinstance(sentence, str) or not isinstance(target_word, str) or not isinstance(replacement_word, str):
        raise TypeError(f"Expected the input to be of type str, got {type(sentence)}", f"{type(target_word)}", f"{type(replacement_word)}")
    
    if occurrence is not None and not isinstance(occurrence, int):
        raise TypeError(f"Expected occurrence to be of type int, got {type(occurrence)}")
    
    # uses regex to find all matched of the target word
    pattern = r'\b' + re.escape(target_word) + r'\b'
    matches = list(re.finditer(pattern, sentence))

    if not matches:
        raise ValueError(f"The target word '{target_word}' not found in the sentence.")
    
    # Replace all or specific occurrence of the target word
    new_sentence = ""
    
    if occurrence is None:
        new_sentence = re.sub(pattern, replacement_word, sentence)
    else:
        if occurrence < 1 or occurrence > len(matches):
            raise ValueError(
                f"Found {len(matches)} occurrences of '{target_word}', "
                f"but you requested occurrence #{occurrence}."
            )
        # Finds the specific match to replace
        target_match = matches[occurrence - 1]
        start_index = target_match.start()
        end_index = target_match.end()
        new_sentence = sentence[: start_index] + replacement_word + sentence[end_index:]
    
    previous_sentiment = analyze_sentiment(sentence)
    new_sentiment = analyze_sentiment(new_sentence)
    prev_type, prev_score = sentiment_specifics(previous_sentiment)
    new_type, new_score = sentiment_specifics(new_sentiment)
    
    results = {
        'New Sentence': new_sentence,
        'Previous Sentiment Type': prev_type,
        'Previous Sentiment Score': prev_score,
        'New Sentiment Type': new_type,
        'New Sentiment Score': new_score
    }
    
    return results
