def sumConsecutiveNumbers(firstNumber, times):
    soma = 0
    for x in range(times):
        soma += firstNumber
        firstNumber += 1
    return soma

valorX = int(input())
valorZ = 0

while True:
    if valorZ > valorX:
        break
    valorZ = int(input())

count = 1

while True:
    if sumConsecutiveNumbers(valorX, count) < valorZ:
        count += 1
    else:
        break

print(str(count))