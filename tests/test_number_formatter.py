import pytest

from number_foramatter import number_format


@pytest.mark.parametrize(
    "number, expected",
    [
        (7, "семь"),
        (45, "сорок пять"),
        (115, "сто пятнадцать"),
        (0, "ноль"),
        (100, "сто"),
        (1000, "одна тысяча"),
        (1001, "одна тысяча один"),
        (2015, "две тысячи пятнадцать"),
        (9999, "девять тысяч девятьсот девяносто девять"),
        (-579, "минус пятьсот семьдесят девять")
    ]
)
def test_valid_number(number, expected):
    assert number_format(number) == expected

def test_invalid_type():
    with pytest.raises(ValueError):
        number_format("яблоко")


def test_invalid_type2():
    with pytest.raises(ValueError):
        number_format(3.14)


def test_invalid_length():
    with pytest.raises(ValueError):
        number_format(10000)


def test_bool():
    with pytest.raises(ValueError):
        number_format(True)
