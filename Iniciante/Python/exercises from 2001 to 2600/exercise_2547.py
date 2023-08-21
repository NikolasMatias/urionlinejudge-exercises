while True:
    try:
        num_visitantes, altura_minima, altura_maxima = [int(x) for x in input().split()]
        altura_visitantes = [int(input()) for x in range(num_visitantes)]
        num_permitidos = sum(
            [1 if altura_visitante >= altura_minima and altura_visitante <= altura_maxima else 0 for altura_visitante in
             altura_visitantes])
        print(str(num_permitidos))
    except EOFError: break