countPar = 0
countImpar = 0
countPositivo = 0
countNegativo = 0

for x in range(5):
    number = int(input())
    if number%2 == 0:
        countPar += 1
    if number%2 != 0:
        countImpar += 1
    if number > 0:
        countPositivo += 1
    if number < 0:
        countNegativo += 1

print(''.join([str(countPar), ' valor(es) par(es)']))
print(''.join([str(countImpar), ' valor(es) impar(es)']))
print(''.join([str(countPositivo), ' valor(es) positivo(s)']))
print(''.join([str(countNegativo), ' valor(es) negativo(s)']))