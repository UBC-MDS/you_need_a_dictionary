# Welcome to You Need a Dictionary

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/you-need-a-dictionary.svg)](https://pypi.org/project/you-need-a-dictionary/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/you-need-a-dictionary.svg)](https://pypi.org/project/you-need-a-dictionary/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |


## Summary

**You Need a Dictionary** is a project that goes beyond simple translation and word definitions. It's an interactive tool for exploring how language choices shape meaning and sentiment. Users can analyze sentences, experiment with word substitutions, and visualize the emotional impact of their linguistic decisions. This tool assists writers and data scientists in understanding how specific vocabulary changes the sentiment and meaning of their text.

## List of Functions

- `get_user_input`: Accepts a raw string and a target word as input from the user.
- `preprocess_user_input`: Preprocessing of user input to prepare the text for NLP analysis and API integration.
- `analyze_sentiment`: Analyzes the preprocessed text using NLP techniques to derive a sentiment polarity score, helping users understand the emotional tone of their input.
- `fetch_definition`: Module that fetches the definition, synonyms and antonyms of a given word using WordNet
- `word_replacement`: Replaces a specific word in the user's sentence with a synonym or antonym specified by the user and automatically re-runs the sentiment analysis to compare the emotional shift in polarity score.
- `translate_sentence`: Translates the entire input sentence into a target language using LibreTranslate.
- `create_wordcloud`: Generates a visual word cloud of synonyms and antonyms for a specific word, providing a pictorial representation of related words.

## `You Need a Dictionary's` Relevance to the Python Ecosystem:

There are several existing Python packages for NLP and dictionary lookups, such as [`PyDictionary`](https://pypi.org/project/PyDictionary/) for definitions and [`TextBlob`](https://textblob.readthedocs.io/en/dev/) or `NLTK` for sentiment analysis. However, **You Need a Dictionary** fills a specific gap by integrating these functionalities into a single workflow. Rather than returning isolated outputs like a sentiment score from [`TextBlob`](https://textblob.readthedocs.io/en/dev/) or a standalone definition from [`PyDictionary`](https://pypi.org/project/PyDictionary/), our package provides a cohesive experience providing insight into both the meaning of a word and its impact on the sentiment of a sentence. **You Need a Dictionary** also enables users to experiment how substituting a single word within a sentence can shift the overall sentiment, making it especially valuable for linguists, writers, and developers who need to understand not just what a word means, but how its replacement alters the emotional and semantic impact of text.


## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install you-need-a-dictionary
```

To use you-need-a-dictionary in your code:

```python
>>> import you-need-a-dictionary
>>> you-need-a-dictionary.hello_world()
```

## Language codes

The following language codes are used:

| Language              | Code |
|-----------------------|------|
| Albanian              | sq   |
| Arabic                | ar   |
| Azerbaijani           | az   |
| Basque                | eu   |
| Bengali               | bn   |
| Bulgarian             | bg   |
| Catalan               | ca   |
| Chinese (traditional) | zt   |
| Chinese               | zh   |
| Czech                 | cs   |
| Danish                | da   |
| Dutch                 | nl   |
| English               | en   |
| Esperanto             | eo   |
| Estonian              | et   |
| Finnish               | fi   |
| French                | fr   |
| Galician              | gl   |
| German                | de   |
| Greek                 | el   |
| Hebrew                | he   |
| Hindi                 | hi   |
| Hungarian             | hu   |
| Indonesian            | id   |
| Irish                 | ga   |
| Italian               | it   |
| Japanese              | ja   |
| Korean                | ko   |
| Kyrgyz                | ky   |
| Latvian               | lv   |
| Lithuanian            | lt   |
| Malay                 | ms   |
| Norwegian             | nb   |
| Persian               | fa   |
| Polish                | pl   |
| Portuguese            | pt   |
| Portuguese (Brazil)   | pb   |
| Romanian              | ro   |
| Russian               | ru   |
| Slovak                | sk   |
| Slovenian             | sl   |
| Spanish               | es   |
| Swedish               | sv   |
| Tagalog               | tl   |
| Thai                  | th   |
| Turkish               | tr   |
| Ukranian              | uk   |
| Urdu                  | ur   |
| Vietnamese            | vi   |

## Dev notes

To contribute to the development of this package, please follow these steps after cloning the repository:
Set up a virtual environment using conda:

```bash
$ conda create -n environment.yml
$ conda activate you-need-a-dictionary
``` 

To install the package locally:
```bash
$ pip install -e .
``` 

To test the package locally:
Open a terminal in the project root directory and run:
```bash
$ pip install -e .[tests] # setup test dependencies
$ pytest
```

To build documentation locally:
```bash
$ pip install -e .[docs] # setup documentation dependencies
$ quartodoc --build
$ quarto render
```

## Contributors
- Eric Wong
- Mailys Guedon
- Godsgift Braimah
- Mara Sanchez


## Copyright

- Copyright © 2026 Mailys Guedon, Mara Sanchez, Godsgift Braimah, Eric Wong.
- Free software distributed under the [MIT License](./LICENSE).


