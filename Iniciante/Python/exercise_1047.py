from datetime import datetime
import datetime as original_datetime

horaInicial, minutoInicial, horaFinal, minutoFinal = [int(x) for x in input().split()]

now = datetime.now().strftime('%Y-%m-%d')

tempoInicial = [now, ' ', str(horaInicial), ':', str(minutoInicial)]
tempoFinal = [str(horaFinal), ':', str(minutoFinal)]

if horaInicial > horaFinal or (horaInicial == horaFinal and minutoInicial > minutoFinal):
    tomorrow = (datetime.now() + original_datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    tempoFinal.insert(0, ' ')
    tempoFinal.insert(0, tomorrow)
else:
    tempoFinal.insert(0, ' ')
    tempoFinal.insert(0, now)


timeInicial = datetime.strptime(''.join(tempoInicial), '%Y-%m-%d %H:%M')
timeFinal = datetime.strptime(''.join(tempoFinal), '%Y-%m-%d %H:%M')
timeTotal = timeFinal - timeInicial
horaTotal = int(timeTotal.total_seconds()/60/60)
minutoTotal = int(timeTotal.total_seconds()%3600/60)

if horaInicial == minutoInicial and horaFinal == minutoFinal and horaInicial == horaFinal:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(''.join(['O JOGO DUROU ', str(horaTotal), ' HORA(S) E ', str(minutoTotal),' MINUTO(S)']))