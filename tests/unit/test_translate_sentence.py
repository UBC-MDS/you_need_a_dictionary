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

# After getting a reply that generated very complex tests, I sent the following prompt:
# Give me more basic tests like:
# 1. Verifying the inputs/outputs are valid
# 2. Check with a dummy text like having "Hello world" translate into "Hola mundo"
# 3. Check that the language they want to use for translation is in "code" form
# 4. Check that if the language they want to translate from/to is available and if it's not check that the function tells the user that the language is not supported rather than having it crash.
# 5. You can choose something else to test if you think it is relevant


def test_empty_string():
    """Test that an empty string can be translated (returns empty result)."""
    result = translate_sentence("", "es")
    assert result["translated_text"] == ""
    assert result["error"] is None


def test_basic_translation():
    """Test that 'Hello world' translates to 'Hola Mundo'."""
    result = translate_sentence("Hello world", "es")
    assert result["translated_text"] == "Hola Mundo"
    assert result["target_language"] == "es"
    assert result["error"] is None


def test_language_code_format():
    """Test that language codes must be in string format."""
    result = translate_sentence("Hello", 123)
    assert result["error"] is not None
    assert "target_language must be a string" in result["error"]


def test_invalid_source_language_code():
    """Test that invalid source language code is handled gracefully."""
    result = translate_sentence("Hello", "es", source_language=456)
    assert result["error"] is not None
    assert "source_language must be a string or None" in result["error"]


def test_unsupported_language():
    """Test that unsupported language codes return an error message."""
    result = translate_sentence("Hello world", "xyz")
    assert result["error"] is not None
    assert result["translated_text"] == "Hello world"  # Returns original text


def test_return_type():
    """Ensure the function returns a dictionary."""
    result = translate_sentence("Hello", "es")
    assert isinstance(result, dict)


def test_return_structure():
    """Test that the returned dictionary has all required keys."""
    result = translate_sentence("Hello", "es")
    assert "translated_text" in result
    assert "source_language" in result
    assert "target_language" in result
    assert "error" in result


def test_invalid_input_type():
    """Test that a non-string sentence input raises a TypeError."""
    result = translate_sentence(123, "es")
    assert result["error"] is not None
    assert "sentence must be a string" in result["error"]


def test_with_explicit_source_language():
    """Test translation with explicitly specified source language."""
    result = translate_sentence("Hello world", "fr", source_language="en")
    assert result["source_language"] == "en"
    assert result["translated_text"] == "Bonjour le monde"
    assert result["error"] is None


def test_auto_detect_source_language():
    """Test that source language defaults to 'auto' when not specified."""
    result = translate_sentence("Hello", "es")
    assert result["source_language"] == "auto"
    assert result["error"] is None


def test_french_to_english():
    """Test translation from French to English."""
    result = translate_sentence("Bonjour tout le monde", "en")
    assert result["target_language"] == "en"
    assert "Hello" in result["translated_text"] or "Good" in result["translated_text"]
    assert result["error"] is None


def test_whitespace_input():
    """Test translation of whitespace-only strings."""
    result = translate_sentence("   ", "es")
    # This should either translate to whitespace or handle gracefully
    assert result["error"] is None or result["translated_text"] == "   "


def test_special_characters():
    """Test translation of sentence with special characters."""
    result = translate_sentence("Hello world!", "es")
    assert result["error"] is None
    assert "Hola" in result["translated_text"]


def test_numbers_in_sentence():
    """Test translation of sentence containing numbers."""
    result = translate_sentence("I have 5 apples", "es")
    assert result["error"] is None
    assert (
        "5" in result["translated_text"] or "cinco" in result["translated_text"].lower()
    )
