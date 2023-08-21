print('-'*39)
for x in range(5):
    print('|', end='')
    if x == 0:
        print(' ' * 8, end='')
        print('Roberto', end='')
        print(' ' * 22, end='')
    elif x == 2:
        print(' ' * 8, end='')
        print('5786', end='')
        print(' ' * 25, end='')
    elif x == 4:
        print(' ' * 8, end='')
        print('UNIFEI', end='')
        print(' ' * 23, end='')
    else:
        print(' ' * 37, end='')
    print('|')
print('-'*39)