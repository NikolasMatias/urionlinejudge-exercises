def play_bazinga(jogador1, jogador2):
    if jogador1 == jogador2:
        return 'De novo!'
    opcoes = {
        'tesoura': ['papel', 'lagarto'],
        'papel': ['pedra', 'Spock'],
        'pedra': ['lagarto', 'tesoura'],
        'lagarto': ['Spock', 'papel'],
        'Spock': ['tesoura', 'pedra']
    }
    if jogador2 in opcoes[jogador1]:
        return 'Bazinga!'
    elif jogador1 in opcoes[jogador2]:
        return 'Raj trapaceou!'

countLoop = int(input())
for x in range(1, countLoop+1):
    jogador1, jogador2 = [str(x) for x in input().split()]
    resultado = play_bazinga(jogador1, jogador2)
    print(''.join(['Caso #', str(x), ': ', resultado]))