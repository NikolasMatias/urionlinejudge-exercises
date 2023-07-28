valorX, valorY = [int(x) for x in input().split()]
valores = []
count = 0

for x in range(1, valorY+1):
    if len(valores) > 0 and len(valores[count]) == valorX:
        count += 1
    if len(valores) > 0 and (count+1) <= len(valores):
        valores[count].append(x)
    else:
        valores.insert(count, [x])

for valor in valores:
    print(' '.join(str(x) for x in valor))