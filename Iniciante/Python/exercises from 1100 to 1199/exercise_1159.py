def sumEvenConsecutives(numberBase, times):
    soma = 0
    number_base = numberBase if numberBase%2 == 0 else numberBase+1

    for x in range(times):
        soma += number_base
        number_base += 2
    return soma
resultados = []

while True:
    numberBase = int(input())
    if not numberBase == 0:
        resultados.append(sumEvenConsecutives(numberBase, 5))
    else:
        break

for resultado in resultados:
    print(str(resultado))