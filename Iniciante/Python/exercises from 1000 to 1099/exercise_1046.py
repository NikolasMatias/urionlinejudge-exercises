horaInicial, horaFinal = [int(x) for x in input().split()]
horaTotal = 24

if horaInicial > horaFinal:
    horaFinal = horaFinal + 24
    horaTotal = horaFinal - horaInicial
elif horaInicial < horaFinal:
    horaTotal = horaFinal - horaInicial

print(''.join(['O JOGO DUROU ', str(horaTotal), ' HORA(S)']))
# print(f"O JOGO DUROU {horaTotal} HORA(S)")