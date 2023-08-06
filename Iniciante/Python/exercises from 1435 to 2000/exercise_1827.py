while True:
    try:
        valor_n = int(input())
        base_1 = int(valor_n/3)
        limit_1 = int(valor_n-base_1)
        matriz = [[0 for i in range(valor_n)] for j in range(valor_n)]

        for x in range(valor_n):
            matriz[x][x] = 2

        x = 0
        for y in range(valor_n-1, -1, -1):
            matriz[x][y] = 3
            x += 1

        for x in range(base_1, limit_1):
            for y in range(base_1, limit_1):
                matriz[x][y] = 1

        matriz[int(valor_n/2)][int(valor_n/2)] = 4

        for x in range(valor_n):
            for y in range(valor_n):
                print(str(matriz[x][y]), end='')
            print()
        print()
    except EOFError:
        break