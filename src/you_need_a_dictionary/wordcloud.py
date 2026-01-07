"""
A module that creates wordclouds of antanonyms and/or synonyms of a given word .

This module contains functions to:
- create the wordclouds
- find 

"""

def create_wordcloud(word, type='both'):
    """
    This function creates a wordcloud of either antonyms, synonyms or both for a given word.


    Parameters
    ----------
    word : string
        The word that we want the synonyms and antonyms.
    type : string
        Either 'antonym', 'synonym', or 'both'. Default is 'both'

    Returns
    -------
    float
        A wordcloud containing antonyms and/or synonyms for a given word.

    Examples
    --------
    
    """
    ...

def find_strength(word, other_word):
    """
    This function finds the strength of the similarity between 2 words.

    Parameters
    ----------
    word : string
        The word that we want the synonyms and antonyms.
    other_word : string
        The antonym or synonym that we want to compare.

    Returns
    -------
    float
        The strength of the similarity of the 2 words. It ranges between 0 and 1 where 1 means 
        strong similarity between words and 0 means weak similarity.

    Examples
    --------
    

    
    """
    ...