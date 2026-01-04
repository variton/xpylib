import pytest

from typehdr.strhdr import StrHdr


@pytest.mark.parametrize(
    "_s, expected",
    [
        ('"hello"', True),
        ("'world'", True),
        ("hello", False),
        ("", False),
        ("\"mismatch'", False),
        ("'mismatch\"", False),
        ('""', True),  # empty content but quoted
        ("''", True),  # empty content but quoted
        ('"a"', True),
        ("'a'", True),
        ("'a", False),  # missing closing quote
        ('a"', False),  # missing opening quote
        ("`a`", False),  # unsupported quote type
        (" ", False),  # single char, not a quote
        ('I am the "blue" spectrum', True),
    ],
)


def test_detect_embedded_str(_s, expected):
    assert StrHdr.detect_embedded_str(_s) is expected

def test_detect_embedded_str_does_not_raise_on_empty():
    # Implementation explicitly handles empty strings
    assert StrHdr.detect_embedded_str("") is False

@pytest.mark.parametrize(
    "input_s, expected",
    [
        ("hello world", ["hello", "world"]),
        ("one   two\tthree\nfour", ["one", "two", "three", "four"]),  # mixed whitespace
        ("  spaced words  ", ["spaced", "words"]),                   # leading/trailing spaces
        ("", []),                                                    # empty string
        ("single", ["single"]),                                      # no whitespace
        ("a\nb\r\nc\td", ["a", "b", "c", "d"]),                       # newline variants + tab
    ],
)

def test_str_to_list_splits_on_whitespace(input_s: str, expected: list[str]) -> None:
    assert StrHdr.str_to_list(input_s) == expected

def test_str_to_list_preserves_token_text() -> None:
    # punctuation remains part of tokens (split doesn't strip punctuation)
    assert StrHdr.str_to_list("hi, there!") == ["hi,", "there!"]

def test_str_to_list_returns_list_type() -> None:
    result = StrHdr.str_to_list("a b")
    assert isinstance(result, list)
    assert all(isinstance(x, str) for x in result)
