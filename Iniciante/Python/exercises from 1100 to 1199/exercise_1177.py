number = int(input())
vetor = []
sequencia = 0

vetor.append(sequencia)

for x in range(999):
    if sequencia <= (number-2):
        sequencia += 1
    else:
        sequencia = 0

    vetor.append(sequencia)

for x in range(1000):
    print(''.join(['N[', str(x),'] = ', str(vetor[x])]))