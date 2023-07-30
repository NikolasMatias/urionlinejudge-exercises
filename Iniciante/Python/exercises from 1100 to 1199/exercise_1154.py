valores = []

while True:
    valor = int(input())
    if valor >= 0:
        valores.append(valor)
    else:
        break

print('{:.2f}'.format(sum(valores)/len(valores)))