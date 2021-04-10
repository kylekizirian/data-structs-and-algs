"""
Tests for Rabin-Karp implementation
"""
from unicodedata import category

from hypothesis import given, strategies as st

from honey import rabinkarp


@given(st.data())
def test_rabin_karp(data):
    """Tests Rabin-Karp against randomly generated strings

    Generate a string, then take random splice from the string. Assert that
    the splice always exists within the string. Generate another random
    string and check our Rabin-Karp implementation against Python's
    built-in `in` keyword.
    """
    char_categories = [category("a"), category("A"), category("0")]
    string = data.draw(
        st.text(st.characters(whitelist_categories=char_categories), min_size=1)
    )

    substr_start = data.draw(st.integers(max_value=len(string)))
    substr_end = data.draw(st.integers(min_value=substr_start, max_value=len(string)))
    substr = string[substr_start:substr_end]

    random_str = data.draw(
        st.text(st.characters(whitelist_categories=char_categories), min_size=1)
    )

    # substr was selected from string so it's guaranteed to exist within
    # string
    assert rabinkarp.is_in(substr, string)

    # compare our Rabin-Karp implementation of two random strings to
    # Python's built-in `in` implementation
    assert rabinkarp.is_in(random_str, string) == (random_str in string)
