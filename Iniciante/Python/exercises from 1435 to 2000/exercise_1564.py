while True:
    try:
        valor_n = int(input())
        if valor_n > 0:
            print('vai ter duas!')
        else:
            print('vai ter copa!')
    except EOFError:
        break