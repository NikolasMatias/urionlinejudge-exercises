valorN = int(input())
valores = [0,1]

for x in range(valorN-2):
    valores.append(valores[-1]+valores[-2])

print(' '.join(str(x) for x in valores))