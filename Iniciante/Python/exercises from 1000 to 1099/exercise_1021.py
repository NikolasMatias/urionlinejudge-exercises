import math

def pegarCedulaPorTipo(dinheiro, tipo):
    return int(dinheiro/tipo)

def pegarNotasEMoedas(dinheiro):
    notas100 = pegarCedulaPorTipo(dinheiro, 100)
    notas50 = pegarCedulaPorTipo((dinheiro-(100*notas100)), 50)
    notas20 = pegarCedulaPorTipo((dinheiro-(100*notas100)-(50*notas50)), 20)
    notas10 = pegarCedulaPorTipo((dinheiro-(100*notas100)-(50*notas50)-(20*notas20)), 10)
    notas5 = pegarCedulaPorTipo((dinheiro-(100*notas100)-(50*notas50)-(20*notas20)-(10*notas10)), 5)
    notas2 = pegarCedulaPorTipo((dinheiro-(100*notas100)-(50*notas50)-(20*notas20)-(10*notas10)-(5*notas5)), 2)

    moedas100 = pegarCedulaPorTipo(dinheiro%100%50%20%10%5%2, 1)
    moedas50 = pegarCedulaPorTipo(((dinheiro-(math.floor(dinheiro)))*100), 50)
    moedas25 = pegarCedulaPorTipo(((dinheiro-(math.floor(dinheiro)))*100)%50, 25)
    moedas10 = pegarCedulaPorTipo(((dinheiro-(math.floor(dinheiro)))*100)%50%25, 10)
    moedas5 = pegarCedulaPorTipo(((dinheiro-(math.floor(dinheiro)))*100)%50%25%10, 5)
    moedas1 = pegarCedulaPorTipo(((dinheiro-(math.floor(dinheiro)))*100)%50%25%10%5, 1)

    return [dinheiro, notas100, notas50, notas20, notas10, notas5, notas2, moedas100, moedas50, moedas25, moedas10, moedas5, moedas1]

dinheiro, notas100, notas50, notas20, notas10, notas5, notas2, moedas100, moedas50, moedas25, moedas10, moedas5, moedas1 = pegarNotasEMoedas(float(input()))

print('NOTAS:')
print(''.join([str(notas100), ' nota(s) de R$ 100.00']))
print(''.join([str(notas50), ' nota(s) de R$ 50.00']))
print(''.join([str(notas20), ' nota(s) de R$ 20.00']))
print(''.join([str(notas10), ' nota(s) de R$ 10.00']))
print(''.join([str(notas5), ' nota(s) de R$ 5.00']))
print(''.join([str(notas2), ' nota(s) de R$ 2.00']))

print('MOEDAS:')
print(''.join([str(moedas100), ' moeda(s) de R$ 1.00']))
print(''.join([str(moedas50), ' moeda(s) de R$ 0.50']))
print(''.join([str(moedas25), ' moeda(s) de R$ 0.25']))
print(''.join([str(moedas10), ' moeda(s) de R$ 0.10']))
print(''.join([str(moedas5), ' moeda(s) de R$ 0.05']))
print(''.join([str(moedas1), ' moeda(s) de R$ 0.01']))
