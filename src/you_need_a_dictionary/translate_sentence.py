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
        - 'error' : string or None
          An error message if the translation failed; otherwise None.

    Examples
    --------
    >>> translate_sentence("Hello world", "es")

    >>> translate_sentence("Bonjour tout le monde", "en")

    >>> translate_sentence("Hello world", "fr", source_language="en")
    """

    from libretranslatepy import LibreTranslateAPI

    lt = LibreTranslateAPI("https://libretranslate.com/")

    try:
        confidence = None

        # Basic validation
        if not isinstance(sentence, str):
            raise TypeError("sentence must be a string")
        if not isinstance(target_language, str):
            raise TypeError("target_language must be a string")
        if source_language is not None and not isinstance(source_language, str):
            raise TypeError("source_language must be a string or None")

        # Auto-detect source language if not provided
        if source_language is None:
            detection = lt.detect(sentence)

            if detection:
                source_language = detection[0].get("language")
                confidence = detection[0].get("confidence")

            # If detection didn't give us a language, fallback to "auto"
            if not source_language:
                source_language = "auto"

        # Perform translation
        translated_text = lt.translate(sentence, source_language, target_language)

        return {
            "translated_text": translated_text,
            "source_language": source_language,
            "target_language": target_language,
            "confidence": confidence,
            "error": None,
        }

    except Exception as e:
        return {
            "translated_text": sentence,
            "source_language": source_language,
            "target_language": target_language,
            "confidence": None,
            "error": str(e),
        }
