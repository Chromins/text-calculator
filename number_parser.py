#  Делает слова в число


UNITS = {
    'ноль': 0,
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9
}


TEENS = {
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19
}


TENS = {
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90
}


def parse_number(text):
    if not text or text.isspace():
        raise ValueError('Пустой ввод!')
    words = text.lower().split()
    if 1 <= len(words) <= 2:  #  Проверка длины ввода
        if len(words) == 1:
            words = words[0]
            if words in UNITS:  #  Проверка односложного ввода
                return UNITS[words]
            elif words in TEENS:
                return TEENS[words]
            elif words in TENS:
                return TENS[words]
            else:
                raise ValueError('Некорректный ввод!')
        elif len(words) == 2:
                if words[0] not in TENS:  #  Проверка на разряды в двусложном вводе
                    raise ValueError('Неверный ввод, ожидались десятки!')
                elif words[1] in UNITS and words[1] != 'ноль':
                    return TENS[words[0]] + UNITS[words[1]]
                else:
                    raise ValueError('Ожидались единицы!')
    else:
        raise ValueError('Некорректная строка!')
