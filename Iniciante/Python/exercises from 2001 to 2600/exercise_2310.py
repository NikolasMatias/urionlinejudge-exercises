num_jogadores = int(input())
tentativas_totais = [0]*3
sucessos_totais = [0]*3
for x in range(num_jogadores):
    nome_jogador = input()
    saque_ten, bloqueio_ten, ataque_ten = [int(y) for y in input().split()]
    saque_suc, bloqueio_suc, ataque_suc = [int(y) for y in input().split()]
    tentativas_totais[0] += saque_ten
    tentativas_totais[1] += bloqueio_ten
    tentativas_totais[2] += ataque_ten
    sucessos_totais[0] += saque_suc
    sucessos_totais[1] += bloqueio_suc
    sucessos_totais[2] += ataque_suc
print(' '.join(['Pontos de Saque:', '{:.2f}'.format((sucessos_totais[0]/tentativas_totais[0])*100), '%.']))
print(' '.join(['Pontos de Bloqueio:', '{:.2f}'.format((sucessos_totais[1]/tentativas_totais[1])*100), '%.']))
print(' '.join(['Pontos de Ataque:', '{:.2f}'.format((sucessos_totais[2]/tentativas_totais[2])*100), '%.']))