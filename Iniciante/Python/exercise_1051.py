def calcularValorImpostoRenda(salario):
    if salario >= 0 and salario <= 2000:
        return 'Isento'
    if salario > 2000 and salario <= 3000:
        valorImpostoRenda = (salario - 2000) * 0.08
        return ''.join(['R$ ',"{:.2f}".format(valorImpostoRenda)])
    if salario > 3000 and salario <= 4500:
        valorImpostoRenda = (1000 * 0.08) + ((salario - 3000) * 0.18)
        return ''.join(['R$ ',"{:.2f}".format(valorImpostoRenda)])
    if salario > 4500:
        valorImpostoRenda = (1000 * 0.08) + (1500 * 0.18) + ((salario-4500) * 0.28)
        return ''.join(['R$ ',"{:.2f}".format(valorImpostoRenda)])

salarioAtual = float("{:.2f}".format(float(input())))
print(calcularValorImpostoRenda(salarioAtual))

