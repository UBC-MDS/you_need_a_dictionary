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
import string
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sentiment_analysis import analyze_sentiment


def word_replacement(sentence : str, target_word : str, replacement_word : str) -> dict:
    """
    Substitutes a target word in a sentence with a replacement word and calculates 
    the new sentiment score.

    This function identifies all occurrences of a specified target word within 
    the input sentence, replaces them with the provided replacement word, and 
    then performs sentiment analysis on the newly modified sentence. This allows 
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

    Returns
    -------
    dict
        A dictionary containing the results of the simulation with the keys:
        - 'new_sentence' (str): The modified sentence after replacement.
        - 'previous_sentiment' (float): The sentiment score of the original sentence.
        - 'new_sentiment' (float): The sentiment score of the modified sentence.
        - 'score_diff' (float): The difference between new and original scores.

    Raises
    ------
    ValueError
        If the `target_word` is not present in the input `sentence`.
    TypeError
        If `sentence`, `target_word`, or `replacement_word` are not strings.
    """
    if not isinstance(sentence, str) or not isinstance(target_word, str) or not isinstance(replacement_word, str):
        raise TypeError(f"Expected the input to be of type str, got {type(sentence)}", f"{type(target_word)}", f"{type(replacement_word)}")
    
    # remove punctuations
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    # convert to list? # lower the words?
    list_sentence = sentence.split() # .lower()
    index = list_sentence.index(target_word)

    # find the position and join it back?
    list_sentence[index] = replacement_word
    new_sentence = ' '.join(list_sentence)
    
    previous_sentiment = analyze_sentiment(sentence)['compound']
    new_sentiment = analyze_sentiment(new_sentence)['compound']
    score_diff = new_sentiment - previous_sentiment
    
    results = {
        'New Sentence': new_sentence,
        'Previous Sentiment': previous_sentiment,
        'New Sentiment': new_sentiment,
        'Score Difference': score_diff
    }
    
    return results


#changes to make
# Word must be found in the sentence
# Type checks for inputs
# How does the function handle punctuations after removing them to do the replacement?
## remember to update this function to handle punctuations removed.