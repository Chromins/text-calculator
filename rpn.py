#  С обычной записи в польскую обратную
PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def to_rpn(tokens):
    operators = []
    output = []

    for token in tokens:
        if isinstance(token, int):
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if not operators:
                raise ValueError('Лишняя закрывающая скобка!')
            operators.pop()
        else:
            while operators and operators[-1] != '(' and PRECEDENCE[token] <= PRECEDENCE[operators[-1]]:
                output.append(operators.pop())
            operators.append(token)
    while operators:
        if operators[-1] != '(':
            output.append(operators.pop())
        else:
            raise ValueError('Некорректный ввод!')
    return output

























