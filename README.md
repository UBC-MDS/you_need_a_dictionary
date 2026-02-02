# Welcome to You Need a Dictionary

[![codecov](https://codecov.io/gh/UBC-MDS/you_need_a_dictionary/graph/badge.svg?token=IIfAQEEKTp)](https://codecov.io/gh/UBC-MDS/you_need_a_dictionary)
## Summary

**You Need a Dictionary** is a project that goes beyond simple translation and word definitions. It's an interactive tool for exploring how language choices shape meaning and sentiment. Users can analyze sentences, experiment with word substitutions, and visualize the emotional impact of their linguistic decisions. This tool assists writers and data scientists in understanding how specific vocabulary changes the sentiment and meaning of their text.

## List of Functions

- `analyze_sentiment`: Analyzes the preprocessed text using NLP techniques to derive a sentiment polarity score, helping users understand the emotional tone of their input.
- `fetch_definition`: Module that fetches the definition, synonyms and antonyms of a given word using WordNet
- `word_replacement`: Replaces a specific word in the user's sentence with a synonym or antonym specified by the user and automatically re-runs the sentiment analysis to compare the emotional shift in polarity score.
- `translate_sentence`: Translates the entire input sentence into a target language using LibreTranslate.
- `create_wordcloud`: Generates a visual word cloud of synonyms and antonyms for a specific word, providing a pictorial representation of related words.

## Documentation

Full documentation, tutorials, and examples are available on the [project website](https://ubc-mds.github.io/you_need_a_dictionary/).

## `You Need a Dictionary's` Relevance to the Python Ecosystem:

There are several existing Python packages for NLP and dictionary lookups, such as [`PyDictionary`](https://pypi.org/project/PyDictionary/) for definitions and [`TextBlob`](https://textblob.readthedocs.io/en/dev/) or `NLTK` for sentiment analysis. However, **You Need a Dictionary** fills a specific gap by integrating these functionalities into a single workflow. Rather than returning isolated outputs like a sentiment score from [`TextBlob`](https://textblob.readthedocs.io/en/dev/) or a standalone definition from [`PyDictionary`](https://pypi.org/project/PyDictionary/), our package provides a cohesive experience providing insight into both the meaning of a word and its impact on the sentiment of a sentence. **You Need a Dictionary** also enables users to experiment how substituting a single word within a sentence can shift the overall sentiment, making it especially valuable for linguists, writers, and developers who need to understand not just what a word means, but how its replacement alters the emotional and semantic impact of text.

## Language Codes

The following language codes are supported for translation:
<details>
<summary>Language codes</summary>

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

</details>

## Get started

You can install this package into your preferred Python environment using pip:

```bash
pip install -i https://test.pypi.org/simple/ you-need-a-dictionary
```

For more information, you can find the package on Test-PyPi [here](https://test.pypi.org/project/you-need-a-dictionary/).

Example usage in Python:
```python
import you_need_a_dictionary as ynd
ynd.analyze_sentiment("I love programming!")
```

The model returns a sentiment label and a confidence score. A higher score means the model is more confident in its prediction.
```python
{
  "neg": 0.0,
  "neu": 0.182,
  "pos": 0.818,
  "compound": 0.6696
}
```


## Dev notes

To contribute to the development of this package, please follow these steps after cloning the repository:
Set up a virtual environment using conda:

```bash
conda env create -f environment.yml
conda activate you_need_a_dictionary
``` 

To install the package locally:
```bash
pip install -e .
``` 

To test the package locally:
Open a terminal in the project root directory and run:
```bash
pip install -e .[tests] # setup test dependencies
pytest
```

To build documentation locally:
```bash
pip install -e .[docs] # setup documentation dependencies
quartodoc --build
quarto render
```

## Contributors
- Eric Wong
- Mailys Guedon
- Godsgift Braimah
- Mara Sanchez


## Copyright

- Copyright © 2026 Mailys Guedon, Mara Sanchez, Godsgift Braimah, Eric Wong.
- Free software distributed under the [MIT License](./LICENSE).


