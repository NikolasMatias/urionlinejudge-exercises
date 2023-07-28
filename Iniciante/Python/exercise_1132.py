valorA = int(input())
valorB = int(input())

menorValor = valorA if valorA < valorB else valorB
maiorValor = valorA if valorA > valorB else valorB

valores = list(
    filter(lambda valor: valor % 13 != 0, range(menorValor, maiorValor+1))
)

print(str(sum(valores)))