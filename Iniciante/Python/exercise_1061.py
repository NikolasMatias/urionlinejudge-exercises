from datetime import datetime

diaInicial = str(input()).replace('Dia', '').strip()
tempoInicial = str(input())
diaFinal = str(input()).replace('Dia', '').strip()
tempoFinal = str(input())

tempoInicialConfig = [' ', str(tempoInicial)]
tempoFinalConfig = [' ', tempoFinal]

tempoInicialConfig.insert(0, str(diaInicial).rjust(2, '0'))
tempoFinalConfig.insert(0, str(diaFinal).rjust(2, '0'))

tempoInicialConfig.insert(0, '2023-04-')
tempoFinalConfig.insert(0, '2023-04-')

timeInicial = datetime.strptime(''.join(tempoInicialConfig), '%Y-%m-%d  %H : %M : %S')
timeFinal = datetime.strptime(''.join(tempoFinalConfig), '%Y-%m-%d %H : %M : %S')
timeTotal = timeFinal - timeInicial

diasTotais = int(timeTotal.total_seconds()/3600/24)
horasTotais = int(timeTotal.total_seconds()%(3600*24)/3600)
minutosTotais = int(timeTotal.total_seconds()%(3600*24)%3600/60)
segundosTotais = int(timeTotal.total_seconds()%(3600*24)%3600%60)

print(''.join([str(diasTotais), ' dia(s)']))
print(''.join([str(horasTotais), ' hora(s)']))
print(''.join([str(minutosTotais), ' minuto(s)']))
print(''.join([str(segundosTotais), ' segundo(s)']))