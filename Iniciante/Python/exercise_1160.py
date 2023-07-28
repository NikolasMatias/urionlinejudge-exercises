def calculateProgressaoAritmetica(valorBase, progressao, anos):
    return valorBase + (anos -1)*(valorBase*(progressao/100))

def whenCityAWillBeBiggerThanCityB(
        populacaoA, porcentagemA, populacaoB, porcentagemB
):
    anos = 1
    while True:
        if calculateProgressaoAritmetica(populacaoA, porcentagemA, anos) < calculateProgressaoAritmetica(populacaoB,
                                                                                                         porcentagemB,
                                                                                                         anos):
            anos += 1
        else:
            break
    return anos

countLoop = int(input())
valores = []

for x in range(countLoop):
    print('cheguei aqui de novo gente')
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