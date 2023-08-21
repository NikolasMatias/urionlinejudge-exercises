def is_triangle(valor_a, valor_b, valor_c):
    is_A_plus_B_bigger_than_C = valor_a+valor_b > valor_c
    is_B_plus_C_bigger_than_A = valor_b+valor_c > valor_a
    is_A_plus_C_bigger_than_B = valor_a+valor_c > valor_b
    return is_A_plus_C_bigger_than_B and is_B_plus_C_bigger_than_A and is_A_plus_B_bigger_than_C

def isRightTriangle(valorA, valorB, valorC):
    return valorA**2 == (valorB**2+valorC**2)
def isEquilateralTriangle(valorA, valorB, valorC):
    return valorA == valorB and valorB == valorC

def isIsoscelesTriangle(valorA, valorB, valorC):
    return valorA == valorB or valorB == valorC or valorA == valorC

def isScaleneTriangle(valor_a, valor_b, valor_c):
    return valor_a != valor_b and valor_b != valor_c and valor_a != valor_b

lado_a, lado_b, lado_c = [int(x) for x in input().split()]

if is_triangle(lado_a, lado_b, lado_c):
    print('Valido-', end='')

    if isEquilateralTriangle(lado_a, lado_b, lado_c):
        print('Equilatero')
    elif isIsoscelesTriangle(lado_a, lado_b, lado_c):
        print('Isoceles')
    elif isScaleneTriangle(lado_a, lado_b, lado_c):
        print('Escaleno')

    if isRightTriangle(lado_a, lado_b, lado_c):
        print('Retangulo: S')
    else:
        print('Retangulo: N')
else:
    print('Invalido')