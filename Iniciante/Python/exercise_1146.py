valores = []

while True:
    valor = int(input())
    if valor == 0:
        break
    else:
        valores.append(valor)

for valor in valores:
    print(' '.join(str(x) for x in range(1, valor+1)))