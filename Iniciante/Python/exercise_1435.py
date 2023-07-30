while True:
    countLoop = int(input())
    if countLoop == 0:
        break
    matriz = []
    for x in range(countLoop):
        matriz.append([])

    for x in range(countLoop):
        for y in range(countLoop):
            matriz[x].append(1)

    for x in range(countLoop):
        for y in range(countLoop):
            baseX = x+1
            baseY = y+1
            baseValue = min([x,y])+1
            matriz[x][y] = baseValue

            if x == 4 and y == 3:
                teste = 1

            if (countLoop - baseX + 1) < baseValue:
                matriz[x][y] = countLoop - baseX + 1

            if (countLoop - baseY + 1) < baseValue:
                matriz[x][y] = countLoop - baseY + 1


    for x in range(countLoop):
        print(' '.join([str(y) for y in matriz[x]]).strip())