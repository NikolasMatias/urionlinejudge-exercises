def calcularValorReajuste(salario):
    if salario >= 0 and salario <= 400:
        return ['15', salario * 0.15]
    elif salario > 400 and salario <= 800:
        return ['12', salario * 0.12]
    elif salario > 800 and salario <= 1200:
        return ['10', salario * 0.1]
    elif salario > 1200 and salario <= 2000:
        return ['7', salario * 0.07]
    else:
        return ['4', salario * 0.04]

salarioAtual = float("{:.2f}".format(float(input())))
porcentagemReajuste, valorReajuste = calcularValorReajuste(salarioAtual)
salarioNovo = salarioAtual + valorReajuste

print(''.join(['Novo salario: ', "{:.2f}".format(salarioNovo)]))
print(''.join(['Reajuste ganho: ', "{:.2f}".format(valorReajuste)]))
print(''.join(['Em percentual: ', str(porcentagemReajuste), ' %']))