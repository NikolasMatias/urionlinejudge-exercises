while True:
    try:
        num_atributos = int(input())
        num_cartas_marcos, num_cartas_leonardo = [int(x) for x in input().split()]
        cartas_marcos = [[int(x) for x in input().split()[:num_atributos]] for y in range(num_cartas_marcos)]
        cartas_leonardo = [[int(x) for x in input().split()[:num_atributos]] for y in range(num_cartas_leonardo)]
        carta_escolhida_marcos, carta_escolhida_leonardo = [int(x) for x in input().split()]
        atributo_sorteado = int(input())

        if cartas_marcos[carta_escolhida_marcos-1][atributo_sorteado-1] > cartas_leonardo[carta_escolhida_leonardo-1][atributo_sorteado-1]:
            print('Marcos')
        elif cartas_marcos[carta_escolhida_marcos-1][atributo_sorteado-1] < cartas_leonardo[carta_escolhida_leonardo-1][atributo_sorteado-1]:
            print('Leonardo')
        else:
            print('Empate')
    except EOFError: break