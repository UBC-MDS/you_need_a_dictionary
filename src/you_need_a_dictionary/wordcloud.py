"""
A module that creates wordclouds of antonyms and/or synonyms for a given word.
"""


import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
import string

from you_need_a_dictionary.wordcloud_utils import similarity_score, wordcloud_plotter

def create_wordcloud(word, sentence, type='both'):
    """
    This function creates a wordcloud of either antonyms, 
    synonyms or both for a given word.

    The size of the words in the wordcloud are determined 
    by the strength of the similarity between the given word and its antonym or synonym. 
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
    >>> create_wordcloud('car', 'The car is on the road', 'antonym')

    >>> create_wordcloud('happy', 'I am glad this trip made you happy')
    
    """
    # Check that Wordnet works as expected
    try:
        wn.synsets("test")
    except LookupError :
        raise LookupError(
            "The function was not able to access Wordnet. Ensure the nltk package is installed and imported. \
            If needed run the following commands: from nltk.corpus import wordnet as wn "
        ) 
    
    
    # Check that word input is a string
    if not isinstance(word, str):
        raise TypeError("word argument must be a string.")
    
     # Check that the word is in Wordnet
    synsets = wn.synsets(word)
    if not synsets:
        return f"The word '{word}' is not in the nltk Wordnet."
    
    # Check that sentence input is a string
    if not isinstance(sentence, str):
        raise TypeError("sentence argument must be a string.")
    
    # Check that type input is a string
    if not isinstance(type, str):
        raise TypeError("type argument must be a string.")
    
    # Check that type input is one of the options
    if not (type=='synonym' or type=='antonym' or type=='both'):
        raise NameError("type argument must be a either synonym, antonym or both.")
    

    # Get the correct meaning for the word based on sentence context
    sentence_list = str.split(sentence.translate(str.maketrans('', '', string.punctuation))) # Inspiration drawn from Stack Overflow : https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    word_with_context = lesk(sentence_list, word)

    # Get the antonyms and synonyms
    synonyms = set()
    antonyms = set() 
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma)
            for antonym in lemma.antonyms():
                antonyms.add(antonym)


    
    # Get the similarity scores
    syn_scores = similarity_score(word_with_context,synonyms)
    ant_scores = similarity_score(word_with_context,antonyms)


    # If there are no synonyms/antonyms for the word, ask the user if they want to try another type 
    if (len(syn_scores)==0 and (type=='synonym' or type=='both')) or (len(ant_scores)==0 and (type=='antonym' or type=='both')) :
        if type=='synonym' :
            print(f"There are no synonyms for {word} in this context.")
            return "You can try again with another word, try another meaning or get the antonym wordcloud."
        elif type=='antonym':
            print(f"There are no antonyms for {word} in this context.")
            return "You can try again with another word, try another meaning or get the synonym wordcloud."
        elif type=='both':
            if len(syn_scores)==0:
                print(f"There are no synonyms for {word} in this context.")
                type='antonym'
            if len(ant_scores)==0:
                print(f"There are no antonyms for {word} in this context.")
                type='synonym'
                    
    
    # Plot the wordclouds
    if type == 'synonym':
        return wordcloud_plotter(word, syn_scores,'synonym')
    elif type == 'antonym' :
        return wordcloud_plotter(word, ant_scores,'antonym')
    elif type == 'both':
        syn_wc = wordcloud_plotter(word, syn_scores,'synonym')
        ant_wc = wordcloud_plotter(word, ant_scores,'antonym')
        return syn_wc,ant_wc
    

