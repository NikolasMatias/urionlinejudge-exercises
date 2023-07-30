def findOwnDividers(number):
    dividersList = []
    for x in range(1, number):
        if (number/x) == int(number/x):
            dividersList.append(x)
    return dividersList

countLoop = int(input())
valores = []

for x in range(countLoop):
    number = int(input())
    dividers = findOwnDividers(number)
    if sum(dividers) == number:
        valores.append(''.join([str(number), ' eh perfeito']))
    else:
        valores.append(''.join([str(number), ' nao eh perfeito']))

for valor in valores:
    print(valor)