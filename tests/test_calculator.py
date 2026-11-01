import pytest

from calculator import evaluate_rpn


@pytest.mark.parametrize(
    "tokens",
    [
        [5, 0, '/'],
        [0, 0, '/'],
        [10, 5, 5, '-', '/'],
        [3, 'NEG', 0, '/'],
    ]
)
def test_division_by_zero(tokens):
    with pytest.raises(ZeroDivisionError):
        evaluate_rpn(tokens)


@pytest.mark.parametrize(
    "tokens",
    [
        [7, 2, '/'],
        [1, 3, '/'],
        [10, 4, '/'],
        [7, 'NEG', 2, '/'],
        [2, 3, '/', 5, '+'],
    ]
)
def test_fractional_division(tokens):
    with pytest.raises(ValueError):
        evaluate_rpn(tokens)

@pytest.mark.parametrize(
    "tokens",
    [
        [5, '+'],
        [5, '-'],
        [5, '*'],
        [5, '/'],
        ['NEG'],
        [5, 'NEG', '+'],
        [5, 3, '+', '*'],
    ]
)
def test_insufficient_operands(tokens):
    with pytest.raises(ValueError):
        evaluate_rpn(tokens)

@pytest.mark.parametrize(
    "tokens",
    [
        [],
        [5, 3],
        [5, 3, '+', 7],
        [5, 3, 2, '+'],
        [5, 3, '^'],
        [5, 3, '%'],
    ]
)
def test_invalid_rpn(tokens):
    with pytest.raises(ValueError):
        evaluate_rpn(tokens)

@pytest.mark.parametrize(
    "tokens, expected",
    [
        ([8, 2, '/'], 4),
        ([0, 5, '/'], 0),
        ([12, 3, '/', 2, '*'], 8),
        ([8, 'NEG', 2, '/'], -4),
        ([8, 2, 'NEG', '/'], -4),
        ([8, 'NEG', 2, 'NEG', '/'], 4),
        ([5, 'NEG', 'NEG'], 5),
        ([10, 3, '-'], 7),
        ([10, 3, 'NEG', '-'], 13),
        ([5, 3, 'NEG', 2, '+', '*'], -5),
    ]
)
def test_valid_calculations(tokens, expected):
    assert evaluate_rpn(tokens) == expected

def test_integer_division_result_type():
    result = evaluate_rpn([8, 2, '/'])
    assert type(result) is int

def test_unknown_operator_with_extra_number():
    with pytest.raises(ValueError):
        evaluate_rpn([5, 3, '^', 7])