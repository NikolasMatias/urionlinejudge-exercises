codigo1, numPecas1, valorUnitario1 = input().split()
codigo2, numPecas2, valorUnitario2 = input().split()

codigo1 = int(codigo1)
numPecas1 = int(numPecas1)
valorUnitario1 = float(valorUnitario1)

codigo2 = int(codigo2)
numPecas2 = int(numPecas2)
valorUnitario2 = float(valorUnitario2)

valorAPagar = (numPecas1*valorUnitario1)+(numPecas2*valorUnitario2)

print(''.join(['VALOR A PAGAR: R$ ', "{:.2f}".format(valorAPagar)]))