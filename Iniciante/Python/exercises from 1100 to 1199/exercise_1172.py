vetor = {}

for x in range(10):
    vetor[x] = int(input())

for x in vetor.keys():
    if vetor[x] <= 0:
        vetor[x] = 1

for x in vetor.keys():
    print(''.join(['X[', str(x),'] = ', str(vetor[x])]))