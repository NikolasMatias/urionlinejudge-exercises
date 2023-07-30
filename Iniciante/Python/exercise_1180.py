def getMinorValue(vetor):
    key = 0
    value = vetor[0]
    for x in range(1, len(vetor)):
        if vetor[x] < value:
            key = x
            value = vetor[x]
    return [key, value]

countLoop = int(input())
valores = [int(x) for x in input().split()]
vetor = []

for x in range(countLoop):
    vetor.append(valores[x])

key, value = getMinorValue(vetor)

print(''.join(['Menor valor: ', str(value)]))
print(''.join(['Posicao: ', str(key)]))