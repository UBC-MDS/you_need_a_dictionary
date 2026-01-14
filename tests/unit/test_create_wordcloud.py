"""
A test module that tests the wordcloud function.
"""
import matplotlib.pyplot as plt
from src.you_need_a_dictionary.wordcloud import create_wordcloud
import pytest

def test_create_wordcloud():

    results = create_wordcloud('door')

    # Verify return type 
    assert isinstance(results, plt.Figure)