import math

valores = [int(x) for x in input().split()]
valores.sort()
valorA, valorB = valores

valorK = valorB/valorA
isMultiple = (valorK - math.floor(valorK)) == 0.0

if isMultiple:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')