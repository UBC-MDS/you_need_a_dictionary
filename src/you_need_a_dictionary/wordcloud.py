"""
A module that creates wordclouds of antanonyms or synonyms of a word .

"""

def create_wordcloud(word, sentence, type='both'):
    """
    This function creates a wordcloud of either antonyms, synonyms or both for a given word.


    Parameters
    ----------
    word : string
        The word that we want the synonyms and antonyms.
    sentence : string
        The sentence that the word comes from.
    type : string
        Either 'antonym', 'synonym', or 'both'. Default is 'both'

    Returns
    -------
    float
        A wordcloud containing antonyms and/or synonyms for a given word.

    Examples
    --------
    

    """