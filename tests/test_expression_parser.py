import pytest

from expression_parser import parse_expression


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("минус пять", ['NEG', 5]),
        ("пять минус три", [5, '-', 3]),
        ("пять минус минус три", [5, '-', 'NEG', 3]),
        ("минус минус пять", ['NEG', 'NEG', 5]),
        ("пять плюс минус три", [5, '+', 'NEG', 3]),
        ("минус двадцать пять умножить два",
         ['NEG', 25, '*', 2]),
        ("десять делить минус два", [10, '/', 'NEG', 2]),
        ("ноль минус минус ноль", [0, '-', 'NEG', 0]),
    ]
)
def test_unary_minus(expression, expected):
    assert parse_expression(expression) == expected


@pytest.mark.parametrize(
    "expression",
    [
        "",
        "минус",
        "пять минус",
        "минус минус",
        "плюс пять",
        "пять плюс умножить три",
        "минус плюс пять",
        "пять умножить делить три",
        "пять минус плюс два",
    ]
)
def test_invalid_expression(expression):
    with pytest.raises(ValueError):
        parse_expression(expression)


def test_undefined_words():
    with pytest.raises(ValueError):
        parse_expression("двадцать яблоко")


def test_void_expressions():
    with pytest.raises(ValueError):
        parse_expression("")

def test_correct_negative_expressions():
    assert parse_expression("двадцать пять минус минус три") == [25, '-', 'NEG', 3]