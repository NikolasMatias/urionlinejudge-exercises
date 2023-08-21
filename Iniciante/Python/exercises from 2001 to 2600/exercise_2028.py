count_casos = 0
while True:
    try:
        count_casos += 1
        number = int(input())
        lista_number = [0]
        if number > 0:
            for x in range(1, number+1):
                lista_number.extend([x]*x)
        print(''.join(['Caso ', str(count_casos), ': ', str(len(lista_number)), ' numeros' if len(lista_number) > 1 else ' numero']))
        print(' '.join([str(x) for x in lista_number]))
        print()
    except EOFError:
        break