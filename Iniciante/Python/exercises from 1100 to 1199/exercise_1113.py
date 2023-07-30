def hasDifferentValues(numbers):
    valorA, valorB = numbers
    return valorA != valorB

listResults = []

while len(listResults) == 0 or hasDifferentValues(listResults[-1]):
    valorA, valorB = [int(x) for x in input().split()]
    listResults.append([valorA, valorB])

listResults.pop()

for result in listResults:
    valorA, valorB = result
    if valorA > valorB:
        print('Decrescente')
    else:
        print('Crescente')