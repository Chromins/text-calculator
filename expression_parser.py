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
    for word in words:
        if word not in OPERATORS:
            number_words.append(word)
        else:
            if number_words:
                tokens.append(parse_number(' '.join(number_words)))
                tokens.append(OPERATORS[word])
                number_words = []
            else:
                raise ValueError('Неправильный порядок!')
    if tokens or number_words:
        tokens.append(parse_number(' '.join(number_words)))
    else:
        raise ValueError('Пустой ввод!')
    return tokens










