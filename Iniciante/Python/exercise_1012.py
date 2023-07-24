valorA, valorB, valorC = [float(x) for x in input().split()]
pi = 3.14159

areaTriangulo = (valorA*valorC)/2
areaCirculo = pi*valorC**2
areaTrapezio = ((valorA+valorB)*valorC)/2
areaQuadrado = valorB**2
areaRetangulo = valorA*valorB

print(''.join(['TRIANGULO: ', "{:.3f}".format(areaTriangulo)]))
print(''.join(['CIRCULO: ', "{:.3f}".format(areaCirculo)]))
print(''.join(['TRAPEZIO: ', "{:.3f}".format(areaTrapezio)]))
print(''.join(['QUADRADO: ', "{:.3f}".format(areaQuadrado)]))
print(''.join(['RETANGULO: ', "{:.3f}".format(areaRetangulo)]))