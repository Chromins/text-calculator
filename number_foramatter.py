#  Делает из слова числа


UNITS = {
    0: 'ноль',
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять'
}


TEENS = {
    10: 'десять',
    11: 'одиннадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'девятнадцать'
}


TENS = {
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    60: ' шестьдесят',
    70: 'семьдесят',
    80: 'восемьдесят',
    90: 'девяносто'
}


HUNDREDS = {
    100: 'сто',
    200: 'двести',
    300: 'триста',
    400: 'четыреста',
    500: 'пятьсот',
    600: 'шестьсот',
    700: 'семьсот',
    800: 'восемьсот',
    900: 'девятьсот'
}


THOUSANDS = {
    1000: 'одна тысяча',
    2000: 'две тысячи',
    3000: 'три тысячи',
    4000: 'четыре тысячи',
    5000: 'пять тысяч',
    6000: 'шесть тысяч',
    7000: 'семь тысяч',
    8000: 'восемь тысяч',
    9000: 'девять тысяч'
}


def number_format(number):
    result = []
    if type(number) is not int:
        raise ValueError('Ожидалось целое число!')  # Проверка типа ввода
    elif number == 0:  # Обработка нуля
        result.append(UNITS[0])
    elif number < 0:  # Отрицательные числа
        result.append('минус')
        number = abs(number)
    divisor = 10 ** (len(str(number)) - 1)  # определитель разряда для последующего цикла
    if divisor > 1000:  # Пока ограничение от -9999 до 9999
        raise ValueError('Число длиннее ожидаемого!')
    else:  # Основная вевть цикла
        while number > 0:
            divisor = 10 ** (len(str(number)) - 1)
            digit = number // divisor
            key = divisor * digit
            if divisor == 1000:
                result.append(THOUSANDS[key])
            elif divisor == 100:
                result.append(HUNDREDS[key])
            elif divisor == 10:
                if 10 <= number <= 19:  # Проверка на интервал от 10 до 19
                    result.append(TEENS[number])
                    number = 0
                else:
                    result.append(TENS[key])
            else:
                result.append(UNITS[number])
                number = 0
            number %= divisor
    return ' '.join(result)  # Вывод функции в формате строки





















