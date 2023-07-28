def sumAllOddNumbersBetweenTwoValues(valorA, valorB):
    soma = 0
    menor_valor = valorA if valorA < valorB else valorB
    maior_valor = valorA if valorA > valorB else valorB

    for x in range((menor_valor + 1), maior_valor):
        if x % 2 != 0:
            soma += x
    return soma

countLoop = int(input())
somas = []

for x in range(countLoop):
    valorA, valorB = [int(y) for y in input().split()]
    somas.append(sumAllOddNumbersBetweenTwoValues(valorA, valorB))

for soma in somas:
    print(soma)