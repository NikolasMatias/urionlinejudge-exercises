eixoX, eixoY = [float(x) for x in input().split()]

if eixoX == 0 and eixoY == 0:
    print('Origem')
elif eixoX == 0 and eixoY != 0:
    print('Eixo Y')
elif eixoX != 0 and eixoY == 0:
    print('Eixo X')
else:
    if eixoX > 0:
        if eixoY > 0:
            print('Q1')
        else:
            print('Q4')
    else:
        if eixoY > 0:
            print('Q2')
        else:
            print('Q3')