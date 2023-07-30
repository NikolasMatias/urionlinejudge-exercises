valorS = 0.0
valorBase = 1
expoente = 1
baseDivisor = 2
divisor = 1

for x in range(20):
    valorS += valorBase/divisor
    valorBase += 2
    divisor = baseDivisor**expoente
    expoente += 1

print('{:.2f}'.format(valorS))