vetorImpar = []
vetorPar = []

for x in range(15):
    number = int(input())
    if number%2 == 0:
        vetorPar.append(number)
    else:
        vetorImpar.append(number)

    if len(vetorImpar) == 5:
        for y in range(5):
            print(''.join(['impar[', str(y), '] = ', str(vetorImpar[y])]))
        vetorImpar = []

    if len(vetorPar) == 5:
        for y in range(5):
            print(''.join(['par[', str(y), '] = ', str(vetorPar[y])]))
        vetorPar = []

for y in range(len(vetorImpar)):
    print(''.join(['impar[', str(y), '] = ', str(vetorImpar[y])]))

for y in range(len(vetorPar)):
    print(''.join(['par[', str(y), '] = ', str(vetorPar[y])]))