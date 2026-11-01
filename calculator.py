#  Делает вычисления

def evaluate_rpn(tokens):
    stack = []

    for token in tokens:
        if isinstance(token, int):
            stack.append(token)
        elif token == 'NEG' and len(stack) > 0:
            stack.append(-(stack.pop()))
        elif token in ['+', '-', '*', '/']:
            if len(stack) < 2:
                raise ValueError('Некорректная запись операндов!')
            else:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                elif token == '/':
                    if a != 0:
                        if b % a == 0:
                            stack.append(b // a)
                        else:
                            raise ValueError('Не делится нацело!')
                    else:
                        raise ZeroDivisionError('На ноль делить нельзя!')
        else:
            raise ValueError('Некорректный операнд!')
    if len(stack) == 1:
        return stack.pop()
    else:
        raise ValueError('Некорректный ОПН!')