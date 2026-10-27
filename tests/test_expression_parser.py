import pytest

from expression_parser import parse_expression


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("пять", [5]),
        ("пять плюс три", [5, '+', 3]),
        ("двадцать пять минус семь", [25, '-', 7]),
        ("пять плюс три умножить два", [5, '+', 3, '*', 2]),
    ]
)
def test_parse_expression(expression, expected):
    assert parse_expression(expression) == expected


def test_invalid_order_operators():
    with pytest.raises(ValueError):
        parse_expression("пять плюс умножить три")


def test_invalid_order_expressions():
    with pytest.raises(ValueError):
        parse_expression("плюс пять")


def test_undefined_words():
    with pytest.raises(ValueError):
        parse_expression("двадцать яблоко")


def test_void_expressions():
    with pytest.raises(ValueError):
        parse_expression("")