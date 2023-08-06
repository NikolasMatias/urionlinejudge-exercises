from datetime import date
def days_for_xmas(mes, dias):
    actual_date = date(2016, mes, dias)
    xmas_date = date(2016, 12, 25)
    delta = xmas_date - actual_date
    return int(delta.days)
while True:
    try:
        mes, dia = [int(x) for x in input().split()]
        dias_faltando = 0
        if mes == 12:
            if dia == 24:
                print('E vespera de natal!')
            elif dia == 25:
                print('E natal!')
            elif dia > 25:
                print('Ja passou!')
            else:
                dias_faltando = days_for_xmas(mes, dia)
        else:
            dias_faltando = days_for_xmas(mes, dia)
        if dias_faltando > 0:
            print(''.join(['Faltam ', str(dias_faltando),' dias para o natal!']))


    except EOFError:
        break