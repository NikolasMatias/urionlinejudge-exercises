while True:
    try:
        valor_n = int(input())
        valor_base_2 = valor_n -1

        for x in range(valor_n):
            for y in range(valor_n):
                if y == valor_base_2:
                    print(str(2), end='')
                    valor_base_2 -= 1
                elif x == y:
                    print(str(1), end='')
                else:
                    print(str(3), end='')
                if (y + 1) >= valor_n:
                    print('')
    except EOFError:
        break