while True:
    try:
        linhas, colunas = [int(x) for x in input().split()]
        matrizInicial = [[int(x) for x in input().split()[:colunas]] for y in range(linhas)]
        matrizFinal = [[0 for x in range(colunas)] for y in range(linhas)]
        for x in range(linhas):
            for y in range(colunas):
                if matrizInicial[x][y] == 1:
                    matrizFinal[x][y] = 9
                else:
                    if (y+1) < colunas and matrizInicial[x][y+1] == 1:
                        matrizFinal[x][y] += 1
                    if (x+1) < linhas and matrizInicial[x+1][y] == 1:
                        matrizFinal[x][y] += 1
                    if (x-1) >= 0 and matrizInicial[x-1][y] == 1:
                        matrizFinal[x][y] += 1
                    if (y-1) >= 0 and matrizInicial[x][y-1] == 1:
                        matrizFinal[x][y] += 1
        for x in range(linhas):
            for y in range(colunas):
                print(str(matrizFinal[x][y]), end='')
                if y+1 == colunas:
                    print()
    except EOFError: break