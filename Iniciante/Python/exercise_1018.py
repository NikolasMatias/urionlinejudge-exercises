def pegarCedulaPorTipo(dinheiro, tipo):
    return int(dinheiro/tipo)

def pegarCedulas(dinheiro):
    notas100 = pegarCedulaPorTipo(dinheiro, 100)
    notas50 = pegarCedulaPorTipo((dinheiro-(100*notas100)), 50)
    notas20 = pegarCedulaPorTipo((dinheiro-(100*notas100)-(50*notas50)), 20)
    notas10 = pegarCedulaPorTipo((dinheiro-(100*notas100)-(50*notas50)-(20*notas20)), 10)
    notas5 = pegarCedulaPorTipo((dinheiro-(100*notas100)-(50*notas50)-(20*notas20)-(10*notas10)), 5)
    notas2 = pegarCedulaPorTipo((dinheiro-(100*notas100)-(50*notas50)-(20*notas20)-(10*notas10)-(5*notas5)), 2)
    notas1 = pegarCedulaPorTipo((dinheiro-(100*notas100)-(50*notas50)-(20*notas20)-(10*notas10)-(5*notas5)-(2*notas2)), 1)
    return [dinheiro, notas100, notas50, notas20, notas10, notas5, notas2, notas1]

dinheiro, notas100, notas50, notas20, notas10, notas5, notas2, notas1 = pegarCedulas(int(input()))

print(str(dinheiro))
print(''.join([str(notas100), ' nota(s) de R$ 100,00']))
print(''.join([str(notas50), ' nota(s) de R$ 50,00']))
print(''.join([str(notas20), ' nota(s) de R$ 20,00']))
print(''.join([str(notas10), ' nota(s) de R$ 10,00']))
print(''.join([str(notas5), ' nota(s) de R$ 5,00']))
print(''.join([str(notas2), ' nota(s) de R$ 2,00']))
print(''.join([str(notas1), ' nota(s) de R$ 1,00']))