linhas, colunas = [int(x) for x in input().split()]
matriz = []
x_encontrado = 0
y_encontrado = 0
for x in range(linhas):
    matriz.append([int(y) for y in input().split()])
for x in range(linhas):
    for y in range(colunas):
        if matriz[x][y] == 42 and 0 < x < (linhas - 1) and 0 < y < (colunas - 1):
            is_seven_up = matriz[x - 1][y - 1] == 7 and matriz[x - 1][y + 1] == 7 and matriz[x - 1][y] == 7
            is_seven_middle = matriz[x][y - 1] == 7 and matriz[x][y + 1] == 7
            is_seven_down = matriz[x + 1][y + 1] == 7 and matriz[x + 1][y] == 7 and matriz[x + 1][y - 1] == 7
            if is_seven_down and is_seven_up and is_seven_down:
                x_encontrado = x+1
                y_encontrado = y+1
                break
print(str(x_encontrado), str(y_encontrado))