print('-'*39)
showDecimalTitle = False
showOctalTitle = False
showHexadecimalTitle = False
for x in range(39):
    if (x+1) in [1, 13, 23, 39]:
        print('|', end='')
    elif not showDecimalTitle and x+1 in range(4, 4+len('decimal')):
        print('decimal', end='')
        showDecimalTitle = True
    elif not showOctalTitle and x+1 in range(16, 16+len('octal')):
        print('octal', end='')
        showOctalTitle = True
    elif not showHexadecimalTitle and x+1 in range(26, 26+len('Hexadecimal')):
        print('Hexadecimal', end='')
        showHexadecimalTitle = True
    elif x+1 not in range(4, 4+len('decimal')) and x+1 not in range(16, 16+len('octal')) and x+1 not in range(26, 26+len('Hexadecimal')):
        print(' ', end='')
    if x+1 == 39:
        print()
print('-'*39)
for y in range(16):
    showDecimalNumber = False
    showOctalNumber = False
    showHexadecimalNumber = False
    for x in range(39):
        if (x + 1) in [1, 13, 23, 39]:
            print('|', end='')
        elif not showDecimalNumber and x + 1 in range(7, 9):
            print(str(y).rjust(2), end='')
            showDecimalNumber = True
        elif not showOctalNumber and x + 1 in range(17, 19):
            print(str(oct(y)).replace('0o', '').rjust(2), end='')
            showOctalNumber = True
        elif not showHexadecimalNumber and x + 1 in range(30, 32):
            print(str(hex(y)).replace('0x', '').upper().rjust(2), end='')
            showHexadecimalNumber = True
        elif x + 1 not in range(7, 9) and x + 1 not in range(17, 19) and x + 1 not in range(30, 32):
            print(' ', end='')
        if x + 1 == 39:
            print()
print('-'*39)