soma = 0
numbers = []

for x in range(2):
    numbers.append(int(input()))

maiorValor, menorValor = numbers

for x in range((menorValor+1), maiorValor):
    if x%2 != 0:
        soma += x

print(soma)