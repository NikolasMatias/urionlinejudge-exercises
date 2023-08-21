while True:
    try:
        num_jogadores = int(input())
        voto_jogadores = [int(x) for x in input().split()[:num_jogadores]]
        if sum(voto_jogadores)/num_jogadores >= 2/3:
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError: break