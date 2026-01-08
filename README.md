# Welcome to You Need a Dictionary

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/you-need-a-dictionary.svg)](https://pypi.org/project/you-need-a-dictionary/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/you-need-a-dictionary.svg)](https://pypi.org/project/you-need-a-dictionary/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them.*
## Summary

You Need a Dictionary is a project that goes beyond simple translation and word definitions. It's an interactive tool for exploring how language choices shape meaning and sentiment. Users can analyze sentences, experiment with word substitutions, and visualize the emotional impact of their linguistic decisions. This tool assists writers and data scientists in understanding how specific vocabulary changes the sentiment and meaning of their text.

## List of Functions (A Reminder to replace this section with OUR ACTUAL FUNCTION NAMES)

- Process user input: Users input sentence and a word related to the sentence preprocessing happens (This is dependent on the input to the API)
- Analyze sentiment of the sentence: Use NLP to derive sentiment based on preprocessed user input
- Return definitions: Function returns the definition of the word(s)
- Analysis of replacement: If user opts to use this function then replace the word in the sentence with another word from the dictionary and then sentiment analysis function is called again on new sentence
- Whole sentence translation: User is also able to translate the entire sentence.
- Word cloud: Word Cloud for Antonyms/Synonyms

## `You Need a Dictionary's` Relevance to the Python Ecosystem:
There are several existing Python packages for NLP and dictionary lookups, such as [`PyDictionary`](https://pypi.org/project/PyDictionary/) for definitions and [`TextBlob`](https://textblob.readthedocs.io/en/dev/) or `NLTK` for sentiment analysis. However, **You Need a Dictionary** fills a specific gap by integrating these functionalities into a single workflow. Rather than returning isolated outputs like a sentiment score from [`TextBlob`](https://textblob.readthedocs.io/en/dev/) or a standalone definition from [`PyDictionary`](https://pypi.org/project/PyDictionary/), our package provides a cohesive experience providing insight into both the meaning of a word and its impact on the sentiment of a sentence. **You Need a Dictionary** also enables users to experiment how substituting a single word within a sentence can shift the overall sentiment, making it especially valuable for linguists, writers, and developers who need to understand not just what a word means, but how its replacement alters the emotional and semantic impact of text.


## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install you-need-a-dictionary
```

TODO: Add a brief example of how to use the package to this section

To use you-need-a-dictionary in your code:

```python
>>> import you-need-a-dictionary
>>> you-need-a-dictionary.hello_world()
```

## Contributors
- Eric Wong
- Mailys Guedon
- Godsgift Braimah
- Mara Sanchez


## Copyright

- Copyright © 2026 Mailys Guedon, Mara Sanchez, Godsgift Braimah, Eric Wong.
- Free software distributed under the [MIT License](./LICENSE).
