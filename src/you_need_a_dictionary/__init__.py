"""
This module contains all the imports necessary for our functions.

"""

from you_need_a_dictionary.fetch_definition import fetch_definition
from you_need_a_dictionary.sentiment_analysis import analyze_sentiment
from you_need_a_dictionary.translate_sentence import translate_sentence
from you_need_a_dictionary.word_replacement import word_replacement
from you_need_a_dictionary.wordcloud import create_wordcloud

__all__ = ['word_replacement','create_wordcloud','fetch_definition','analyze_sentiment','translate_sentence']
