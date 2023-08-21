numAtletas = int(input())

for x in range(numAtletas):
    name = str(input())
    notaPartida = float(input())
    notasJuizes = [float(y) for y in input().split()]
    notasJuizes.sort()
    notasJuizes.pop(0)
    notasJuizes.pop(-1)
    notaFinal = sum(notasJuizes)*notaPartida
    print(' '.join([name, '{:.2f}'.format(notaFinal)]))