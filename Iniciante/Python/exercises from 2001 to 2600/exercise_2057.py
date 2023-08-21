hora_saida, tempo_viagem, fuso_horario = [int(x) for x in input().split()]
if hora_saida == 0 and fuso_horario < 0:
    hora_saida = 24
hora_saida = hora_saida + fuso_horario
hora_chegada = hora_saida + tempo_viagem
if hora_chegada >= 24:
    hora_chegada -= 24
print(str(hora_chegada))