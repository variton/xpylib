import pytest

from typehdr.strhdr import StrHdr
from typehdr.listhdr import ListHdr


@pytest.mark.parametrize(
    "_l, expected",
    [
        (
            ["I", "am", "the", "'blue'", "spectrum"],
            ["I", "am", "the", "blue", "spectrum"],
        ),
        (
            ["I", "am", "the", '"blue"', "spectrum"],
            ["I", "am", "the", "blue", "spectrum"],
        ),
    ],
)
def test_mutate(_l, expected):
    assert ListHdr.mutate(_l, StrHdr.detect_embedded_str) == expected


def test_mutate_empty():
    assert ListHdr.mutate([], StrHdr.detect_embedded_str) == []
