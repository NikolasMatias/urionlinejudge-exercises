number = float(input())
vetor = [number]

for x in range(1, 100):
    vetor.append(vetor[x-1]/2)

for x in range(100):
    print(''.join(['N[', str(x),'] = ', '{:.4f}'.format(vetor[x])]))