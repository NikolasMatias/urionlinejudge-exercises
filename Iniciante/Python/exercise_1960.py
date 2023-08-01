def int_to_roman(number):
    int_base = [
        1000, 900, 500, 400, 100, 90,
        50, 40, 10, 9, 5, 4, 1
    ]
    roman_base = [
        'M', 'CM', 'D', 'CD', 'C', 'XC', 'L',
        'XL', 'X', 'IX', 'V', 'IV', 'I'
    ]
    for x in int_base:
        if number // x: