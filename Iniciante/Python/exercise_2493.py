def is_calculo_possible(valor_a, valor_b, resultado_calculo):
    return valor_a+valor_b == resultado_calculo or valor_a-valor_b == resultado_calculo or valor_a*valor_b == resultado_calculo
def test_calculo(calculo, expressao_escolhida):
    valor_a,valor_b, resultado_calculo = [int(x) for x in calculo.replace('=', ' ').split()]
    if expressao_escolhida == 'I':
        return not is_calculo_possible(valor_a, valor_b, resultado_calculo)
    if expressao_escolhida == '+':
        return valor_a+valor_b == resultado_calculo
    if expressao_escolhida == '-':
        return valor_a-valor_b == resultado_calculo
    if expressao_escolhida == '*':
        return valor_a*valor_b == resultado_calculo



while True:
    try:
        qtdeExpressoes = int(input())
        expressoes = [input() for x in range(qtdeExpressoes)]
        respostaJogadores = [input() for x in range(qtdeExpressoes)]
        jogadoresErrados = []
        for resposta_jogador in respostaJogadores:
            nome_jogador, indice, resposta = resposta_jogador.split()
            if not test_calculo(expressoes[int(indice)-1], resposta):
                jogadoresErrados.append(nome_jogador)
        if len(jogadoresErrados) == 0:
            print('You Shall All Pass!')
        elif len(jogadoresErrados) == len(respostaJogadores):
            print('None Shall Pass!')
        else:
            jogadoresErrados.sort()
            print(' '.join(jogadoresErrados))
    except EOFError:
        break