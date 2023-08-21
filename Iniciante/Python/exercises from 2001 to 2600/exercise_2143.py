while True:
    valor_n = int(input())
    if not valor_n:
        break
    pessoas = []
    while valor_n:
        valor_n -= 1
        valor_x = int(input())
        if valor_x %2 == 0:
            pessoas.append((valor_x*2)-2)
        else:
            pessoas.append((valor_x * 2)-1)
    for pessoa in pessoas:
        print(pessoa)
