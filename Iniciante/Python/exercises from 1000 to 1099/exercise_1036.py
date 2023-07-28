valorA, valorB, valorC = [float(x) for x in input().split()]

delta = valorB**2 - (4*valorA*valorC)

if valorA > 0 and delta >= 0:
    raiz1 = (-valorB + (delta)**(1/2))/(2*valorA)
    raiz2 = (-valorB - (delta)**(1/2))/(2*valorA)

    print(''.join(['R1 = ', "{:.5f}".format(raiz1)]))
    print(''.join(['R2 = ', "{:.5f}".format(raiz2)]))
else:
    print('Impossivel calcular')