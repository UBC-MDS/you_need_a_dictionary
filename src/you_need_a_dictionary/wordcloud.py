"""
A module that creates wordclouds of antonyms and/or synonyms for a given word.

"""
import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud

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
    >>> create_wordcloud('car', 'The car is on the road', 'antonym')

    >>> create_wordcloud('happy')
    
    """
    if not isinstance(word, str):
        raise TypeError("word argument must be a string.")
    
    if not isinstance(sentence, str):
        raise TypeError("sentence argument must be a string.")
    
    if not isinstance(type, str):
        raise TypeError("type argument must be a string.")

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
    
    # Plot the wordclouds
    if type == 'synonym':
        fig, ax = plt.subplots(figsize=(7,7))
        wordcloud_plotter(ax, word, syn_scores)
        return fig
    elif type == 'antonym' :
        fig, ax = plt.subplots(figsize=(7,7))
        wordcloud_plotter(ax, word, ant_scores)
        return fig
    elif type == 'both':
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
        wordcloud_plotter(ax1, word, syn_scores)
        wordcloud_plotter(ax2, word, ant_scores)
        return fig

    

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
    if not isinstance(basis, nltk.corpus.reader.wordnet.Synset):
        raise TypeError("Basis must be a wordnet synset.")
    
    if not isinstance(lemmas, set):
        raise TypeError("Lemmas must be a set")
    
    if not all(isinstance(value, nltk.corpus.reader.wordnet.Lemma) for value in lemmas):
        raise TypeError("All the values in lemmas must be a wordnet lemma")
    
    scores = {}
    for word in lemmas:
        if word.name() == basis.name().split(".")[0].replace('_',' '):
            continue   
        scores[word.name()]=basis.path_similarity(word.synset())
    return scores

def wordcloud_plotter(central_word,word_dic,type):
    """
    This function plots a wordcloud.

    This function was developed with the help of ChatGPT to determine how to position the points to reduce overlap.

    Parameters
    ----------
    central_word : str
        The central word in the wordcloud.
    word_dic : dictionary
        A dictionary mapping words (str) to their similarity scores (float, range 0–1)
    type : str
        Defines what type of wordcloud it is
    

    Returns
    -------
    plt.Figure
        A Matplotlib figure of a wordcloud containing antonyms and/or synonyms for a given word. 

    Examples
    --------
    >>> wordcloud_plotter('car',{'door':0.083, 'cat': 0.056,'wheel': 0.091,'automobile':1.0})
        
    """
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

    plt.title(f'{type} Wordcloud for {central_word} ',pad=10, fontweight='bold')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off") 
    plt.show()