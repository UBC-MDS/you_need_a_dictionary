
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import pytest
from you_need_a_dictionary.sentiment_analysis import analyze_sentiment

def test_empty_string():
    with pytest.raises(Exception):
        analyze_sentiment("")

def test_sentiment_values():
    result = analyze_sentiment("I absolutely love Kpop")
    assert 'neg' in result
    assert 'neu' in result
    assert 'pos' in result
    assert 'compound' in result
    assert result['pos'] > result['neg']