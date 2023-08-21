pi = 3.14
while True:
    try:
        volume = float('{:.2f}'.format(float(input())))
        diametro = float('{:.2f}'.format(float(input())))
        raio = diametro/2
        area = pi * raio**2
        altura = volume / area
        print(''.join(['ALTURA = ', '{:.2f}'.format(altura)]))
        print(''.join(['AREA = ', '{:.2f}'.format(area)]))
    except EOFError:
        break