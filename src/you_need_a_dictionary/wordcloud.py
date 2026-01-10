"""
A module that creates wordclouds of antonyms and/or synonyms for a given word.

"""
def create_wordcloud(word, type='both'):
    """
    This function creates a wordcloud of either antonyms, 
    synonyms or both for a given word.

    The word in the middle of the wordcloud is the word 
    we want the antonyms/synonyms for.
    The size of the words in the wordcloud are determined 
    by the strength of the similarity between the given word and its antonym/synonym. 
    The similarity score can be found using the NLTK wordnet 
    package and ranges between 0 and 1 with 1 meaning strong similarity and 0 means weak similarity.

    Parameters
    ----------
    word : string
        The central word in the wordcloud for which we 
        want to find the synonyms/antonyms.
    type : string
        This determines whether the wordcloud contains antonyms or synonyms or whether 
        the function outputs two wordclouds (one for antonyms and one for synonyms).
        Either 'antonym', 'synonym', or 'both'. Default is 'both'

    Returns
    -------
    plt.Figure
        A Matplotlib figure of a wordcloud containing antonyms and/or synonyms for a given word.

    Examples
    --------
    >>> create_wordcloud('car', 'antonym')

    >>> create_wordcloud('happy')
    
    """
    ...
