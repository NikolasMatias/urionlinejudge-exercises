countCaws = 0

while countCaws < 3:
    valores = []
    while True:
        enter_value = input()
        if enter_value == 'caw caw':
            countCaws += 1
            break
        valores.append(enter_value.replace('-', '0').replace('*', '1'))
    for x in range(len(valores)):
        valores[x] = int(valores[x], 2)
    print(str(sum(valores)))