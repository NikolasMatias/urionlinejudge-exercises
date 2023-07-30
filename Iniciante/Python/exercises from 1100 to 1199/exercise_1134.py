combustivelList = []

while True:
    combustivel = int(input())
    if combustivel == 4:
        break
    elif combustivel in [1,2,3]:
        combustivelList.append(combustivel)

countAlcool = len(list(
    filter(lambda combustivel: combustivel == 1, combustivelList)
))
countGasolina = len(list(
    filter(lambda combustivel: combustivel == 2, combustivelList)
))
countDiesel = len(list(
    filter(lambda combustivel: combustivel == 3, combustivelList)
))

print('MUITO OBRIGADO')
print(''.join(['Alcool: ', str(countAlcool)]))
print(''.join(['Gasolina: ', str(countGasolina)]))
print(''.join(['Diesel: ', str(countDiesel)]))