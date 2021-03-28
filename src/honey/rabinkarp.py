"""
Rabin-Karp Algorithm

Uses a rolling hash for expected linear time string-matching.

Given a string of length n and a substring of length m being searched for,
the steps are as follows:

1. Compute the substrings hash
2. Compute the hash of the first m characters of the string being searched
3. For each character in the string being searched, update the string's
rolling hash by subtracting off the left-most character and adding the next
character to the hash. Check whether the substring's hash matches the
rolling hash and, if so, check that the substrings themselves match. If
both match, we've found a match.

The algorithm runs in expected linear time because each step updates the
hash with one new character and compares the substring hashes. Assuming no
hash collisions, either the hashes don't match because the substrings don't
match, or the hashes do match and we've found the substring.

The algorithm still runs in worst-case O(mn) time because if we have a hash
collision, we have to compare m characters to check for a match. With a
good hash algorithm, the likelihood of such behavior is vanishingly small.
"""

_BASE = 256
_PRIME_MOD = 101


def _hash(string: str) -> int:
    """Hash function used for Rabin-Karp algorithm

    For a string length n with characters c_0, c_1, ..., c_n-1, the hash
    is computed as

    c_0*k^(n-1) + c_1*k^(n-2) + ... + c_n-1 * k^0

    The result is taken mod(prime) to prevent the hash from growing too large.
    """
    if not string:
        raise ValueError

    hash_ = 0

    for char in string[:-1]:
        hash_ += ord(char)
        hash_ %= _PRIME_MOD
        hash_ *= _BASE

    char = string[-1]
    hash_ += ord(char)
    return hash_ % _PRIME_MOD


def _pow_mod(base: int, exp: int, modulo: int) -> int:
    """Return base^exp % modulo"""
    result = 1
    for _ in range(exp):
        result = (result * base) % modulo

    return result


def _update_hash(
    current_hash: int, removed_char: str, added_char: str, str_len: int
) -> int:
    """Given a current hash, the character being removed from the left-end,
    and the character being added to the right-end, return the new hash
    value.

    When removing the left-most character, we take the current hash and
    subtract c*k^(n-1) where n is the length of the hashed string. We
    multiply the result by k because every existing weight is shifted by k,
    then we add the new character's value and take the result mod n.
    """
    if not len(removed_char) == len(added_char) == 1:
        raise ValueError

    removed_val = ord(removed_char)
    added_val = ord(added_char)

    left_base_offset = _pow_mod(_BASE, str_len - 1, _PRIME_MOD)
    return (
        (current_hash - removed_val * left_base_offset) * _BASE + added_val
    ) % _PRIME_MOD


def is_in(substring: str, string: str) -> bool:
    """Uses Rabin-Karp to return whether substring exists within string"""
    # empty substring always returns True
    if not substring:
        return True

    substr_hash = _hash(substring)
    substr_len = len(substring)
    string_hash = _hash(string[:substr_len])

    if string_hash == substr_hash and string[:substr_len] == substring:
        return True

    for index in range(len(string) - substr_len):
        # update the string's rolling hash by removing the character from
        # the left and adding the next character in the string
        string_hash = _update_hash(
            string_hash, string[index], string[index + substr_len], substr_len
        )

        # compare the hashes first, then the substring. Because Python uses
        # short-circuit evaluation, the substrings will only be compared if
        # the hashes match.
        if (
            string_hash == substr_hash
            and string[index + 1 : index + 1 + substr_len] == substring
        ):
            return True

    return False
