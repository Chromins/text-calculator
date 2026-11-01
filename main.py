#  Сама функция calc()
from expression_parser import parse_expression

from rpn import to_rpn

from calculator import evaluate_rpn

from number_foramatter import number_format


def calc(expression):
    tokens = parse_expression(expression)
    rpn = to_rpn(tokens)
    result = evaluate_rpn(rpn)
    answer = number_format(result)
    return answer
while True:
    expression = input('Введите выражение: ')
    if expression.strip().lower() == 'конец':
        break
    try:
        print(f'Ответ: {calc(expression)}')
    except (ValueError, ZeroDivisionError) as error:
        print(f'Ошибка: {error}')