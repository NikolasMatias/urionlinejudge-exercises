while True:
    try:
        x_f, y_f, x_i, y_i, v_i, raio_1, raio_2 = [int(x) for x in input().split()]

        distancia_f_de_i = ((x_i - x_f) ** 2 + (y_i - y_f) ** 2) ** (1 / 2)
        distancia_i_final = distancia_f_de_i + v_i * 1.5
        distancia_f_final = raio_1 + raio_2
        if distancia_f_final >= distancia_i_final:
            print('Y')
        else:
            print('N')

    except EOFError:
        break