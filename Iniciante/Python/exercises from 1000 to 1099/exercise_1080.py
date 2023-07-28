maiorValor = 0
index = 0

for x in range(100):
    valorAtual = int(input())
    if valorAtual > maiorValor:
        maiorValor = valorAtual
        index = x+1

print(str(maiorValor))
print(str(index))