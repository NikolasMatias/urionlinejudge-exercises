opcoes = {
    'papel': [],
    'pedra': ['papel'],
    'ataque': ['pedra', 'papel']
}
count_partidas = int(input())
for x in range(count_partidas):
    jogador_1 = input()
    jogador_2 = input()
    if jogador_1 == jogador_2:
        if jogador_1 == 'papel':
            print('Ambos venceram')
        elif jogador_1 == 'pedra':
            print('Sem ganhador')
        elif jogador_1 == 'ataque':
            print('Aniquilacao mutua')
    elif jogador_2 in opcoes[jogador_1]:
        print('Jogador 1 venceu')
    elif jogador_1 in opcoes[jogador_2]:
        print('Jogador 2 venceu')