count_casos = int(input())
for x in range(count_casos):
    hora, minuto, ocorrencia = [int(y) for y in input().split()]
    print(':'.join([str(hora).zfill(2), str(minuto).zfill(2)]), end='')
    if ocorrencia:
        print(' - A porta abriu!')
    else:
        print(' - A porta fechou!')