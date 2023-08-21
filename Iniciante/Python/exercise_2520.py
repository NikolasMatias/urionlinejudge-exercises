while True:
    try:
        linhas, colunas = [int(x) for x in input().split()]
        matriz = [[int(x) for x in input().split()[:colunas]] for y in range(linhas)]
        posicao_player = []
        posicao_analogimon = []
        distancia_percorrida = 0
        for x in range(linhas):
            for y in range(colunas):
                if matriz[x][y] == 1:
                    posicao_player = [x, y]
                elif matriz[x][y] == 2:
                    posicao_analogimon = [x, y]
                if len(posicao_player) > 0 and len(posicao_analogimon) > 0:
                    break
            else:
                continue
            break
        posicoes_x = [posicao_player[0], posicao_analogimon[0]]
        posicoes_y = [posicao_player[1], posicao_analogimon[1]]
        posicoes_x.sort(reverse=True)
        posicoes_y.sort(reverse=True)
        distancia_percorrida = (posicoes_x[0] - posicoes_x[1]) + (posicoes_y[0] - posicoes_y[1])
        print(str(distancia_percorrida))
    except EOFError: break