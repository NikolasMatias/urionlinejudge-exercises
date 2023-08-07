countLoop = int(input())
for x in range(countLoop):
    bonus = int(input())
    ataqueD, defesaD, levelD = [int(y) for y in input().split()]
    ataqueG, defesaG, levelG = [int(y) for y in input().split()]
    valor_golpe_d = ((ataqueD+defesaD)/2)+(bonus if levelD%2 == 0 else 0)
    valor_golpe_g = ((ataqueG+defesaG)/2)+(bonus if levelG%2 == 0 else 0)
    if valor_golpe_g == valor_golpe_d:
        print('Empate')
    elif valor_golpe_g > valor_golpe_d:
        print('Guarte')
    elif valor_golpe_d > valor_golpe_g:
        print('Dabriel')