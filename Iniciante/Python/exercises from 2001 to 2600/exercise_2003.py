while True:
    try:
        hora, minuto = [int(x) for x in input().split(':')]
        if hora >= 7:
            if minuto > 0 or hora > 7:
                atraso = (hora-7)*60 + minuto
                print(''.join(['Atraso maximo: ', str(atraso)]))
            else:
                print('Atraso maximo: 0')
        else:
            print('Atraso maximo: 0')
    except EOFError:
        break