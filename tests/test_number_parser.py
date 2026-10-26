import pytest

from number_parser import parse_number


@pytest.mark.parametrize(
    " text,expected ",
    [
        ("семь", 7),
        ("пятнадцать", 15),
        ("сорок", 40),
        ("сорок пять", 45),
        ("ноль", 0),
        ("девяносто девять", 99)
    ]
)
def test_parse_number(text, expected):
    assert parse_number(text) == expected


def test_invalid_word():
    with pytest.raises(ValueError):
        parse_number("яблоко")