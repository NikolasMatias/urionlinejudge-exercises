def isNotTriangle(valorA, valorB, valorC):
    return valorA >= (valorB+valorC)

def isRightTriangle(valorA, valorB, valorC):
    return valorA**2 == (valorB**2+valorC**2)

def isObtusangleTriangle(valorA, valorB, valorC):
    return valorA**2 > (valorB**2+valorC**2)

def isAcuteTriangle(valorA, valorB, valorC):
    return valorA ** 2 < (valorB ** 2 + valorC ** 2)

def isEquilateralTriangle(valorA, valorB, valorC):
    return valorA == valorB and valorB == valorC

def isIsoscelesTriangle(valorA, valorB, valorC):
    return valorA == valorB or valorB == valorC or valorA == valorC

valores = [float(x) for x in input().split()]
valores.sort(reverse=True)
valorA, valorB, valorC = valores

if isNotTriangle(valorA, valorB, valorC):
    print('NAO FORMA TRIANGULO')
elif isRightTriangle(valorA, valorB, valorC):
    print('TRIANGULO RETANGULO')
elif isObtusangleTriangle(valorA, valorB, valorC):
    print('TRIANGULO OBTUSANGULO')
elif isAcuteTriangle(valorA, valorB, valorC):
    print('TRIANGULO ACUTANGULO')

if isEquilateralTriangle(valorA, valorB, valorC):
    print('TRIANGULO EQUILATERO')
elif isIsoscelesTriangle(valorA, valorB, valorC):
    print('TRIANGULO ISOSCELES')