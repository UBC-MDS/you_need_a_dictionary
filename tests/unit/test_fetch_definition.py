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

# If you could add two impactful unit tests in addition to the tests in test_fetch_definition.py, 
# what would they be? Apply coding best practices and look for edge cases as well.

def test_antonyms_returned_for_word_with_opposites():
    """Test that antonyms are returned for words that have them."""
    _skip_if_wordnet_missing()
    # "good" has well-known antonyms like "bad", "evil", etc.
    result = ynd.fetch_definition("good", top_n=1)
    lines = result.splitlines()
    
    antonyms_line = next(
        (line for line in lines if line.startswith("Antonyms:")), None
    )
    assert antonyms_line is not None, "Antonyms line should be present"
    assert "None found" not in antonyms_line, "Antonyms should not be empty for 'good'"
    
    # Verify antonyms are comma-separated and non-empty
    antonyms_str = antonyms_line.replace("Antonyms:", "").strip()
    antonyms_list = [a.strip() for a in antonyms_str.split(",")]
    assert len(antonyms_list) > 0
    assert all(isinstance(a, str) and len(a) > 0 for a in antonyms_list)


def test_pos_filter_restricts_results():
    """Test that filtering by part-of-speech returns only matching senses."""
    _skip_if_wordnet_missing()
    # "run" is both noun and verb; filter to only verbs
    result_verb = ynd.fetch_definition("run", pos="v", top_n=2)
    verb_senses = [line for line in result_verb.splitlines() if line.startswith("Sense ")]
    
    # All returned senses should show verb POS
    for sense_line in verb_senses:
        assert "(v)" in sense_line, f"Expected verb POS in: {sense_line}"
    
    # Verify we actually got results
    assert len(verb_senses) > 0, "Should return at least one verb sense for 'run'"
