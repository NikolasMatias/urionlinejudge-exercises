def isJogador1WinnerOfRockPaperScissors(jogador1, jogador2):
    if jogador1 == 'papel' and jogador2 == 'pedra':
        return True
    if jogador1 == 'tesoura' and jogador2 == 'papel':
        return True
    if jogador1 ==  'pedra' and jogador2 == 'tesoura':
        return True
    return False


while True:
    try:
        dodo, leo, pepper = input().split()
        if isJogador1WinnerOfRockPaperScissors(dodo, leo) and isJogador1WinnerOfRockPaperScissors(dodo, pepper):
            print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
        elif isJogador1WinnerOfRockPaperScissors(leo, dodo) and isJogador1WinnerOfRockPaperScissors(leo, pepper):
            print("Iron Maiden's gonna get you, no matter how far!")
        elif isJogador1WinnerOfRockPaperScissors(pepper, dodo) and isJogador1WinnerOfRockPaperScissors(pepper, leo):
            print('Urano perdeu algo muito precioso...')
        else:
            print('Putz vei, o Leo ta demorando muito pra jogar...')
    except EOFError: break