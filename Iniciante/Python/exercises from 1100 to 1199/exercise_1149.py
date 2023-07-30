valores = [int(x) for x in input().split()]
valorA = valores.pop(0)
valorN = valores.pop(0)
soma = 0

if valorN <= 0:
    for valor in valores:
        if valor > 0:
            valorN = valor
            break

for x in range(valorN):
    soma += valorA
    valorA += 1

print(str(soma))