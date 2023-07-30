number = int(input())
vetor = {}

for x in range(10):
    if x == 0:
        vetor[x] = number
    else:
        vetor[x] = vetor[x-1]*2

for x in vetor.keys():
    print(''.join(['N[', str(x),'] = ', str(vetor[x])]))