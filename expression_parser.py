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
    for word in words:
        if word not in OPERATORS:
            number_words.append(word)
        else:
            if number_words:
                tokens.append(parse_number(' '.join(number_words)))
                number_words = []
                expect_number = False
            if word == 'минус' and expect_number:
                tokens.append('NEG')
            else:
                if not expect_number:
                    tokens.append(OPERATORS[word])
                    expect_number = True
                else:
                    raise ValueError('Неправильный порядок!')
    if number_words:
        tokens.append(parse_number(' '.join(number_words)))
        expect_number = False
    if not tokens:
        raise ValueError('Пустой ввод!')
    if expect_number:
        raise ValueError('Незаконченное выражение!')
    return tokens









