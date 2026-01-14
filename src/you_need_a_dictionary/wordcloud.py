"""
A module that creates wordclouds of antonyms and/or synonyms for a given word.

"""
import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
import string

def create_wordcloud(word, sentence, type='both'):
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
    sentence : string
        The sentence that contains the word we are interested in.
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

    # Get the correct meaning for the word based on sentence context
    sentence_list = str.split(sentence.translate(str.maketrans('', '', string.punctuation))) # Inspiration drawn from Stack Overflow : https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    word_with_context = lesk(sentence_list, word)

    # Get the antonyms and synonyms
    synonyms = set()
    antonyms = set() 
    for synset in wn.synsets('open'):
        for lemma in synset.lemmas():
            synonyms.add(lemma)
            for antonym in lemma.antonyms():
                antonyms.add(antonym)
    
    print(synonyms, antonyms)
    
