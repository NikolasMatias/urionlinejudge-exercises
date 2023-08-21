while True:
    try:
        num_treinos = int(input())
        treinos = [[int(x) for x in input().split()[:2]] for y in range(num_treinos)]
        record = treinos[0][1]/treinos[0][0]
        for indice_treino in range(num_treinos):
            if indice_treino > 0:
                resultado = treinos[indice_treino][1] / treinos[indice_treino][0]
                if resultado > record:
                    record = resultado
                    print(str(indice_treino+1))
            else:
                print('1')
    except EOFError: break