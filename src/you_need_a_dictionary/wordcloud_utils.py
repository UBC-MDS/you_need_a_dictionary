"""
A module that creates helper functions to find similarity scores between a given word and its synonym/antonym 
as well as plotting wordclouds.

Functions:
- similarity_score
- wordcloud_plotter
"""
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def similarity_score(basis,lemmas):
    """
    This function finds the score of similarity strength between two words.

    The similarity score can be found using the NLTK wordnet 
    package and ranges between 0 and 1 where:
     - 1 : strong similarity 
     - 0 : weak similarity.

    Parameters
    ----------
    basis : nltk.corpus.reader.wordnet.Synset
        The word we are comparing to.
    lemmas : set
        A set of lemmas we want to compare the word to. The values in the set must have nltk.corpus.reader.wordnet.Lemma data type

    Returns
    -------
    Dictionary
        A dictionary mapping words (str) to their similarity scores (float, range 0–1)

    Examples
    --------
    >>> similarity_score(wn.synset('car.n.01'),{wn.lemma('door.n.01.door'), wn.lemma('cat.n.01.cat'), wn.lemma('wheel.n.01.wheel'), wn.lemma('car.n.01.automobile')})
        {'door':0.083, 'cat': 0.056,'wheel': 0.091,'automobile':1.0}

    """

    # Check that basis input has correct type
    if not isinstance(basis, nltk.corpus.reader.wordnet.Synset):
        raise TypeError("Basis must be a wordnet synset.")
    
    # Check that lemmas input is a set
    if not isinstance(lemmas, set):
        raise TypeError("Lemmas must be a set")
    
    # Check that the values in lemmas set have correct type
    if not all(isinstance(value, nltk.corpus.reader.wordnet.Lemma) for value in lemmas):
        raise TypeError("All the values in lemmas must be a wordnet lemma")
    
    scores = {}
    for word in lemmas:
        if word.name() == basis.name().split(".")[0].replace('_',' '):
            continue   
        scores[word.name()]=basis.path_similarity(word.synset())
    return scores

def wordcloud_plotter(given_word,word_dic,type):
    """
    This function plots a wordcloud.

    The size of the word indicate how similar it is to our given word.
    This means that the larger the word, the more similar it is.
    Colour is also used to indicate words with same scores.

    Parameters
    ----------
    given_word : str
        The given word that we want to plot the wordcloud for.
    word_dic : dictionary
        A dictionary mapping words (str) to their similarity scores (float, range 0–1)
    type : str
        Defines what type of wordcloud it is. Either 'synonym' or 'antonym'.
    

    Returns
    -------
    plt.Figure
        A Matplotlib figure of a wordcloud containing antonyms or synonyms for a given word. 

    Examples
    --------
    >>> wordcloud_plotter('car',{'door':0.083, 'cat': 0.056,'wheel': 0.091,'automobile':1.0},'antonym')
        
    """
    
    # Check that given_word input is a string
    if not isinstance(given_word, str):
        raise TypeError("given_word argument must be a string.")
    
    # Check that word_dic input is a string
    if not isinstance(word_dic, dict):
        raise TypeError("word_dic argument must be a dictionary.")
    
    # Check that values in word_dic are floats
    if not all(isinstance(value, float) for value in word_dic.values()):
        raise TypeError("values in word_dic argument must be floats.")
    
    # Check that keys in word_dic are strings
    if not all(isinstance(keys, str) for keys in word_dic):
        raise TypeError("keys in word_dic argument must be strings.")
    
    # Check that values in word_dic are between 0 and 1
    if not all(0 <= value <= 1 for value in word_dic.values()):
        raise TypeError("values in word_dic argument must be between 0 and 1.")
    
    # Check that type input is a string
    if not isinstance(type, str):
        raise TypeError("type argument must be a string.")
    
    # Set of scores 
    score_set = sorted(set(word_dic.values()), reverse=True)


    max_size = 100
    min_size = 10

    # The difference in size between words is based on the score rank 
    step = (max_size - min_size)/max(1,len(score_set)-1)

    score_dic = {}

    # Assign a score based on score rank (i.e words with same score have same size)
    for syn in word_dic:
        score_dic[syn]=max_size-score_set.index(word_dic[syn])*step

    # Plot wordcloud
    wordcloud = WordCloud(width=1000, height=700, background_color='white', random_state=8).generate_from_frequencies(score_dic)

    plt.title(f'{type.capitalize()} Wordcloud for {given_word} ',pad=10, fontweight='bold', fontsize = 20)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off") 
    plt.show()

    return plt.gcf()

 
