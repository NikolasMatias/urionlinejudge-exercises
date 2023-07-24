def isTriangle(valorA, valorB, valorC):
    isAPlusBBiggerThanC = valorA+valorB > valorC
    isBPlusCBiggerThanA = valorB+valorC > valorA
    isAPlusCBiggerThanB = valorA+valorC > valorB
    return isAPlusCBiggerThanB and isBPlusCBiggerThanA and isAPlusBBiggerThanC

valorA, valorB, valorC = [float(x) for x in input().split()]

if isTriangle(valorA, valorB, valorC):
    perimetro = valorA+valorB+valorC
    print('Perimetro = '+ "{:.1f}".format(perimetro))
else:
    area = ((valorA+valorB)*valorC)/2
    print('Area = '+ "{:.1f}".format(area))
