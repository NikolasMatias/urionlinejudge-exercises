def int_to_roman(number):
    result = ''
    resto = number
    int_to_roman_base = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    keys = list(int_to_roman_base.keys())
    for x in sorted(keys, reverse=True):
        n_times = resto // x
        resto = resto % x
        if n_times > 0:
            result = result + int_to_roman_base[x]*n_times
    return result

valor_a = int(input())
print(int_to_roman(valor_a))