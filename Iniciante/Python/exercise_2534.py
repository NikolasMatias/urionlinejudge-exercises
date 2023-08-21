while True:
    try:
        num_populacao, num_consultas = [int(x) for x in input().split()]
        nota_populacao = [int(input()) for x in range(num_populacao)]
        consultas = [int(input()) for x in range(num_consultas)]
        nota_populacao.sort(reverse=True)
        for consulta in consultas:
            print(nota_populacao[consulta-1])
    except EOFError: break