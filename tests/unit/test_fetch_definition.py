"""
Unit tests for the fetch_definition module.
"""
import pytest
import you_need_a_dictionary as ynd

# Below test cases were obtained with prompt: Hi, based on the following function <insert fetch_definition docstring>
# create pytest unit tests to validate that it works properly.


def _skip_if_wordnet_missing():
    """
    Helper: skip tests that require WordNet if the NLTK WordNet resource
    isn't available in the environment.
    """
    try:
        # Any call will trigger your internal WordNet availability check
        ynd.fetch_definition("test")
    except LookupError:
        pytest.skip("WordNet resource not available (nltk wordnet/omw not downloaded).")


def test_invalid_type():
    """Test that a non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="word must be a string."):
        ynd.fetch_definition(123)


def test_empty_string():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="word must be a non-empty string."):
        ynd.fetch_definition("")


def test_whitespace_input():
    """Test that a whitespace-only string raises a ValueError."""
    with pytest.raises(ValueError, match="word must be a non-empty string."):
        ynd.fetch_definition("     ")


def test_invalid_pos():
    """Test that an invalid part-of-speech code raises a ValueError."""
    _skip_if_wordnet_missing()
    with pytest.raises(ValueError, match=r"pos must be one of"):
        ynd.fetch_definition("run", pos="x")


def test_word_not_found():
    """Test that an unknown word returns the 'No definition found' message."""
    _skip_if_wordnet_missing()
    nonsense = "asdkfjhasdkfjh"
    result = ynd.fetch_definition(nonsense)
    assert result == f"No definition found for '{nonsense}'."


def test_top_n_controls_number_of_senses():
    """Test that top_n controls how many sense lines are returned."""
    _skip_if_wordnet_missing()
    result = ynd.fetch_definition("run", top_n=3)
    sense_lines = [line for line in result.splitlines() if line.startswith("Sense ")]
    assert len(sense_lines) == 3


def test_max_synonyms_cap():
    """Test that max_synonyms limits the number of synonyms displayed."""
    _skip_if_wordnet_missing()
    max_syn = 3
    result = ynd.fetch_definition("happy", max_synonyms=max_syn)

    # Find synonyms line and count items
    synonyms_line = next(
        line for line in result.splitlines() if line.startswith("Synonyms:")
    )
    synonyms_str = synonyms_line.replace("Synonyms:", "").strip()

    if synonyms_str == "None found":
        assert True  # valid: 0 synonyms
    else:
        synonyms_list = [s.strip() for s in synonyms_str.split(",") if s.strip()]
        assert len(synonyms_list) <= max_syn


def test_no_examples_when_disabled():
    """Test that examples are not included when include_examples is False."""
    _skip_if_wordnet_missing()
    result = ynd.fetch_definition("run", include_examples=False)
    assert "e.g.," not in result
