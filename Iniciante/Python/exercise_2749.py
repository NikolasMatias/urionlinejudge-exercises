texto = 'x = 35'
print('-'*39)
for x in range(5):
    print('|', end='')
    if x == 0:
        print(texto, end='')
        print(' ' * (37-len(texto)), end='')
    elif x == 2:
        print(' ' * 15, end='')
        print(texto, end='')
        print(' ' * (37-len(texto)-15), end='')
    elif x == 4:
        print(' ' * (37-len(texto)), end='')
        print(texto, end='')
    else:
        print(' ' * 37, end='')
    print('|')
print('-'*39)