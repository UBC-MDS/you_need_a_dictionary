"""
Module that fetches a sentence's translation and metadata through Google Translate.
"""


def translate_sentence(sentence, target_language, source_language=None):
    """
    Translate an input sentence into a target language using Google Translate.

    This function sends the input sentence to Google Translate and returns
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
        language is automatically detected. Default is None.

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
        - 'error' : string or None
          An error message if the translation failed; otherwise None.

    Examples
    --------
    >>> translate_sentence("Hello world", "es")
    >>> translate_sentence("Bonjour tout le monde", "en")
    >>> translate_sentence("Hello world", "fr", source_language="en")
    """
    from deep_translator import GoogleTranslator

    try:
        # Basic validation
        if not isinstance(sentence, str):
            raise TypeError("sentence must be a string")
        if not isinstance(target_language, str):
            raise TypeError("target_language must be a string")
        if source_language is not None and not isinstance(source_language, str):
            raise TypeError("source_language must be a string or None")

        # Use 'auto' for automatic detection if source_language is None
        source = source_language if source_language else "auto"

        # Perform translation
        translated_text = GoogleTranslator(
            source=source, target=target_language
        ).translate(sentence)

        return {
            "translated_text": translated_text,
            "source_language": source,
            "target_language": target_language,
            "error": None,
        }

    except Exception as e:
        return {
            "translated_text": sentence,
            "source_language": source_language,
            "target_language": target_language,
            "error": str(e),
        }
