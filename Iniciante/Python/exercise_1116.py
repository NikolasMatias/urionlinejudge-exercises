countLoop = int(input())
resultList = []

for y in range(countLoop):
    valorA, valorB = [int(x) for x in input().split()]
    resultList.append([valorA, valorB])

for result in resultList:
    valorA, valorB = [float(x) for x in result]
    if valorB == 0:
        print('divisao impossivel')
    else:
        print("{:.1f}".format(valorA/valorB))