valorA = int(input())
valorB = int(input())

menorValor = min([valorA, valorB])
maiorValor = max([valorA, valorB])

for x in range(menorValor+1, maiorValor):
    if x%5 in [2,3]:
        print(x)