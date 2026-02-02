"""
Module that fetches the definition, synonyms and antonyms of a given word using WordNet.
"""


def fetch_definition(
    word,
    pos=None,  # "n", "v", "a", "r" or None (noun [n], verb [v], adjective [a], adverb [r])
    top_n=1,  # number of definitions to return
    max_synonyms=10,
    include_examples=False,
    return_type="str",  # string/dictionary
):
    """
    Fetch definitions, synonyms, and antonyms of a word using WordNet.

    Parameters
    ----------
    word : str
        The word to look up.
    pos : {"n","v","a","r"}, optional
        Part of speech filter: noun (n), verb (v), adjective (a), adverb (r).
        If None, returns results for all parts of speech. Default is None.
    top_n : int, default=1
        Number of top-ranked senses to include.
    max_synonyms : int, default=10
        Max number of synonyms to show (combined across returned senses).
    include_examples : bool, default=False
        If True, include example sentences when available.
    return_type : str, default="str"
        Format for returned results (currently supports "str").

    Returns
    -------
    str
        Formatted string of word definition, senses, synonyms, and antonyms.

    Raises
    ------
    LookupError
        If WordNet resource is not available.
    TypeError
        If word is not a string.
    ValueError
        If word is empty or pos is not valid.

    Examples
    --------
    >>> fetch_definition("happy")
    Word: happy
    Sense 1 (a): feeling or showing pleasure or contentment
    Synonyms: cheerful, gay, glad, joyful, joyous, lighthearted, pleased
    Antonyms: sad, unhappy

    >>> fetch_definition("run", pos="v", top_n=2)
    Word: run
    Sense 1 (v): move fast by using one's legs
    Sense 2 (v): flee; take to one's heels; cut and run
    Synonyms: bolt, dash, escape, flow, gallop, go, hurry, jog, move, operate
    Antonyms: None found
    """
    from nltk.corpus import wordnet as wn

    # ====== INPUT VALIDATION ======

    # WordNet availability check
    try:
        wn.synsets("test")
    except LookupError as e:
        raise LookupError(
            "WordNet resource not found. Run:\n"
            "  nltk.download('wordnet')\n"
            "  nltk.download('omw-1.4')"
        ) from e

    # Check input is a string
    if not isinstance(word, str):
        raise TypeError("word must be a string.")
    word = word.strip()

    # Check input is not empty
    if not word:
        raise ValueError("word must be a non-empty string.")

    # Check the user inputs a valid classification for the word
    if pos is not None and pos not in {"n", "v", "a", "r"}:
        raise ValueError("pos must be one of {'n','v','a','r'} or None.")

    # Check if the word is in wordnet
    synsets = wn.synsets(word, pos=pos)
    if not synsets:
        return f"No definition found for '{word}'."

    # Rank synsets (synonyms) by total word frequency (for a specific meaning)
    def synset_score(s):
        score = 0
        for lemma in s.lemmas():
            if lemma.name().lower() == word.lower():
                score += lemma.count()
        return score

    # Rank all meanings of the word from most to least common
    synsets_sorted = sorted(synsets, key=synset_score, reverse=True)
    chosen = synsets_sorted[: max(1, int(top_n))]

    # Collect info
    senses = []
    synonyms = set()
    antonyms = set()

    # Give examples of use for each definition
    for s in chosen:
        sense = {
            "name": s.name(),
            "definition": s.definition(),
            "pos": s.pos(),
        }

        if include_examples:
            sense["examples"] = s.examples()

        senses.append(sense)

        # synonyms and antonyms from words in this synset
        for lemma in s.lemmas():
            synonyms.add(lemma.name().replace("_", " "))

            for ant in lemma.antonyms():
                antonyms.add(ant.name().replace("_", " "))

    # Remove the input word from the synonyms
    synonyms = {s for s in synonyms if s.lower() != word.lower()}

    # Limit synonyms shown (default 10)
    synonyms_list = sorted(synonyms)[:max_synonyms]
    antonyms_list = sorted(antonyms)

    # Format output to display in string
    lines = [f"Word: {word}"]
    for i, s in enumerate(senses, start=1):
        lines.append(f"Sense {i} ({s['pos']}): {s['definition']}")
        if include_examples and s.get("examples"):
            for ex in s["examples"][:2]:
                lines.append(f"  e.g., {ex}")

    lines.append(
        f"Synonyms: {', '.join(synonyms_list) if synonyms_list else 'None found'}"
    )
    lines.append(
        f"Antonyms: {', '.join(antonyms_list) if antonyms_list else 'None found'}"
    )

    return "\n".join(lines)
