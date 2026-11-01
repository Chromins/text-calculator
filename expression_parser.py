#  Разбор выражений и вычислений
from number_parser import parse_number

OPERATORS = {
    'плюс': '+',
    'минус': '-',
    'умножить': '*',
    'делить': '/'
}


def parse_expression(expression):
    words = expression.split()
    tokens = []
    number_words = []
    expect_number = True
    bracket_depth = 0

    def finish_number():
        nonlocal number_words, expect_number
        if not number_words:
            return
        tokens.append(parse_number(' '.join(number_words)))
        number_words = []
        expect_number = False

    for word in words:
        if word == 'скобка':
            finish_number()
            if expect_number:
                tokens.append('(')
                bracket_depth += 1
            elif not expect_number and bracket_depth > 0:
                tokens.append(')')
                bracket_depth -= 1
                expect_number = False
            else:
                tokens.append('*')
                tokens.append('(')
                bracket_depth += 1
                expect_number = True
        elif word in OPERATORS:
            finish_number()
            if word == 'минус' and expect_number:
                tokens.append('NEG')
            else:
                if not expect_number:
                    tokens.append(OPERATORS[word])
                    expect_number = True
                else:
                    raise ValueError('Неправильный порядок!')
        else:
            if expect_number:
                number_words.append(word)
            else:
                if tokens[-1] == ')':
                    tokens.append('*')
                    number_words.append(word)
                    expect_number = True
                else:
                    raise ValueError('Неправильный порядок!')
    finish_number()
    if not tokens:
        raise ValueError('Пустой ввод!')
    if expect_number:
        raise ValueError('Незаконченное выражение!')
    if bracket_depth > 0:
        raise ValueError('Незаконченное подвыражение!')
    return tokens








