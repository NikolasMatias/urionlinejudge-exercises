def whenCityAWillBeBiggerThanCityB(
        populacaoA, porcentagemA, populacaoB, porcentagemB
):
    PA = populacaoA
    PB = populacaoB
    anos = 0
    while PB >= PA:
        PA += int((PA*porcentagemA)/100)
        PB += int((PB*porcentagemB)/100)
        anos += 1

        if anos > 100:
            break
    return anos

countLoop = int(input())
valores = []

for x in range(countLoop):
    result = input().split()
    populacaoA = int(result[0])
    populacaoB = int(result[1])
    porcentagemA = float(result[2])
    porcentagemB = float(result[3])
    valores.append(whenCityAWillBeBiggerThanCityB(populacaoA,porcentagemA, populacaoB, porcentagemB))

for valor in valores:
    if valor > 100:
        print('Mais de 1 seculo.')
    else:
        print(''.join([str(valor), ' anos.']))