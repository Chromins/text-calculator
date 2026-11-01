import pytest

from rpn import to_rpn


@pytest.mark.parametrize(
    "expression, expected",
    [
        ([5, '+', 3], [5, 3, '+']),
        ([5, '+', 3, '*', 2], [5, 3, 2, '*', '+']),
        ([10, '-', 3, '-', 2], [10, 3, '-', 2, '-']),
        (['(', 5, '+', 3, ')', '*', 2], [5, 3, '+', 2, '*']),
        (['(', 5, '+', '(', 3, '*', 2, ')', ')'], 	[5, 3, 2, '*', '+'])
    ]
)
def test_to_rpn(expression, expected):
    assert to_rpn(expression) == expected


def test_to_rpn_double_unary_minus():
    assert to_rpn(['NEG', 'NEG', '(', 5, '+', 3, ')']) == [5, 3, '+', 'NEG', 'NEG']

def test_to_rpn_invalid_brackets1():
    with pytest.raises(ValueError):
        to_rpn([5, '+', 3, ')'])


def test_to_rpn_invalid_brackets2():
    with pytest.raises(ValueError):
        to_rpn(['(', 5, '+', 3])