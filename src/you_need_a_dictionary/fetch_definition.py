"""
Module that fetches the definition, synonyms and antonyms of a given word using WordNet.
"""


def fetch_definition(word):
    """
    Fetch the standard definition of a given word along with its synonyms
    and antonyms using WordNet.

    This function uses the NLTK WordNet database to retrieve the
    most common definition of the specified word. It also extracts associated
    synonyms and antonyms based on WordNet synsets. The results are combined
    into a single formatted string for easy display.

    Parameters
    ----------
    word : string
        The word for which the definition, synonyms, and antonyms
        are to be retrieved.

    Returns
    -------
    string
        A formatted string containing the standard definition of the word,
        followed by its synonyms and antonyms as identified by WordNet.

    Examples
    --------
    >>> fetch_definition('happy')

    >>> fetch_definition('dark')
    """
