count_caso = 0
while True:
    try:
        count_caso += 1
        substring = str(int(input()))
        whole_string = str(int(input()))
        qtde_subsequencias = whole_string.count(substring)
        print(''.join(['Caso #', str(count_caso), ':']))
        if qtde_subsequencias > 0:
            posicao = whole_string.rfind(substring)
            print(''.join(['Qtd.Subsequencias: ', str(qtde_subsequencias)]))
            print(''.join(['Pos: ', str(posicao+1)]))
        else:
            print('Nao existe subsequencia')
        print()
    except EOFError:
        break