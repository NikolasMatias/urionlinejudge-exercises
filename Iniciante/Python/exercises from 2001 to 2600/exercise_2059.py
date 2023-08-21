valor_p, jogador_1, jogador_2, roubo, acusacao = [int(x) for x in input().split()]
ganhador = ''
if roubo or acusacao:
    if roubo and acusacao:
        ganhador = '2'
    elif (roubo and acusacao == 0) or (roubo == 0 and acusacao):
        ganhador = '1'
elif sum([jogador_1, jogador_2])%2 == 0:
    ganhador = '1' if valor_p == 1 else '2'
else:
    ganhador = '1' if valor_p == 0 else '2'
print(''.join(['Jogador ', ganhador, ' ganha!']))