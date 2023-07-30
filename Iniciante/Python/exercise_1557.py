import math

while True:
    countLoop = int(input())
    if countLoop == 0:
        break
    matriz = []
    for x in range(countLoop):
        matriz.append([])
        for y in range(countLoop):
            matriz[x].append(0)
    for x in range(countLoop):
        for y in range(countLoop):
            if y == 0:
                matriz[x][y] = 2**x
            else:
                matriz[x][y] = matriz[x][y-1]*2

    digits = int(math.log10(matriz[countLoop-1][countLoop-1])) + 1
    for x in range(countLoop):
        print(' '.join([''.join(['{:',str(digits),'d}']).format(y) for y in matriz[x]]))
    print('')