"""
Module that fetches a sentence's translation and metadata through the LibreTranslate API.
"""


def translate_sentence(sentence, target_language, source_language=None):
    """
    Translate an input sentence into a target language using LibreTranslate.

    This function sends the input sentence to the LibreTranslate API and returns
    the translated text along with additional metadata. By default, the source
    language is automatically detected by the translation service. If an error
    occurs during translation, the original sentence is returned and error
    information is included in the output.

    Parameters
    ----------
    sentence : string
        The input sentence to be translated.
    target_language : string
        The target language code (e.g., 'es' for Spanish, 'fr' for French).
    source_language : string, optional
        The source language code of the input sentence. If None, the source
        language is automatically detected by LibreTranslate. Default is None.

    Returns
    -------
    dict
        A dictionary containing the translation result and metadata with the
        following keys:

        - 'translated_text' : string
          The translated sentence.
        - 'source_language' : string
          The detected or specified source language code.
        - 'target_language' : string
          The target language code used for translation.
        - 'confidence' : float or None
          A confidence score provided by the translation service, if available.
        - 'provider' : string
          The translation provider used ('LibreTranslate').
        - 'error' : string or None
          An error message if the translation failed; otherwise None.

    Examples
    --------
    >>> translate_sentence("Hello world", "es")

    >>> translate_sentence("Bonjour tout le monde", "en")

    >>> translate_sentence("Hello world", "fr", source_language="en")
    """
