valor_binario = input()
if valor_binario.count('1')%2 == 0:
    print(''.join([valor_binario, '0']))
else:
    print(''.join([valor_binario, '1']))