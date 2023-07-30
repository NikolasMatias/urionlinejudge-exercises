operacao = str(input())
matriz = []
values = []
for x in range(12):
    matriz.append([])

for x in range(12):
    for y in range(12):
        matriz[x].append(float(input()))
        if y > x and (x+y) < 11:
            values.append(matriz[x][y])

if operacao == 'S':
    print('{:.1f}'.format(sum(values)))
elif operacao == 'M':
    print('{:.1f}'.format(sum(values)/len(values)))