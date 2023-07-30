vetor = {}

for x in range(100):
    vetor[x] = float(input())

for x in vetor.keys():
    if vetor[x] <= 10:
        print(''.join(['A[', str(x), '] = ', str(vetor[x])]))