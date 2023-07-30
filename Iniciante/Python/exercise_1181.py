linha = int(input())
operacao = str(input())
matriz = []
for x in range(12):
    matriz.append([])

for x in range(12):
    for y in range(12):
        matriz[x].append(float(input()))

if operacao == 'S':
    print('{:.1f}'.format(sum(matriz[linha])))
elif operacao == 'M':
    print('{:.1f}'.format(sum(matriz[linha])/len(matriz[linha])))