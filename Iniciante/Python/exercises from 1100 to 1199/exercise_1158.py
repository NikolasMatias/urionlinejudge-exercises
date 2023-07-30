def calculateOddConsecutives(numberBase, times):
    soma = 0
    number_base = numberBase if not numberBase%2 == 0 else numberBase+1

    for x in range(times):
        soma += number_base
        number_base += 2
    return soma

countLoop = int(input())
resultados = []

for x in range(countLoop):
    numberBase, times = [int(y) for y in input().split()]
    resultados.append(calculateOddConsecutives(numberBase, times))

for resultado in resultados:
    print(str(resultado))