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
