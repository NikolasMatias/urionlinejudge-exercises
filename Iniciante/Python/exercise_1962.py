countLoop = int(input())

for x in range(countLoop):
    valor_n = int(input())
    anos_passados = 2015 - valor_n
    if anos_passados <= 0:
        anos_passados = abs(anos_passados)+1
        print(''.join([str(anos_passados), ' A.C.']))
    else:
        print(''.join([str(anos_passados), ' D.C.']))