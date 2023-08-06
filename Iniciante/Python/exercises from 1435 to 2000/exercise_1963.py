valor_antigo, valor_novo = [float('{:.2f}'.format(float(x))) for x in input().split()]
diferenca = valor_novo - valor_antigo
porcentagem = diferenca*100/valor_antigo
print(''.join(['{:.2f}'.format(porcentagem), '%']))