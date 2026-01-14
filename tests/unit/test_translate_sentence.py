"""
Unit tests for the translate_sentence module.
"""

import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

import pytest
from you_need_a_dictionary.translate_sentence import translate_sentence

# Below test cases were obtained with prompt: Hi, based on the following function <insert translate_sentence docstring>
# create pytest unit tests to validate that it works properly.

# After getting a reply than generated very complex tests, I sent the following prompt:
# Give me more basic tests like:
# 1. Verifying the inputs/outputs are valid
# 2. Check with a dummy text like having "Hello world" translate into "Hola mundo"
# 3. Check that the language they want to use for translation is in "code" form
# 4. Check that if the language they want to translate from/to is available and if it's not check that the function tells the user that the language is not supported rather than having it crash.
# 5. You can choose something else to test if you think it is relevant

# Supported languages for translation
SUPPORTED_CODES = {
    "sq",
    "ar",
    "az",
    "eu",
    "bn",
    "bg",
    "ca",
    "zt",
    "zh",
    "cs",
    "da",
    "nl",
    "en",
    "eo",
    "et",
    "fi",
    "fr",
    "gl",
    "de",
    "el",
    "he",
    "hi",
    "hu",
    "id",
    "ga",
    "it",
    "ja",
    "ko",
    "ky",
    "lv",
    "lt",
    "ms",
    "nb",
    "fa",
    "pl",
    "pt",
    "pb",
    "ro",
    "ru",
    "sk",
    "sl",
    "es",
    "sv",
    "tl",
    "th",
    "tr",
    "uk",
    "ur",
    "vi",
}

EXPECTED_KEYS = {
    "translated_text",
    "source_language",
    "target_language",
    "confidence",
    "provider",
    "error",
}


def assert_valid_schema(out):
    assert isinstance(out, dict)
    assert EXPECTED_KEYS.issubset(out.keys())
    assert isinstance(out["translated_text"], str)
    assert isinstance(out["target_language"], str)
    assert isinstance(out["provider"], str)
    assert out["error"] is None or isinstance(out["error"], str)
    assert out["confidence"] is None or isinstance(out["confidence"], (int, float))


def assert_raises_or_returns_error(*args, **kwargs):
    """
    Accept either:
    - ValueError raised (recommended), OR
    - returned dict with 'error' not None
    """
    try:
        out = translate_sentence(*args, **kwargs)
    except ValueError:
        return None

    assert_valid_schema(out)
    assert out["error"] is not None
    return out


# 1) Verifying the inputs/outputs are valid
def test_output_has_expected_schema(monkeypatch):
    # Mock success response so we don't call the real API
    import requests

    class DummyResponse:
        status_code = 200

        def json(self):
            return {
                "translatedText": "Hola mundo",
                "detectedLanguage": {"language": "en"},
            }

    monkeypatch.setattr(requests, "post", lambda *a, **k: DummyResponse())

    out = translate_sentence("Hello world", "es")
    assert_valid_schema(out)
    assert out["provider"] == "LibreTranslate"


# 2) "Hello world" -> "Hola mundo"
def test_translates_hello_world_to_hola_mundo(monkeypatch):
    import requests

    class DummyResponse:
        status_code = 200

        def json(self):
            return {
                "translatedText": "Hola mundo",
                "detectedLanguage": {"language": "en"},
            }

    monkeypatch.setattr(requests, "post", lambda *a, **k: DummyResponse())

    out = translate_sentence("Hello world", "es")
    assert_valid_schema(out)
    assert out["translated_text"] == "Hola mundo"
    assert out["target_language"] == "es"
    assert out["error"] is None


# 3) Check that target language is in "code" form (i.e., in your supported set)
@pytest.mark.parametrize("bad_code", ["Spanish", "EN", "e", "en-US", ""])
def test_target_language_must_be_supported_code(bad_code):
    assert_raises_or_returns_error("Hello", bad_code)


# 4) If source/target language not supported, function should not crash
def test_unsupported_target_language_returns_clear_error():
    out = assert_raises_or_returns_error("Hello", "xx")
    if out is not None:
        assert (
            "not supported" in out["error"].lower()
            or "unsupported" in out["error"].lower()
        )


def test_unsupported_source_language_returns_clear_error():
    out = assert_raises_or_returns_error("Hola", "en", source_language="xx")
    if out is not None:
        assert (
            "not supported" in out["error"].lower()
            or "unsupported" in out["error"].lower()
        )


# 5) Extra relevant test: empty sentence should be handled gracefully
def test_empty_sentence_handled_gracefully():
    out = assert_raises_or_returns_error("", "es")
    if out is not None:
        # If your "graceful error" approach returns original input on error:
        assert out["translated_text"] == ""
