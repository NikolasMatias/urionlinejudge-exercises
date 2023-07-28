segundos = int(input())

horas = int(segundos/3600)
minutos = int(segundos/60%60)
segundos = int(segundos%60)

print(str(horas)+':'+str(minutos)+':'+str(segundos))