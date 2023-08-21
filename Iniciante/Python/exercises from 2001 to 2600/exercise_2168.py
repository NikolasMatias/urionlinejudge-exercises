valor_n = int(input())
matriz = [[int(x) for x in input().split()] for y in range(valor_n+1)]
for x in range(valor_n):
    for y in range(valor_n):
        if (matriz[x][y] + matriz[x][y + 1] + matriz[x + 1][y] + matriz[x + 1][y + 1]) >= 2:
            print('S', end='')
        else:
            print('U', end='')
    print()