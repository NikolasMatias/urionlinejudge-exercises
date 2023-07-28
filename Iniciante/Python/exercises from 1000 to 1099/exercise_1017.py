def calculateLitros(horasViagem, velocidadeMedia):
    distancia = velocidadeMedia*horasViagem

    qtdeLitros = distancia / 12.0

    print("{:.3f}".format(qtdeLitros))

calculateLitros(int(input()), int(input()))