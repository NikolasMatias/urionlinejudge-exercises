def hasOnlyPositiveValues(numbers):
    if isinstance(numbers, list) and len(numbers) > 0:
        for number in numbers:
            if number <= 0:
                return False
        return True
    return True

def sumNumbersBetweenTwoValues(valorA, valorB):
    soma = 0
    menor_valor = valorA if valorA < valorB else valorB
    maior_valor = valorA if valorA > valorB else valorB
    rangeValues = range(menor_valor, maior_valor+1)

    for x in rangeValues:
        soma += x

    return [rangeValues, soma]

listResults = []

while len(listResults) == 0 or hasOnlyPositiveValues(listResults[-1]):
    valorA, valorB = [int(x) for x in input().split()]
    listResults.append([valorA, valorB])

listResults.pop()

for result in listResults:
    values, soma = sumNumbersBetweenTwoValues(result[0], result[1])
    print(''.join([' '.join(str(x) for x in values), ' Sum=', str(soma)]))