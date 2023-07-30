valor = int(input())
valores = []

rangeValores = list(
    filter(lambda valor: valor%4 > 0, range(1, (4*valor)+1))
)

count = 0
for x in rangeValores:
    if len(valores) > 0 and len(valores[count]) == 3:
        count += 1
    if len(valores) > 0 and (count+1) <= len(valores):
        valores[count].append(x)
    else:
        valores.insert(count, [x])
for valor in valores:
    print(''.join([' '.join(str(x) for x in valor), ' PUM']))