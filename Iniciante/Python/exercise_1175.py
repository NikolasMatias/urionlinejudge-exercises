vetor = []

for x in range(20):
    vetor.append(int(input()))

for x in range(20):
    if x > 9:
        break
    valor1 = vetor[(x*(-1))-1]
    vetor[(x * (-1)) - 1] = vetor[x]
    vetor[x] = valor1

for x in range(20):
    print(''.join(['N[', str(x), '] = ', str(vetor[x])]))