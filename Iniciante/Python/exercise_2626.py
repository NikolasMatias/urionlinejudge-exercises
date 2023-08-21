def isJogador1WinnerOfRockPaperScissors(jogador1, jogador2):
    if jogador1 == 'papel' and jogador2 == 'pedra':
        return True


while True:
    try:
        dodo, leo, pepper = input().split()
    except EOFError: break