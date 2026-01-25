# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0]

- Added four tests (two tests in test_create_wordcloud.py and two in test_sentiment_analysis.py)
- Created quarto documentation structure and initial files. Hosted on GitHub Pages.


## [1.0.0]

- Added definition fetch code and unit tests: test_fetch_definition.py and fetch_definition.py
- Added sentiment analysis code and unit tests: test_sentiment_analysis.py and sentiment_analysis.py
- Added function logic to replace a word in a sentence and compute the sentiment in word_replacement.py
- Added helper function sentiment_specifics in utils.py to provide detailed sentiment analysis results.
- Added wordcloud plotter code and unit tests: test_create_wordcloud.py and wordcloud.py
- Added helper functions similarity_score and wordcloud_plotter for plotting wordclouds: wordcloud_utils.py
- Updated README.md to incude instructions on now to test package locally
- Fixed imports in word_replacement.py to use package structure instead of sys.path

## [2.0.0]

- Added documentation to the readme.md including installing, running tests, and building docs
