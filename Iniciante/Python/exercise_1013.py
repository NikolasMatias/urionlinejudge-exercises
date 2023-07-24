def max(valorA, valorB):
    return (valorA+valorB+abs(valorA-valorB))/2

valorA, valorB, valorC = [int(x) for x in input().split()]

maiorValor = max(valorA, valorB)
maiorValor = int(max(maiorValor, valorC))

print(''.join([str(maiorValor), ' eh o maior']))