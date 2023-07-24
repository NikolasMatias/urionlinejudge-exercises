valorA, valorB, valorC, valorD = [int(x) for x in input().split()]

isBBiggerThanC = valorB > valorC
isDBiggerThanA = valorD > valorA
isDPlusCBiggerThanAPlusB = (valorD + valorC) > (valorB + valorA)
isCAndDPositive = valorC >= 0 and valorD >= 0
isAPair = valorA%2 == 0

if isBBiggerThanC and isDBiggerThanA and isDPlusCBiggerThanAPlusB and isCAndDPositive and isAPair:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')